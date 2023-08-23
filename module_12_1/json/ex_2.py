import json
with open("storage.json", "r") as f:
    store = json.load(f)  # store = obj

# {'tuple': [3, 4], 'list': [1, 3, 4], 'dict': {'a': 1}, 'bool': True, 'none': None}
print(store)
print(store.get("dict").get("a"))  # 1
