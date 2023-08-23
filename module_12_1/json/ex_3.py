# Работа с кирилицей
import json

data = {
    'dev': {
        'name': 'Владимир',
        'position': 'программист'
    }
}

with open("data_user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

with open("data_user.json", "r", encoding="utf-8") as f:
    restore_data = json.load(f)
    # {'dev': {'name': 'Владимир', 'position': 'программист'}}
    print(restore_data)
