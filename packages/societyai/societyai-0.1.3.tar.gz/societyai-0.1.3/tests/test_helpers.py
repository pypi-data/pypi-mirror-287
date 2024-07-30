import unittest
import os
import subprocess
from unittest.mock import patch, MagicMock
from societyai.helpers import (
    check_git_installation,
    install_git_lfs,
    clone_repository,
    pull_latest_changes,
    fetch_lfs_objects,
    clone
)


class TestHelpers(unittest.TestCase):

    @patch('subprocess.run')
    def test_check_git_installation(self, mock_run):
        check_git_installation()
        mock_run.assert_called_once_with(['git', '--version'], check=True)

    @patch('subprocess.run')
    def test_install_git_lfs(self, mock_run):
        install_git_lfs()
        mock_run.assert_called_once_with(['git', 'lfs', 'install'], check=True)

    @patch('subprocess.Popen')
    @patch('societyai.helpers.CloneProgress')
    def test_clone_repository(self, mock_clone_progress, mock_popen):
        mock_process = MagicMock()
        mock_process.stdout = [b'Cloning...', b'Complete']
        mock_process.returncode = 0
        mock_popen.return_value = mock_process

        clone_repository('https://github.com/societyai/repo.git', '/tmp/repo')

        mock_popen.assert_called_once_with(
            ['git', 'clone', '--progress', 'https://github.com/societyai/repo.git', '/tmp/repo'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        mock_clone_progress.assert_called_once()

    @patch('subprocess.Popen')
    @patch('societyai.helpers.CloneProgress')
    def test_pull_latest_changes(self, mock_clone_progress, mock_popen):
        mock_process = MagicMock()
        mock_process.stdout = [b'Pulling...', b'Complete']
        mock_process.returncode = 0
        mock_popen.return_value = mock_process

        pull_latest_changes('/tmp/repo')

        mock_popen.assert_called_once_with(
            ['git', 'pull', 'origin', 'main'],
            cwd='/tmp/repo',
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        mock_clone_progress.assert_called_once()

    @patch('subprocess.Popen')
    @patch('societyai.helpers.CloneProgress')
    def test_fetch_lfs_objects(self, mock_clone_progress, mock_popen):
        mock_process = MagicMock()
        mock_process.stdout = [b'Fetching LFS...', b'Complete']
        mock_process.returncode = 0
        mock_popen.return_value = mock_process

        fetch_lfs_objects('/tmp/repo')

        mock_popen.assert_called_once_with(
            ['git', 'lfs', 'pull'],
            cwd='/tmp/repo',
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        mock_clone_progress.assert_called_once()

    @patch('societyai.helpers.check_git_installation')
    @patch('societyai.helpers.install_git_lfs')
    @patch('societyai.helpers.pull_latest_changes')
    @patch('societyai.helpers.clone_repository')
    @patch('societyai.helpers.fetch_lfs_objects')
    @patch('os.path.exists')
    def test_clone(self, mock_exists, mock_fetch_lfs, mock_clone_repo, mock_pull, mock_install_git_lfs, mock_check_git):
        mock_exists.return_value = False

        clone(repo_url='https://github.com/societyai/repo.git', output_dir='/tmp')

        mock_check_git.assert_called_once()
        mock_install_git_lfs.assert_called_once()
        mock_clone_repo.assert_called_once_with('https://github.com/societyai/repo.git', '/tmp/repo.git')
        mock_fetch_lfs.assert_called_once_with('/tmp/repo.git')
        mock_pull.assert_not_called()

if __name__ == '__main__':
    unittest.main()
