from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    """Return a simple greeting message."""
    return "Hello from Python!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
