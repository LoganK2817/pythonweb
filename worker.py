import importlib
import covey
# import scorpion

def run_job(
    text_input: str,
    mode_value: int,
    scorpion_param: str = "",
    roz_factor: int = 0,
    hs_d: int = 0,
    char_len_in_hsd: bool = False,
    cc: int = 0,
) -> dict:
    importlib.reload(covey)
    # importlib.reload(scorpion)
    clean_text = text_input.strip()

    

    if mode_value == 1:
        # transformed, string_id = scorpion.main(clean_text)
        transformed, string_id = ("SCORPION", "192.168.17.170")
        preview = f"SCORPION OUTPUT >{transformed}< | PARAM: {scorpion_param}"
        formatted_id = f"ID: {string_id} | mode: 1 | param: {scorpion_param}"
    else:
        transformed, string_id = covey.main(clean_text,roz_factor,hs_d,char_len_in_hsd,cc)
        preview = (
            f"COVEY OUTPUT >{transformed}< | "
            f"RozFactor={roz_factor}, HsD={hs_d}, CharLenInHsD={char_len_in_hsd}, CC={cc}"
        )
        formatted_id = f"ID: {string_id} | mode: 0"

    return {
        "preview": preview,
        "stringID": formatted_id,
    }