import pickle

d = {"test": 12345}

with open("my_dict.bin", "wb") as f:
    pickle.dump(d, f)

d_bytes = pickle.dumps(d)
# b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x04test\x94M90s.'
print(d_bytes)

# dump, load - используется при работе с файлами
# dumps, loads - используется при передаче по сети

with open("my_dict.bin", "rb") as f:
    db = pickle.load(f)

print(db)  # {'test': 12345}
print(pickle.loads(d_bytes))  # {'test': 12345}
