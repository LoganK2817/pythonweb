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
        scorpion_param = request.form.get("scorpion_param", "").strip() if mode_value == 1 else ""

        roz_factor = 0
        hs_d = 0
        cc = 0
        char_len_in_hsd = False

        if not text_input.strip():
            error = "Please enter some text."
        elif mode_value == 1 and not scorpion_param:
            error = "Please enter a SCORPION value (e.g. 12.25.8.2)."
        elif mode_value == 0:
            try:
                roz_factor = int(request.form.get("roz_factor", "0"))
                hs_d = int(request.form.get("hs_d", "0"))
                cc = int(request.form.get("cc", "0"))
                char_len_in_hsd = request.form.get("char_len_in_hsd") == "1"
            except ValueError:
                error = "RozFactor, HsD, and CC must all be valid integers."

        if not error:
            result = run_job(
                text_input=text_input,
                mode_value=mode_value,
                scorpion_param=scorpion_param,
                roz_factor=roz_factor,
                hs_d=hs_d,
                char_len_in_hsd=char_len_in_hsd,
                cc=cc,
            )

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)