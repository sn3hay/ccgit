import hashlib
import os

def hash_file(filepath):
    with open(filepath, 'rb') as f:
        content = f.read()
    return hashlib.sha1(content).hexdigest(), content

def store_object(repo_path, file_path):
    sha1_hash, content = hash_file(file_path)
    object_dir = os.path.join(repo_path, '.git', 'objects', sha1_hash[:2])
    object_file = os.path.join(object_dir, sha1_hash[2:])

    os.makedirs(object_dir, exist_ok=True)

    with open(object_file, 'wb') as f:
        f.write(content)

    return sha1_hash
