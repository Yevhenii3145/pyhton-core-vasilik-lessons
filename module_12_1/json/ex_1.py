import json

d = {"a": 1}
l = [1, 3, 4]
t = (3, 4)
s = 'Hellof world'
b = True
st = {1, 2, "Test"}
none = None
obj = {'tuple': t, 'list': l, 'dict': d, 'bool': b, "none": None}
print(json.dumps(d))
print(json.dumps(l))
print(json.dumps(t))  # tuple станет списком
print(json.dumps(s))
print(json.dumps(b))  # True -> true
print(json.dumps(none))  # None -> null
# print(json.dumps(st))  # TypeError: Object of type set is not JSON serializable

with open("storage.json", "w") as f:
    json.dump(obj, f)
