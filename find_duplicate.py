n = [1, 2, 5, 8, 4, 2, 1, 4, 5, 6, 5]
duplicates = []
for value in n:
    if n.count(value) > 1 and value not in duplicates:
        duplicates.append(value)

print("Duplicate values:", duplicates)
