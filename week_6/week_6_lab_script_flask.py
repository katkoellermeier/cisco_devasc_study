# run this with
# "pip install flask"
# "python week_6_lab_script_flask.py"

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from your first Flask app!"

@app.route('/status')
def status():
    return {"status": "running", "message": "App is healthy."}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



# how to build a docker image
# "docker build -t my-flask-app ."