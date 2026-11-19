
import importlib
import covey

def run_job(text_input: str, mode_value: int) -> dict:
    importlib.reload(covey)
    
    clean_text = text_input.strip()
    
    (transformed, string_id) = covey.main(clean_text)
    transformed = f"COVEY OUTPUT >{transformed}<"
    string_id = f"ID: {string_id} mode: {mode_value}"

    return {
        "preview": transformed,
        "stringID": string_id,
    }