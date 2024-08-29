# Code2LLM

**Code2LLM** is a tool for preparing codebases for analysis by language models (LLMs). It extracts code from a specified directory, chunks it into manageable sizes, and formats it for LLM input. This tool provides both a command-line interface (CLI) and a web interface to interact with the extracted code.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Command-Line Interface (CLI)](#command-line-interface-cli)
  - [Web Interface](#web-interface)
<!-- - [Files and Directories](#files-and-directories) -->
- [Contributing](#contributing)
  - [User Instructions](#user-instructions)
  - [Contributor Instructions](#contributor-instructions)
- [License](#license)
- [Contact](#contact)

## Features

- **Code Extraction:** Extracts and formats code from a directory.
- **Chunking:** Splits code into chunks of a specified size to fit LLM input constraints.
- **Web Interface:** View, copy, and interact with extracted code chunks.
- **CLI Support:** Initialize and run the extraction process from the command line.
- **Customizable Exclusions:** Define patterns to exclude files and directories from processing.

## Installation

You can install Code2LLM using `pipx`:

```bash
pipx install git+https://github.com/adhilroshan/code2llm.git
```

`pipx` is a tool for installing and running Python applications in isolated environments. It ensures that Code2LLM and its dependencies don't interfere with other Python projects on your system.

## Usage

### Command-Line Interface (CLI)

1. **Initialize Exclusion Patterns:**

   Initialize default exclusion patterns and add additional patterns if needed:

   ```bash
   code2llm init --additional-excludes '*.tmp' 'test_dir/'
   ```

2. **Start Extraction and Web Server:**

   Run the extraction process and start the Flask web server:

   ```bash
   code2llm --directory /path/to/your/code --max-chars 3000 --port 2277
   ```

   - `--directory`: Base directory to scan.
   - `--max-chars`: Maximum number of characters per chunk (default is 3000).
   - `--port`: Port number for the Flask app (default is 2277).

### Web Interface

After starting the web server, access the web interface at:

```
http://localhost:2277
```

Here you can view and interact with the extracted code chunks.

<!-- ## Files and Directories

- **`pyproject.toml`**: Project configuration and dependencies.
- **`app.py`**: Flask application and server logic.
- **`code2llm/`**: Package containing initialization and CLI logic.
- **`lib/`**: Library with utilities for code extraction and chunking.
- **`static/`**: Static files (JavaScript and CSS) for the web interface.
- **`templates/`**: HTML templates for the web interface.
- **`tests/`**: Unit tests for the project. -->

## Contributing

We welcome contributions to improve Code2LLM. Please follow the guidelines below:

### User Instructions

1. **Report Issues:** If you encounter any bugs or issues, please open an issue on the [GitHub Issues](https://github.com/adhilroshan/code2llm/issues) page.
2. **Feature Requests:** If you have suggestions for new features, feel free to open a feature request.
3. **Feedback:** For general feedback or questions, you can reach out via email or open a discussion in the [GitHub Discussions](https://github.com/adhilroshan/code2llm/discussions) section.

### Contributor Instructions

1. **Fork the Repository:** Fork the repository on GitHub and clone it to your local machine.
2. **Create a Branch:** Create a new branch for your changes:

   ```bash
   git checkout -b feature-branch
   ```

3. **Make Changes:** Implement your changes or fixes.
4. **Write Tests:** Ensure your changes are covered by tests.
5. **Commit Changes:** Commit your changes with a descriptive message:

   ```bash
   git add .
   git commit -m "Describe your changes"
   ```

6. **Push to GitHub:** Push your changes to your forked repository:

   ```bash
   git push origin feature-branch
   ```

7. **Create a Pull Request:** Open a pull request from your forked repository to the main repository, describing your changes and why they should be merged.

8. **Review Process:** Participate in the review process and make any necessary adjustments based on feedback.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please contact [Adhil Roshan](mailto:adhilroshann@gmail.com).

