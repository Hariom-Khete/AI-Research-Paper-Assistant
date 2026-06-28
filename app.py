from flask import Flask, render_template , request, redirect, url_for
from pdf.loader import read_pdf

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/summarizer")
def summarizer():
    return render_template("summarizer.html")

@app.route("/upload", methods=["POST"])
def upload():
    if 'paper' not in request.files:
        return "No file selected"

    file = request.files['paper']

    if file.filename == '':
        return "No file selected"

    if file:
        pages = read_pdf(file)
        full_text = ""
        for page in pages:
            full_text += page["text"] + "\n"

        lines = full_text.splitlines()
        start = 0
        for i, line in enumerate(lines):
            if "introduction" in line.lower():
                start = i
                break

        preview = "\n".join(lines[start:])[:1000]
        print(f"Preview: {preview}")

        return render_template("summarizer.html", preview=preview, filename=file.filename)


if __name__ == "__main__":
    app.run(debug=True)