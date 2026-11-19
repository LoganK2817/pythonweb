import importlib
import covey
import scorpion

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
    importlib.reload(scorpion)
    clean_text = text_input.strip()

    

    if mode_value == 1:
        transformed = scorpion.main(clean_text,scorpion_param)

        stringInfo = scorpion_param.split(".")
        
        preview = f">{transformed}<"
        formatted_id = f"Decode= {stringInfo[0]}, RozFactor= {stringInfo[1]}, HsD= {stringInfo[2]}, CensorChar= {stringInfo[3]}"
    else:
        transformed, string_id = covey.main(clean_text,roz_factor,hs_d,char_len_in_hsd,cc)
        preview = (
            f">{transformed}< "
        )
        formatted_id = f"ID: {string_id}"

    return {
        "preview": preview,
        "stringID": formatted_id,
    }