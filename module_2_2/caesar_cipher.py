message = input("Введите сообщение: ")
offset = int(input("Введите смещение: "))
encoded_message = ""
for char in message:
    if "a" <= char <= "z":
        pos = ord(char) - ord("a")
        pos = (pos + offset) % 26
        new_char = chr(pos + ord("a"))
        encoded_message = encoded_message + new_char
    elif "A" <= char <= "Z":
        pos = ord(char) - ord("A")
        pos = (pos + offset) % 26
        new_char = chr(pos + ord("A"))
        encoded_message = encoded_message + new_char
    else:
        encoded_message += char
print(encoded_message)
