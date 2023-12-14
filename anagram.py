str_1 = input("Enter string 1  ")
str_2 = input("Enter string 2  ")

str_1 = str_1.lower()
str_2 = str_2.lower()

if len(str_1) == len(str_2):
    if ((sorted(str_1)) == (sorted(str_2))):
        print(f"{str_1} and {str_2} are anagrams")
    # print(f"{str_1} and {str_2} are not anagrams")
else:
    print(f"{str_1} and {str_2} are not anagrams")