from flask import Flask, request, jsonify, render_template
from summarization_model import summarize

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # This will load templates/index.html

@app.route("/summarize", methods=["POST"])
def summarize_text():
    # Get the input text from the request
    data = request.json
    text = data.get("text", "")
    
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    # Summarize the text
    summary = summarize(text)
    
    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True)
