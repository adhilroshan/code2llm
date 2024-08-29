import os


def read_exclude_patterns(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            patterns = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        return patterns
    else:
        return []
