'''
Метод: sub
Дано рядок символів.
Виключити з цього рядка групи символів між дужками [, ].
Самі дужки теж мають бути виключені.
'''

import re
string = "Виключити із цієї [групи] символів, [розташовані між] дужками [, ]."

replaced_str = re.sub(r"\[.*?\]", "", string)
replaced_str = re.sub(r"  ", " ", replaced_str)
replaced_str = re.sub(r" \.", ".", replaced_str)
print(replaced_str)
