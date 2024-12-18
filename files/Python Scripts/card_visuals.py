card_art_dict = {
    #dictionary with unicode for every card in deck
    "Ah": "\U0001F0B1",
    "2h": "\U0001F0B2",
    "3h": "\U0001F0B3",
    "4h": "\U0001F0B4",
    "5h": "\U0001F0B5",
    "6h": "\U0001F0B6",
    "7h": "\U0001F0B7",
    "8h": "\U0001F0B8",
    "9h": "\U0001F0B9",
    "10h": "\U0001F0BA",
    "Jh": "\U0001F0BB",
    "Qh": "\U0001F0BD",
    "Kh": "\U0001F0BE",
    "Ad": "\U0001F0C1",
    "2d": "\U0001F0C2",
    "3d": "\U0001F0C3",
    "4d": "\U0001F0C4",
    "5d": "\U0001F0C5",
    "6d": "\U0001F0C6",
    "7d": "\U0001F0C7",
    "8d": "\U0001F0C8",
    "9d": "\U0001F0C9",
    "10d": "\U0001F0CA",
    "Jd":  "\U0001F0CB",
    "Qd": "\U0001F0CD",
    "Kd": "\U0001F0CE",
    "As": "\U0001F0A1",
    "2s": "\U0001F0A2",
    "3s": "\U0001F0A3",
    "4s": "\U0001F0A4",
    "5s": "\U0001F0A5",
    "6s": "\U0001F0A6",
    "7s": "\U0001F0A7",
    "8s": "\U0001F0A8",
    "9s": "\U0001F0A9",
    "10s": "\U0001F0AA",
    "Js": "\U0001F0AB",
    "Qs": "\U0001F0AD",
    "Ks": "\U0001F0AE",
    "Ac": "\U0001F0D1",
    "2c": "\U0001F0D2",
    "3c": "\U0001F0D3",
    "4c": "\U0001F0D4",
    "5c": "\U0001F0D5",
    "6c": "\U0001F0D6",
    "7c": "\U0001F0D7",
    "8c": "\U0001F0D8",
    "9c": "\U0001F0D9",
    "10c": "\U0001F0DA",
    "Jc": "\U0001F0DB",
    "Qc": "\U0001F0DD",
    "Kc": "\U0001F0DE"
}

def card_to_art(hand: list) -> str:
    """
    Turns input hand into hand with visuals

    Arg:
        hand (list): list of strings representing cards
    
    Returns:
             (str): strings with unicode for visuals
    
    Example:
    >>>card_to_art(["Ah"])
       🂱
    """

    #final string containing unicode for cards
    return_str = ""

    #calls on dictionary to add unicode to return_string
    for i in hand:
        return_str += card_art_dict[i]
        
    return return_str 
