#baseN_to_int
def baseN_to_int(text, base_chars):
    base = len(base_chars)
    char_to_val = {c: i for i, c in enumerate(base_chars)}
    num = 0
    for c in text:
        if c not in char_to_val:
            raise ValueError(f"Invalid character '{c}' not in base chars.")
        num = num * base + char_to_val[c]
    return num
