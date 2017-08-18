from flask import Flask, jsonify
app = Flask(__name__)

print("__name__: ", __name__)

@app.route("/")
def hello():
    return "hello world!"

@app.route("/tasks")
def list_tasks():
    tasks = [{"name": "task1"}, {"name": "task2"}]
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
