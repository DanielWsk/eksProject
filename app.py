# flask_web/app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, this docker container just got updated with CircleCi!'

def Add(a, b):
        return a + b

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
