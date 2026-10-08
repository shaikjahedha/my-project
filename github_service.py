import os
from urllib.parse import quote

import requests
from dotenv import load_dotenv

load_dotenv()


class GitHubAPIError(RuntimeError):
    """Raised when GitHub cannot provide commits for the requested repository."""


def get_commits(owner, repo, branch="main"):
    """
    Get commits from a GitHub repository.
    """
    owner = owner.strip()
    repo = repo.strip()
    branch = branch.strip()

    if not owner or not repo or not branch:
        raise ValueError("GitHub owner, repository, and branch are required.")

    url = (
        "https://api.github.com/repos/"
        f"{quote(owner, safe='')}/{quote(repo, safe='')}/commits"
    )

    params = {
        "sha": branch,
        "per_page": 30
    }

    headers = {
        "Accept": "application/vnd.github+json"
    }

    # Optional GitHub token
    token = "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"

    if token:
        headers["Authorization"] = f"Bearer {token}"

    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=30
    )

    if response.status_code == 404:
        raise GitHubAPIError(
            f"GitHub could not find the repository '{owner}/{repo}'. "
            "Check the owner and repository spelling. If the repository is "
            "private, add a valid GITHUB_TOKEN with access to it in your .env "
            "file. Also verify that the selected branch exists."
        )

    if response.status_code == 401:
        raise GitHubAPIError(
            "GitHub rejected the authentication token. Check GITHUB_TOKEN "
            "in your .env file, or remove it when accessing a public repository."
        )

    if response.status_code == 403:
        raise GitHubAPIError(
            "GitHub denied this request. Check the token's repository access "
            "and permissions, or wait if the unauthenticated API rate limit "
            "has been exceeded."
        )

    if not response.ok:
        raise GitHubAPIError(
            f"GitHub API request failed with status {response.status_code}. "
            "Check the repository details and try again."
        )

    data = response.json()

    if not isinstance(data, list):
        raise GitHubAPIError(
            "GitHub returned an unexpected response while listing commits."
        )

    commits = []

    for item in data:
        commit_info = item["commit"]
        author = commit_info.get("author") or {}

        commits.append({
            "message": commit_info["message"].split("\n")[0],
            "author": author.get("name") or "Unknown author",
            "date": author.get("date") or "",
            "sha": item["sha"]
        })

    return commits