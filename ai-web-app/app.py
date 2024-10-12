from flask import Flask, request, jsonify, render_template # type: ignore
from summarization_model import summarize

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def summarize_text():
    data = request.json
    text = data.get("text", "")
    
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    summary = summarize(text)
    
    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True)
