import os
import logging
from flask import Flask, render_template, jsonify
import click
import waitress

from code2llm.lib.commandline_response import commandline_response
from code2llm.lib.extract_files_for_llm import extract_files_for_llm
from code2llm.lib.read_exclude_patterns import read_exclude_patterns
from code2llm.lib.find_available_port import find_available_port

app = Flask(__name__)

# extracted_content = ""
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
    return jsonify({'content': extracted_content,"max_chars": max_characters})
    # print("Extracted content", extracted_content)

@click.command()
@click.option('--directory', '-d', type=str, default=os.getcwd(), help='Base directory to scan.')
@click.option('--max-chars', '-m', type=int, default=128000, help='Maximum number of characters per chunk.')
def start(directory, max_chars):
    """Start the Code2LLM server.

    Launches the server to process the codebase.
    """
    exclude_file_path = os.path.join(directory, EXCLUDE_FILE_NAME)
    port = find_available_port()

    # Ensure the exclude file exists
    if not os.path.exists(exclude_file_path):
        click.echo(f"{EXCLUDE_FILE_NAME} not found in the directory. Please run 'code2llm init' before starting the server.")
        return
    
    # Your existing extraction logic here
    exclude_patterns = read_exclude_patterns(exclude_file_path)
    
    global max_characters
    max_characters = max_chars
    
    global extracted_content
    extracted_content = extract_files_for_llm(directory, exclude_patterns, max_chars)

    suppress_flask_logs()

    commandline_response(port=port)

    # Use Waitress to serve the Flask app quietly
    waitress.serve(app, host='0.0.0.0', port=port, _quiet=True)

