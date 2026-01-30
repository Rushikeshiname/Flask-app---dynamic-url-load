from flask import Flask, jsonify, request

app = Flask(__name__)

# Initial data
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"},
    {"id": 3, "name": "Item 3", "description": "This is item 3"}
]

@app.route('/')
def home():
    return "Welcome to the Sample To-Do List Application"


# GET all items
@app.route('/items/', methods=['GET'])
def get_all_items():
    return jsonify(items)


# GET item by id
@app.route('/items/<int:item_id>/', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)


# POST create new item
@app.route('/items/', methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        return jsonify({"error": "Invalid input"}), 400

    new_item = {
        "id": items[-1]['id'] + 1 if items else 1,
        "name": request.json.get('name'),
        "description": request.json.get('description', "")
    }

    items.append(new_item)
    return jsonify(new_item), 201


# PUT update item
@app.route('/items/<int:item_id>/', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404

    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)


# DELETE remove item
@app.route('/items/<int:item_id>/', methods=['DELETE'])
def delete_item(item_id):
    global items
    item = next((item for item in items if item['id'] == item_id), None)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    items = [i for i in items if i['id'] != item_id]
    return jsonify({"message": "Item deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)
