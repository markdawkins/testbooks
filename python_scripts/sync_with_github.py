import os
from github import Github

# Replace with your own access token and repository information
access_token = 'YOUR_ACCESS_TOKEN'
repository_name = 'markdawkins/testbooks'
file_path = '/inventory/1000'

# Authenticate with GitHub using access token
g = Github(access_token)

# Get the repository object
repo = g.get_user().get_repo(repository_name)

# Read the contents of the file
with open(file_path, 'r') as file:
    file_contents = file.read()

# Get the contents of the file in the repository
try:
    contents = repo.get_contents(file_path)
    sha = contents.sha
except Exception as e:
    sha = None

# If the file exists, update its contents
if sha:
    repo.update_file(
        file_path,
        'Updating file',
        file_contents,
        sha
    )
else:
    # If the file does not exist, create a new file
    repo.create_file(
        file_path,
        'Creating file',
        file_contents
    )

print(f'Successfully synced {file_path} with GitHub.')
