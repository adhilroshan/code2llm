import os
import logging
from flask import Flask, render_template, jsonify
import click
import waitress

from lib.commandline_response import commandline_response
from lib.extract_files_for_llm import extract_files_for_llm
from lib.read_exclude_patterns import read_exclude_patterns

app = Flask(__name__)

extracted_content = ""
EXCLUDE_FILE_NAME = ".llm_ignore"

def page_not_found(e):
    return render_template('404.html'), 404

def internal_server_error(e):
    return render_template('500.html'), 500


def suppress_flask_logs():
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/content')
def content():
    return jsonify({'content': extracted_content})

@click.command()
@click.option('--directory', '-d', type=str, default=os.getcwd(), help='Base directory to scan.')
@click.option('--max-chars', '-m', type=int, default=3000, help='Maximum number of characters per chunk.')
@click.option('--port', '-p', type=int, default=2277, help='Port number for the Flask app.')
def start(directory, max_chars, port):
    """Start the Code2LLM server.

    Launches the server to process the codebase.
    """
    exclude_file_path = os.path.join(directory, EXCLUDE_FILE_NAME)

    # Ensure the exclude file exists
    if not os.path.exists(exclude_file_path):
        raise FileNotFoundError(f"{exclude_file_path} not found. Please run 'code2llm init' first.")

    # Your existing extraction logic here
    exclude_patterns = read_exclude_patterns(exclude_file_path)
    
    global extracted_content
    extracted_content = extract_files_for_llm(directory, exclude_patterns, max_chars)

    suppress_flask_logs()

    commandline_response()

    # Use Waitress to serve the Flask app quietly
    waitress.serve(app, host='0.0.0.0', port=port, _quiet=True)

