from flask import Flask

app = Flask(__name__)

@app.route('/helloworld')
def get_hello_world():
    return {'message': 'Hello World!'}