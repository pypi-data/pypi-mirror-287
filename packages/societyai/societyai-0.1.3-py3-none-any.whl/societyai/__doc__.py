"""
societyai.helpers

This module provides a helper function to clone repositories with support for Git LFS, private repositories, and progress tracking.

Functions:
- clone(**kwargs): Clone a repository from a given URL, remote host, or repository name.

Usage Examples:
1. Clone a Public Repository by Full URL:
    from societyai.helpers import clone
    clone(repo_url="https://a.dev.societyai.com/owner/repo", output_dir="repo")

2. Clone a Private Repository by Full URL with Access Token:
    from societyai.helpers import clone
    clone(repo_url="https://a.dev.societyai.com/owner/repo", output_dir="repo", access_token="your_access_token")

3. Clone a Repository by Remote Host and Repository Name:
    from societyai.helpers import clone
    clone(remote_host="https://a.dev.societyai.com", repo_name="owner/repo", output_dir="repo")

4. Clone a Private Repository by Remote Host and Repository Name with Access Token:
    from societyai.helpers import clone
    clone(remote_host="https://a.dev.societyai.com", repo_name="owner/repo", output_dir="repo", access_token="your_access_token")

5. Clone a Repository by Remote Host Only (Default Repository Name):
    from societyai.helpers import clone
    clone(remote_host="https://a.dev.societyai.com", repo_name="owner/repo", output_dir="repo")

6. Clone a Private Repository by Remote Host Only with Access Token (Default Repository Name):
    from societyai.helpers import clone
    clone(remote_host="https://a.dev.societyai.com", repo_name="owner/repo", output_dir="repo", access_token="your_access_token")
"""
