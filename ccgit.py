import os
import sys

def init_repo(repo_path):
    git_dir = os.path.join(repo_path, '.git')

    if os.path.exists(git_dir):
        print(f"A Git repository already exists in {repo_path}")
        return

    # directories
    dirs = [
        'objects',
        'refs',
        'hooks',
        'info'
    ]
    for d in dirs:
        os.makedirs(os.path.join(git_dir, d), exist_ok=True)

    # default files
    with open(os.path.join(git_dir, 'HEAD'), 'w') as f:
        f.write('ref: refs/heads/master\n')

    with open(os.path.join(git_dir, 'config'), 'w') as f:
        f.write('[core]\n\trepositoryformatversion = 0\n\tfilemode = true\n')

    with open(os.path.join(git_dir, 'description'), 'w') as f:
        f.write('Unnamed repository; edit this file to name it.\n')

    print(f"Initialized empty Git repository in {os.path.abspath(git_dir)}")


# This is a simple command-line interface for initializing a Git repository.
# It can be run with the command: python3 ccgit.py init <repo_path>
def main():
    if len(sys.argv) < 3 or sys.argv[1] != "init":
        print("Usage: python3 ccgit.py init <repo_path>")
        return

    repo_path = sys.argv[2]
    os.makedirs(repo_path, exist_ok=True)
    init_repo(repo_path)

if __name__ == "__main__":
    main()
