numbers = [4, 5, 6, 7, 4, 6, 9, 1, 2, 1, 2, 2]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)


numbers = [4, 5, 6, 7, 4, 6, 9, 1, 2, 1, 2, 2]
uniques = []
uniques = [number for number in numbers if number not in uniques]
print(uniques)




