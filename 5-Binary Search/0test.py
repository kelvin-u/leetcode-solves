def build_decode_map():
    plain = "ARCHIVETERMINALUSERMANUAL"
    cipher = "HOWAURDTDONUXHGLQDONHXLHG"

    # Create mapping dictionaries for uppercase and lowercase
    decode_upper = {}
    decode_lower = {}

    for p_char, c_char in zip(plain, cipher):
        decode_upper[c_char] = p_char
        decode_lower[c_char.lower()] = p_char.lower()

    return decode_upper, decode_lower


def decode(text, decode_upper, decode_lower):
    result = []
    for ch in text:
        if ch.isupper() and ch in decode_upper:
            result.append(decode_upper[ch])
        elif ch.islower() and ch in decode_lower:
            result.append(decode_lower[ch])
        else:
            # Leave unchanged (spaces, digits, punctuation, unknown letters)
            result.append(ch)
    return "".join(result)


if __name__ == "__main__":
    decode_upper, decode_lower = build_decode_map()
    user_input = input("Enter encoded text to decode: ")
    decoded = decode(user_input, decode_upper, decode_lower)
    print("Decoded text:")
    print(decoded)
