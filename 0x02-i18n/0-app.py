#!/usr/bin/env python3
""" Flask app """
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns a template"""
    return render_template('0-index.html')
