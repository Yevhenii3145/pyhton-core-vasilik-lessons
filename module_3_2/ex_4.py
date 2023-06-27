def codes_for_str(data: str) -> dict:
    result = {}
    for char in data:
        if char not in result:
            result[char] = ord(char)
    return result  # {'P': 80, 'y': 121, 't': 116,....}


print(codes_for_str("Python is the best language"))
