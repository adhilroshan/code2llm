import fnmatch
import mimetypes
import os
from code2llm.lib.get_source_tree import get_source_tree
from code2llm.lib.split_in_to_chunks import split_into_chunks

def extract_files_for_llm(base_dir, exclude_patterns, max_chars=3000):
    output = []

    # Add initial instructions for the LLM
    output.append("### IMPORTANT: LLM Interaction Instructions ###\n")
    output.append(
        "Please do not respond or analyze the content until you receive the final signal indicating all files have been entered. "
        "I will provide multiple files or parts of files below. Once you receive the final signal, you may begin your analysis.\n\n"
    )

    # Include the source tree structure
    source_tree = get_source_tree(base_dir, exclude_patterns)
    output.append("### Source Tree\n")
    output.append(f"{source_tree}\n\n")

    # Initial instruction for LLM input preparation
    output.append("### LLM Input Preparation\n")
    output.append(
        "The following sections contain code snippets extracted from the codebase. "
        "Each snippet is labeled with its file name and part number if split. "
        "Please wait until all snippets are provided before starting your analysis.\n\n"
    )

    def should_exclude(file_path):
        for pattern in exclude_patterns:
            if fnmatch.fnmatch(file_path, pattern) or fnmatch.fnmatch(os.path.basename(file_path), pattern):
                return True
        return False

    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if not should_exclude(os.path.join(root, d))]

        for file in files:
            file_path = os.path.join(root, file)

            if should_exclude(file_path):
                continue

            relative_path = os.path.relpath(file_path, base_dir)
            file_type, _ = mimetypes.guess_type(file_path)
            language = file_type.split('/')[-1] if file_type else 'unknown'

            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    file_content = f.read()
                    chunks = split_into_chunks(file_content, max_chars)
                    for i, chunk in enumerate(chunks):
                        output.append(f"--- File: {relative_path} - Part {i + 1} ---\n")
                        output.append(f"Language: {language}, Size: {os.path.getsize(file_path)} bytes\n")
                        output.append(chunk)
                        output.append("\n\n")
            except Exception as e:
                output.append(f"Error reading {file_path}: {e}\n")

    # Final instruction to let the LLM know that all files have been entered
    output.append("\n### All files entered. You may now begin your analysis or response.\n")

    return ''.join(output)
