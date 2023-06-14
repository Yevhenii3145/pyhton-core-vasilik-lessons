# сортировка
t = [3, 1, 5.5, 4]
t.sort()  # мутирует оригинальный список
print(t)

a = [5, 0, 1, 40, 4]
new_a = sorted(a)
print(new_a)


d = ["a", "c", "d", "b"]
d.sort()  # нельзя сортировать элементы разных типов, например инт и строку
print(d)

a = [5, 1, 0, 40, 4]
a.sort()
print("vvv", a)
a.sort(reverse=True)
print(a)

print(max(a))
print(min(a))

c = ["v", "a", "b"]
# сравнение по ascii кодам
print(max(c))
print(min(c))
