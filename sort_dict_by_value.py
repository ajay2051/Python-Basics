a = {"a": 9, "b": 5, "c": 7}
result = dict(sorted(a.items(), key=lambda x: x[1]))
print(result)
