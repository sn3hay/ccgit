import os
from utils import hash_file, store_object

def add_to_index(repo_path, file_path, object_hash):
    index_path = os.path.join(repo_path, '.git', 'index')
    with open(index_path, 'a') as index_file:
        index_file.write(f"{file_path} {object_hash}\n")

def add_file(repo_path, file_path):
    file_name_only = os.path.basename(file_path)  # Just the file name
    full_path = os.path.join(repo_path, file_name_only)

    if not os.path.exists(full_path):
        print(f"{file_name_only} doesn't exist in repo. Creating it.")
        with open(full_path, 'w') as f:
            f.write("")

    object_hash = store_object(repo_path, full_path)
    add_to_index(repo_path, file_name_only, object_hash)

    print(f"Added {file_name_only} to staging area with hash {object_hash}")
