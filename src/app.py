from flask import Flask, jsonify, request

app = Flask(__name__)


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": True }
]


@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body:", request_body)
    
    
    if not request_body or "label" not in request_body or "done" not in request_body:
        return jsonify({"error": "Invalid data format"}), 400  
    
    todos.append(request_body)
    
    return jsonify(todos), 200  

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Position out of range"}), 400
    
    todos.pop(position)
    print("This is the position to delete:", position)
    return jsonify(todos), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
