import os
from datetime import datetime, timezone


def run_job(text_input: str, multiplier: int, data_dir: str) -> dict:
    clean_text = text_input.strip()
    transformed = clean_text.upper()

    os.makedirs(data_dir, exist_ok=True)
    filename = f"output_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.txt"
    out_path = os.path.join(data_dir, filename)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(transformed + "\n")

    return {
        "line_count": multiplier,
        "preview": transformed,
        "saved_file": filename,
    }