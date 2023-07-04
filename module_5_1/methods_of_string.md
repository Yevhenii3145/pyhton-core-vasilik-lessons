# Звернення за індексом
S[i]
# Вилучення зрізу
S[i:j:step]
# Довжина рядка
len(S)
# Пошук підрядки у рядку. Повертає номер першого входження або -1
S.find(str, [start], [end])
# Пошук підрядки у рядку. Повертає номер останнього входження або -1
S.rfind(str, [start],[end])
# Пошук підрядки у рядку. Повертає номер першого входження або викликає ValueError
S.index(str, [start], [end])
# Пошук підрядки у рядку. Повертає номер останнього входження або викликає ValueError
S.rindex(str, [start],[end])
# Чи складається рядок з букв
S.isalpha()
# Чи складається рядок з цифр або літер
S.isalnum()
# Чи складається рядок із символів у нижньому регістрі
S.islower()
# Чи складається рядок із символів у верхньому регістрі
S.isupper()
# Чи складається рядок з символів, що не відображаються (пробіл, символ перекладу сторінки ('\f'), "новий рядок" ('\n'), "переклад каретки" ('\r'), "горизонтальна табуляція" ('\t ') та "вертикальна табуляція" ('\v'))
S.isspace()
# Чи починаються слова в рядку з великої літери
S.istitle()
# Перетворення рядка до верхнього регістру
S.upper()
# Перетворення рядка до нижнього регістру
S.lower()
# Чи починається рядок S з шаблону str
S.startswith(str)
# Чи закінчується рядок S шаблоном str
S.endswith(str)
# Перекладає перший символ рядка у верхній регістр, а всі інші в нижній
S.capitalize()
# Повертає кількість неперетинних входжень підрядки в діапазоні [початок, кінець] (0 і довжина рядка за замовчуванням)
S.count(str, [start], [end])
# Видалення пробілів на початку рядка
S.lstrip([chars])
# Видалення символів пробілу в кінці рядка
S.rstrip([chars])
# Видалення пробілових символів на початку та в кінці рядка
S.strip([chars])
# Перекладає символи нижнього регістру у верхній, а верхнього - у нижній
S.swapcase()
# Першу літеру кожного слова переводить у верхній регістр, а решта в нижній
S.title()