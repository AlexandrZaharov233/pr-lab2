from flask import Flask, request, jsonify

app = Flask(__name__)

data_store = {}


@app.route("/data", methods=["GET", "POST", "PUT", "DELETE"])
def data_handler():
    if request.method == "GET":
        return jsonify(data_store)

    if request.method == "POST":
        new_data = request.json
        data_store.update(new_data)
        return jsonify({"message": "Data added", "data": new_data})

    if request.method == "PUT":
        updated_data = request.json
        data_store.update(updated_data)
        return jsonify({"message": "Data updated", "data": updated_data})

    if request.method == "DELETE":
        key = request.args.get("key")
        if key in data_store:
            del data_store[key]
            return jsonify({"message": f"Data with key {key} deleted"})
        return jsonify({"error": "Key not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
