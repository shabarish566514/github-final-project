from flask import Flask, jsonify, request

app = Flask(__name__)

accounts = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Jane"}
]

@app.route("/accounts", methods=["GET"])
def list_accounts():
    return jsonify(accounts)

@app.route("/accounts/<int:id>", methods=["GET"])
def read_account(id):
    for acc in accounts:
        if acc["id"] == id:
            return jsonify(acc)
    return jsonify({"error": "Not found"}), 404

@app.route("/accounts", methods=["POST"])
def create_account():
    data = request.json
    accounts.append(data)
    return jsonify(data), 201

@app.route("/accounts/<int:id>", methods=["PUT"])
def update_account(id):
    for acc in accounts:
        if acc["id"] == id:
            acc["name"] = request.json.get("name")
            return jsonify(acc)
    return jsonify({"error": "Not found"}), 404

@app.route("/accounts/<int:id>", methods=["DELETE"])
def delete_account(id):
    global accounts
    accounts = [a for a in accounts if a["id"] != id]
    return jsonify({"message": "Deleted"})
    
if __name__ == "__main__":
    app.run(debug=True)
