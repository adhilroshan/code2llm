import os

EXCLUDE_FILE_NAME = ".llm_ignore"

def init_cmd(directory, additional_excludes=None):
    exclude_file_path = os.path.join(directory, EXCLUDE_FILE_NAME)

    # Default exclude patterns
    default_patterns = ['*.log', '__pycache__', '*.pyc', 'README.md', 'MANIFEST.in', 'LICENSE', '.gitignore',
    'venv', 'venv/*', '.git/*', '.git', '.idea', '.idea/*', 'node_modules', 'node_modules/*',
    'build', 'build/*', 'dist', 'dist/*', 'target', 'target/*', 'docker-compose.yml',
    'Dockerfile', 'docker-compose*.yaml', '.exclude_patterns', '.*', 'requirement.txt', '*.lock','*-lock.json',"*.pyc", "*.git", "__pycache__"]

    # If the exclude file doesn't exist, create it
    if not os.path.exists(exclude_file_path):
        with open(exclude_file_path, "w") as exclude_file:
            for pattern in default_patterns:
                exclude_file.write(pattern + "\n")

    # Add additional excludes if provided
    if additional_excludes:
        with open(exclude_file_path, "a") as exclude_file:
            for pattern in additional_excludes:
                exclude_file.write(pattern + "\n")

    print(f"Initialized exclusion patterns in {exclude_file_path}")

