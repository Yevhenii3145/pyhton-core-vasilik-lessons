"""
Метод: Translate
----
Перевод 16-ой системы исчисления в двоичную
"""

symbols = '0123456789ABCDEF'
code = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
        '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']


MAP = {}
for k, v in zip(symbols, code):
    MAP[ord(k)] = v
    # MAP[ord(k.lower())] = v
print(MAP)

result = "34 DF 55 CA aa".translate(MAP)
print(result)
# 00110100 11011111 01010101 11001010 aa
