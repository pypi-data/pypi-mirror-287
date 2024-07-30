import os
import subprocess
from tqdm import tqdm
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CloneProgress(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def check_git_installation():
    """Check if Git is installed on the system."""
    logger.info("Checking for Git installation")
    try:
        subprocess.run(['git', '--version'], check=True)
    except subprocess.CalledProcessError:
        logger.error("Git is not installed. Please install Git and try again.")
        raise

def is_git_lfs_installed():
    """Check if Git LFS is installed."""
    try:
        result = subprocess.run(['git', 'lfs', 'version'], check=True, capture_output=True, text=True)
        logger.info("Git LFS is already installed: %s", result.stdout.strip())
        return True
    except subprocess.CalledProcessError:
        return False

def install_git_lfs():
    """Install Git LFS if it is not already installed."""
    if not is_git_lfs_installed():
        logger.info("Installing Git LFS")
        try:
            subprocess.run(['git', 'lfs', 'install'], check=True)
            logger.info("Git LFS installed successfully.")
        except subprocess.CalledProcessError:
            logger.error("Failed to install Git LFS.")
            raise
    else:
        logger.info("Git LFS is already installed. No need to install.")

def clone_repository(repo_url, output_dir):
    """Clone the repository to the specified directory."""
    logger.info(f"Cloning repository from {repo_url} to {output_dir}")
    try:
        with CloneProgress(unit='B', unit_scale=True, miniters=1, desc="Cloning Repository") as progress:
            process = subprocess.Popen(['git', 'clone', '--progress', repo_url, output_dir], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in process.stdout:
                progress.update(len(line))
                logger.info(line.decode().strip())
            process.wait()
            if process.returncode != 0:
                raise subprocess.CalledProcessError(process.returncode, 'git clone')
        logger.info("Clone completed")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error during clone: {e}")
        raise

def pull_latest_changes(output_dir):
    """Pull the latest changes in the existing repository."""
    logger.info("Pulling latest changes in existing directory")
    try:
        with CloneProgress(unit='B', unit_scale=True, miniters=1, desc="Updating Repository") as progress:
            process = subprocess.Popen(['git', 'pull', 'origin', 'main'], cwd=output_dir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in process.stdout:
                progress.update(len(line))
                logger.info(line.decode().strip())
            process.wait()
            if process.returncode != 0:
                raise subprocess.CalledProcessError(process.returncode, 'git pull')
        logger.info("Update completed")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error during pull: {e}")
        raise

def fetch_lfs_objects(output_dir):
    """Fetch LFS objects for the repository."""
    logger.info("Fetching LFS objects")
    try:
        with CloneProgress(unit='B', unit_scale=True, miniters=1, desc="Fetching LFS Objects") as progress:
            process = subprocess.Popen(['git', 'lfs', 'pull'], cwd=output_dir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in process.stdout:
                progress.update(len(line))
                logger.info(line.decode().strip())
            process.wait()
            if process.returncode != 0:
                raise subprocess.CalledProcessError(process.returncode, 'git lfs pull')
        logger.info("LFS objects fetched")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error during LFS pull: {e}")
        raise

def clone(repo_url=None, remote_host="https://a.dev.societyai.com/", repo_name=None, output_dir="./storage", access_token=None):
    """
    Clone a repository from a given URL, remote host, or repository name.

    Parameters:
    - repo_url (str): Full URL of the repository to clone.
    - remote_host (str): Remote host URL.
    - repo_name (str): Repository name (required if remote_host is provided).
    - output_dir (str): Directory to clone the repository into.
    - access_token (str): Access token for private repositories (optional).
    """
    # Check for access token from environment variable
    env_access_token = os.getenv('SOCIETYAI_ACCESS_TOKEN')
    if env_access_token:
        access_token = env_access_token

    if repo_url is None and remote_host and repo_name:
        repo_url = f"{remote_host}/{repo_name}"
    elif repo_url is None:
        raise ValueError("Either 'repo_url' or both 'remote_host' and 'repo_name' must be provided.")

    # Extract the repository name
    repo_dir_name = repo_name.split("/").pop()

    # Create the full path to clone into
    output_path = Path(output_dir) / repo_dir_name

    if access_token:
        # Embed the access token in the URL
        repo_url = repo_url.replace("https://", f"https://{access_token}@")

    try:
        check_git_installation()
        install_git_lfs()

        if output_path.exists():
            pull_latest_changes(output_path)
        else:
            clone_repository(repo_url, output_path)
            fetch_lfs_objects(output_path)

    except Exception as e:
        logger.error(f"Error cloning repository: {e}")
        raise

__all__ = ['clone']
