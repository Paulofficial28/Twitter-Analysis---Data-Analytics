import numpy as np
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/story')
def story():
    return render_template("story.html")

@app.route('/report')
def report():
    return render_template("report.html")

if __name__ == '__main__':
    app.run(debug=True)
