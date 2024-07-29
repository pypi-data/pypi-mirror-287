import os
import stat
import subprocess

def create_post_checkout_hook(repo_path):
    post_checkout_hook = """#!/bin/bash
    # post-checkout hook to update requirements.txt

    # Find all directories in the current git repo
    for dir in $(find . -type d); do
      # Check if the directory contains requirements.txt and a virtual environment
      if [[ -f "$dir/requirements.txt" ]] && ([[ -f "$dir/venv/bin/activate" ]] || [[ -f "$dir/venv/Scripts/activate" ]]); then
        # Activate virtual environment
        if [[ -f "$dir/venv/bin/activate" ]]; then
          source "$dir/venv/bin/activate"
        elif [[ -f "$dir/venv/Scripts/activate" ]]; then
          source "$dir/venv/Scripts/activate"
        fi
        
        # Update requirements.txt
        pip freeze > "$dir/requirements.txt"

        # Add updated requirements.txt to the commit
        git add "$dir/requirements.txt"
      fi
    done
    """

    hook_path = os.path.join(repo_path, '.git', 'hooks', 'post-checkout')
    with open(hook_path, 'w') as file:
        file.write(post_checkout_hook)
    os.chmod(hook_path, 0o755)
    print("post-checkout hook created and made executable.")

def create_pre_commit_hook(repo_path):
    pre_commit_hook = """#!/bin/bash
    # pre-commit hook to check for large files

    max_size=100000000 # 100MB in bytes

    # Iterate over files staged for commit
    for file in $(git diff --cached --name-only); do
      if [ -f "$file" ] && [ $(stat -c%s "$file") -gt $max_size ]; then
        echo "$file is larger than 100MB, removing from commit"
        git reset HEAD "$file"
      fi
    done
    """

    hook_path = os.path.join(repo_path, '.git', 'hooks', 'pre-commit')
    with open(hook_path, 'w') as file:
        file.write(pre_commit_hook)
    os.chmod(hook_path, 0o755)
    print("pre-commit hook created and made executable.")

def create_post_merge_hook(repo_path):
    hook_content = '''#!/bin/bash
    # post-merge hook to update virtual environment if requirements.txt has changed

    python3 <<'EOF'
    import os
    import subprocess
    import filecmp

    def update_venv_if_requirements_changed():
        """Update virtual environment if requirements.txt has changed."""
        requirements_path = 'requirements.txt'
        old_requirements_path = 'old_requirements.txt'

        # Check if requirements.txt exists
        if os.path.exists(requirements_path):
            # Copy current requirements.txt to a temporary file
            if os.path.exists(old_requirements_path):
                os.remove(old_requirements_path)
            os.rename(requirements_path, old_requirements_path)

            # Run git command to check out the previous version of requirements.txt
            subprocess.run(['git', 'checkout', 'HEAD~1', '--', requirements_path])

            # Compare the files
            if not filecmp.cmp(requirements_path, old_requirements_path, shallow=False):
                # If they differ, update the virtual environment
                pip_executable = 'venv/bin/pip' if os.name != 'nt' else 'venv/Scripts/pip'
                try:
                    subprocess.run([pip_executable, 'install', '-r', requirements_path], check=True)
                    print("Virtual environment updated with new dependencies.")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to update virtual environment: {e}")

            # Restore the current version of requirements.txt
            os.rename(old_requirements_path, requirements_path)

    if __name__ == "__main__":
        update_venv_if_requirements_changed()
    EOF
    '''

    hook_path = os.path.join(repo_path, '.git', 'hooks', 'post-merge')
    with open(hook_path, 'w') as hook_file:
        hook_file.write(hook_content)
    st = os.stat(hook_path)
    os.chmod(hook_path, st.st_mode | stat.S_IEXEC)
    print("post-merge hook created and made executable.")