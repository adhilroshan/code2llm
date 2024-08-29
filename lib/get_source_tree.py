import fnmatch
import os


def get_source_tree(base_dir, exclude_patterns):
    tree_lines = []

    def should_exclude(file_path):
        for pattern in exclude_patterns:
            if fnmatch.fnmatch(file_path, pattern) or fnmatch.fnmatch(os.path.basename(file_path), pattern):
                return True
        return False

    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if not should_exclude(os.path.join(root, d))]
        level = root.replace(base_dir, '').count(os.sep)
        indent = ' ' * 4 * (level)
        tree_lines.append(f"{indent}{os.path.basename(root)}/")
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            if not should_exclude(os.path.join(root, f)):
                tree_lines.append(f"{sub_indent}{f}")

    return "\n".join(tree_lines)
