import fnmatch
import mimetypes
import os
from code2llm.lib.get_source_tree import get_source_tree
from code2llm.lib.split_in_to_chunks import split_into_chunks

def extract_files_for_llm(base_dir, exclude_patterns, max_chars=3000):
    output = []

    # Step 1: Chain-of-Thought - Clear initial instructions
    output.append("### IMPORTANT: LLM Interaction Instructions ###\n")
    output.append(
        "1. **Please DO NOT respond, analyze, or provide any feedback until you receive the final signal: '## END_OF_INPUT ##'.**\n"
        "2. **Multiple files or parts of files will be provided.**\n"
        "3. **Acknowledge this instruction by waiting until the final signal before responding.**\n\n"
    )

    # Step 2: Include the source tree structure
    source_tree = get_source_tree(base_dir, exclude_patterns)
    output.append("### Source Tree\n")
    output.append(f"{source_tree}\n\n")

    # Step 3: Initial instruction for LLM input preparation
    output.append("### LLM Input Preparation\n")
    output.append(
        "The following sections contain code snippets extracted from the codebase. "
        "Each snippet is labeled with its file name and part number if split. "
        "**Reminder: Please wait until you receive the signal '## END_OF_INPUT ##' before starting your analysis or response.**\n\n"
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
                        
                        # Step 4: Tree-of-Thought & Self-Refine - Reminder in each chunk
                        output.append("### Reminder: Do not respond until you receive '## END_OF_INPUT ##'.\n")
                        output.append("### Verify that this is not the final input. If it is not, continue waiting.\n")
                        output.append(chunk)
                        output.append("\n\n")
            except Exception as e:
                # Log errors separately instead of including them in LLM input
                print(f"Error reading {file_path}: {e}")

    # Step 5: Final instruction - Signal to start processing
    output.append("\n### ## END_OF_INPUT ##. You may now begin your analysis or response.\n")

    return ''.join(output)
