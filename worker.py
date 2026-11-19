import os
from datetime import datetime, timezone
import covey

def run_job(text_input: str, multiplier: int) -> dict:
    clean_text = text_input.strip()
    transformed = covey.main(clean_text)

    return {
        "line_count": multiplier,
        "preview": transformed,
    }