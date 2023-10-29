import json

from flask import Flask, render_template, request, jsonify
import os
from resume_parser import resumeparse

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/parse', methods=['POST'])
def parse_resume():
    if 'resume' not in request.files:
        return jsonify({'error': 'No file found'})

    resume_file = request.files['resume']
    if resume_file.filename == '':
        return jsonify({'error': 'No file selected/Uploaded.'})

    if resume_file:
        resume_file.save(os.path.join('static', resume_file.filename))
        file = os.path.join('static', resume_file.filename)
        data = resumeparse.read_file(file)
        os.remove(os.path.join('static', resume_file.filename))
        return json.dumps(data)


@app.route('/help')
def help_here():
    return render_template('help.html')


if __name__ == '__main__':
    app.run(debug=True)
