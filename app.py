import os
from flask import Flask

import parserUI

app = Flask(__name__)

@app.route('/')
def hello():
    return parserUI.getHTML()

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))