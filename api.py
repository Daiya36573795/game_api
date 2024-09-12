from flask import Flask, request, jsonify

app = Flask(__name__)

# サンプルデータ
data = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]

# GETリクエスト: 全データを取得
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(data)

# GETリクエスト: 特定のIDのデータを取得
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((item for item in data if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

# POSTリクエスト: 新しいデータを追加
@app.route("/items", methods=["POST"])
def add_item():
    new_item = request.get_json()
    data.append(new_item)
    return jsonify(new_item), 201
