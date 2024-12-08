from flask import Flask, request, jsonify, Response
from AI_vision import askAboutMother

app = Flask(__name__)

@app.route('/askAboutMother', methods=['POST'])
def ask_about_model():
    try:
        data = request.get_json()
        # print(f"Received data: {data}")
    except Exception as e:
        # print(f"Error parsing JSON: {e}")
        return jsonify({"success": False, "message": str(e), "data": None}), 400

    if not data or not all(key in data for key in ['query']):
        return jsonify({"error": "Missing required fields"}), 400

    question = data['query']
    return askAboutMother(question)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
