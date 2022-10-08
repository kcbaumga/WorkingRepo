from flask import Flask
app = Flask(__name__)
#mkdir flask_app && cd flask_app
#source venv/bin/activate
#export FLASK_APP=hello.py
#flask run
#deactivate
@app.route('/')
def hello_world():
    return 'Hello World!'
