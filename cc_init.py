import os

def init_repo(repo_path):
    git_dir = os.path.join(repo_path, '.git')

    if os.path.exists(git_dir):
        print(f"A Git repository already exists in {repo_path}")
        return

    dirs = ['objects', 'refs', 'hooks', 'info']
    for d in dirs:
        os.makedirs(os.path.join(git_dir, d), exist_ok=True)

    with open(os.path.join(git_dir, 'HEAD'), 'w') as f:
        f.write('ref: refs/heads/master\n')

    with open(os.path.join(git_dir, 'config'), 'w') as f:
        f.write('[core]\n\trepositoryformatversion = 0\n\tfilemode = true\n')

    with open(os.path.join(git_dir, 'description'), 'w') as f:
        f.write('Unnamed repository; edit this file to name it.\n')

    print(f"Initialized empty Git repository in {os.path.abspath(git_dir)}")
