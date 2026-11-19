from flask import Flask, render_template, request
from worker import run_job

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        text_input = request.form.get("text_input", "")
        raw_mode = request.form.get("mode_flag", "0")
        mode_value = 1 if raw_mode == "1" else 0

        if not text_input.strip():
            error = "Please enter some text."
        else:
            result = run_job(text_input, mode_value)

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)