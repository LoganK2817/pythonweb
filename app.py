import os
from flask import Flask, render_template, request
from worker import run_job

app = Flask(__name__)
DATA_DIR = os.environ.get("DATA_DIR", "/data")


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        text_input = request.form.get("text_input", "")
        raw_mult = request.form.get("multiplier", "1")

        try:
            multiplier = int(raw_mult)
            if not text_input.strip():
                error = "Please enter some text."
            elif multiplier < 1 or multiplier > 100:
                error = "Repeat count must be between 1 and 100."
            else:
                result = run_job(text_input, multiplier, DATA_DIR)
        except ValueError:
            error = "Repeat count must be a valid integer."

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)