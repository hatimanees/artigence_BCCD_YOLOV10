import subprocess

def clone_repo(repo_url, target_dir):
    """Clones the GitHub repository if not already present."""
    if not os.path.exists(target_dir):
        print(f"Cloning repository from {repo_url}...")
        subprocess.run(["git", "clone", repo_url], check=True)
    else:
        print(f"Repository already exists in {target_dir}.")
