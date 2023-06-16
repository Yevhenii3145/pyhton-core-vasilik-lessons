"""
Методы: split, replace
----
Парим query запрос для гугл.Тут классичесский разделитель & и преобразуем на ловарь данными
"""
url_search = "https://www.google.com/search?rlz=1C1GCEA_enUA1012UA1012&sxsrf=APwXEdf7o1uuDkgXz_LlC461MG7pIHvZ9A:1686895004269&q=cat+and+dogs&tbm=isch&sa=X&ved=2ahUKEwiLvYLMjcf_AhUMgP0HHfVDC2QQ0pQJegQICxAB&biw=2133&bih=1032&dpr=0.9"

_, query = url_search.split("?")
print(query)

obj_query = {}

for el in query.split("&"):
    key, value = el.split("=")
    obj_query.update({key: value.replace("+", " ")})
print(obj_query)
