# flask_web/app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
def hello_world():
    return 'Hey, we have Flask in a Docker container!'

if __name == '__main__':
    app.run(debug=True, host='0.0.0.0')