"""
Методы: split, replace
"""
phone = "+1-234-567-89-10"

# replace(old,new)

edited_phone = phone.replace("-", " ")
print(edited_phone)  # +1 234 567 89 10

edited_phone = phone.replace("-", "*", 2)  # заменит 2 элемнета
print(edited_phone)  # +1*234*567-89-10
