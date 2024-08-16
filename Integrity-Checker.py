import hashlib

def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

file_to_check = "important_file.txt"
known_hash = "5d41402abc4b2a76b9719d911017c592"

file_hash = calculate_hash(file_to_check)
if file_hash == known_hash:
    print("File is intact.")
else:
    print("File has been altered!")
