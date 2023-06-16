"""
Методы: strip, removeprefix,replace,format
----
Провести валидацию списка телефонов
Телефон: +380501234567 Где: +380 код страны, а 501234567 телефон
Считаем, что телефон валидный с кодом и без кода
"""
phone_storage = ["38099124565", "0631245689", "380991234444", "611235489",
                 "000000000000", "4536464443", "374558594433443", "+38(050)123-45-65", "+38(099)123 45 65", "+38(099)123 bc", "380(66)1234567"]

codes_operators = {"067", "068", "096",
                   "095", "097", "099", "050", "063", "066"}


def is_valid_phone(phone):
    def is_valid_operator(phone) -> bool:
        if phone[:3] in codes_operators:
            return True
        return False

    if phone.isdigit():
        if len(phone) == 12:
            if phone[:2] == "38":
                return is_valid_operator(phone[2:])
        if len(phone) == 10:
            return is_valid_operator(phone)
    return False


def sanitize_phone(phone):
    new_phone = (phone.strip()
                 .removeprefix("+")
                 .replace("(", "")
                 .replace(")", "")
                 .replace(" ", "")
                 .replace("-", ""))
    return new_phone


if __name__ == "__main__":
    for phone in phone_storage:
        phone = sanitize_phone(phone)
        is_valid = is_valid_phone(phone)
        if is_valid:
            print("phone {:>12} is valid".format(phone))
        else:
            print("phone {:>12} is invalid".format(phone))
