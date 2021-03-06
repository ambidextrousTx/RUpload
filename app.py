import requests
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404


@app.route('/uploaded', methods=['POST'])
def uploaded_file():
    file_name = request.form['myfile']
    return requests.get('https://s3.amazonaws.com/RUpload/BaltimoreBoats.JPG').content


if __name__ == '__main__':
    app.run(debug=True)
