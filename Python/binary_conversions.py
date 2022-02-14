def dec_to_bin(number: int):
    try:
        return(bin(number[2:]))
    except Exception as err:
        return str(f"Problem occured: {err}")


def bin_to_dec(number:str):
    if 'b' in number:
        number = number[2:]
    try:
        return(int(number, 2))
    except Exception as err:
        return str(f"Problem occured: {err}")