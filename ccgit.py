import sys
from cc_init import init_repo
from cc_add import add_file
import os

def main():
    print("Arguments received:", sys.argv)
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python3 ccgit.py init <repo_path>")
        print("  python3 ccgit.py add <repo_path> <file_name>")
        return

    command = sys.argv[1]

    if command == "init":
        repo_path = sys.argv[2]
        os.makedirs(repo_path, exist_ok=True)
        init_repo(repo_path)

    elif command == "add":
        if len(sys.argv) < 4:
            print("Usage: python3 ccgit.py add <repo_path> <file_name>")
            return
        repo_path = sys.argv[2]
        file_name = sys.argv[3]
        add_file(repo_path, file_name)

    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
