# envsync

envsync is a Python package to manage coding environments and projects using Python virtual environments and Git hooks.

## Installation

You can install envsync from PyPI:

```
pip install envsync
```

## Usage


To initialize a local Git repository with the necessary hooks, run:

```

envsync /path/to/local_git_repo_folder
```

```

```

This command will set up the following hooks:

* `post-checkout`: Updates `requirements.txt` whenever you checkout a new branch or commit.
* `pre-commit`: Prevents committing files larger than 100MB.
* `post-merge`: Updates the virtual environment if `requirements.txt` changes after a merge.


## License 


This project is licensed under the MIT License.
