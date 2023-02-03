# Special thanks to OpenAI and ChatGPT for making this so easy to make. LOL.

import requests
import json

def get_repo_size(repo_owner, repo_name):
    # Make a request to the GitHub API to retrieve the repository information
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
    headers = {'Accept': 'application/vnd.github+json'}
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data from the response
        repo_data = response.json()

        # Retrieve the repository size from the data
        repo_size = repo_data["size"]

        # Return the repository size in MB
        return repo_size / 1024
    else:
        # Raise an error with a descriptive message if the request was not successful
        raise ValueError(f"Failed to retrieve repository information: {response.status_code} {response.reason}")

# Example usage
repo_owner = "LiberlandHacker"
repo_name = "OSSP-CS"

try:
    repo_size = get_repo_size(repo_owner, repo_name)
except ValueError as error:
    print(error)
else:
    print(f"The repository {repo_owner}/{repo_name} is {repo_size:.2f} MB in size.")
