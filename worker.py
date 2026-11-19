import os
from datetime import datetime, timezone
import covey

def run_job(text_input: str, multiplier: int) -> dict:
    clean_text = text_input.strip()
    (transformed, string_id) = covey.main(clean_text)
    transformed = f"COVEY OUTPUT >{transformed}<"
    string_id = f"ID: {string_id}"

    return {
        "preview": transformed,
        "stringID": string_id,
    }