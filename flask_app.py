import logging
import subprocess
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Het weer van vandaag: zonnig</h1>"

def _run_command(bash_command: str) -> str:
    """
    Voert een bash-commando uit en retourneert de uitvoer als string.
    """
    logging.info(f"Running command: {bash_command}")
    
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    
    if process.returncode != 0:
        logging.error(f"Error running command: {error.decode().strip()}")
        raise ValueError(error.decode().strip())
    
    return output.decode().strip()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)
