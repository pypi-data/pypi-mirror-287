import click
import os
from envsync.hooks import create_post_checkout_hook, create_pre_commit_hook, create_post_merge_hook

@click.command()
@click.argument('repo_path', type=click.Path(exists=True, file_okay=False, dir_okay=True))
def main(repo_path):
    """Initialize the Git repository at REPO_PATH with hooks to manage requirements.txt and venv."""
    if not os.path.exists(os.path.join(repo_path, '.git')):
        print(f"The directory {repo_path} is not a Git repository.")
        return

    create_post_checkout_hook(repo_path)
    create_pre_commit_hook(repo_path)
    create_post_merge_hook(repo_path)
    print("Git hooks have been set up successfully.")

if __name__ == "__main__":
    main()