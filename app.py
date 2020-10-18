import os
import pickle
from flask import Flask
import numpy as np
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

app = Flask(__name__)



# @app.route('/upload')
# def upload():
#   return 'yes'

@app.route('/', methods=['GET', 'POST'])
def hello():
    #return render_template("getInput.html")
    return render_template("cyberDetect.html")


if __name__ == '__main__':
    app.run(debug=True)
