import yaml
# yaml - нужно устанавливать командой pip install pyyaml

users = [
    {'name': 'Bob', 'age': 22, 'gender': 'male'},
    {'name': 'Lucy', 'age': 22, 'gender': 'female'},
    {'name': 'Jack', 'age': 18, 'gender': 'male'}
]

serialize = yaml.dump(users)
print(serialize)
result = yaml.load(serialize, Loader=yaml.FullLoader)

with open("test.yaml", "w", encoding='utf-8') as f:
    yaml.dump({'users': users}, f, allow_unicode=True)
