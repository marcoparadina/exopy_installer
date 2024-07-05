import os
import subprocess

# Read the repository URLs from the file
with open('repos.txt', 'r') as file:
    repos = file.readlines()

# Clone each repository
for repo in repos:
    repo = repo.strip()  # Remove any leading/trailing whitespace
    if repo:  # Skip any blank lines
        print(f"Cloning {repo} into the current directory")
        subprocess.run(["git", "clone", repo])
