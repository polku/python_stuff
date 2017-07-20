"""Quick and dirty "make a file downloadable" 
combine with ngrok http 5000 if no domain or public IP 
"""

import os
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory(os.path.dirname(os.path.realpath(__file__)), '<filename>')

if __name__ == '__main__':
    app.run() # port=xx if 5000 is already used
