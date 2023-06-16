'''
Метод: sub
'''

import re

string = "The JavaSript best JavaSript language is JavaSript"
a = string.replace("JavaSript", "Python")
print(a)

# sub(что меняем, на что, где, сколько раз)
replaced_str = re.sub(r"JavaSript", "Python", string, count=3)
print(replaced_str)
