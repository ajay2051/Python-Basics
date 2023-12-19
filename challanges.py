word = "anajsxaushdjaxnjeuyqyeqoncndfh"
word_length = 5
for i in range(0, len(word), word_length):
    result = word[i:i + word_length]
    print(result)


def halt_string(str):
    """ This function returns half of string"""
    return str[:len(str) // 2]
    # To return second half of string str[len(str) // 2:]


result = halt_string("bhadgyaukjan")
print(result)


def capitals(word):
    """ This function returns the capital letter of given string """
    result = []
    for i in word:
        if i.isupper():
            result.append(i)
    return result


a = capitals("AbgfRnjYkjR")
print(a)


def return_capital(words):
    """ Same above function by using generators """
    x = [i for i in words if i.isupper()]
    yield x


print(next(return_capital("RbhTnjUdscR")))


def hello(str):
    str_length = len(str)
    mask = str_length - 4
    result = str[mask:]
    print("*" * mask + result)


hello("125478965321")

l = [[[[1]]]]
for a in l:
    for b in a:
        for c in b:
            for d in c:
                print(d)

email = "ajaythk.94@gmail.com"

a = email.split(".com")
result = a[0].split("@")
print(result[0])

emails = ["ajaythk.94@gmail.com", "andrew200@gmail.com"]
print([x.split("@")[0] for x in emails])

# Find Word Frequency
frequency = {}
sentence = input("Enter Word: ")

for word in sentence.split():
    frequency[word] = frequency.get(word,
                                    0) + 1  # 0 is default value if word is not found if word is found then add + 1
print(frequency)

# Find Letter Frequency
results = {}
x = input("Enter word ")
for i in x.split():
    results[i] = x.count(i)
print(results)
