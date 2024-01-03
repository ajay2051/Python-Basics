some_list = ["1", "2", "5"]
print(some_list.pop(2))

sample_list = [['a'], ['b', ['c', 'd', ['e', [10]]]]]


def find_integers(nested_list):
    """Recursively finds and prints all integers within a nested list."""
    integers = []
    for item in nested_list:
        if isinstance(item, int):  # Check if the item is an integer
            integers.append(item)
        elif isinstance(item, list):  # If it's a list, recursively search it
            integers.extend(find_integers(item))
    return integers


# Call the function to find integers in the sample_list
result = find_integers(sample_list)
print(result)


# Index and Pop Problems
def f1(x):
    for i in x:
        x.pop()
        print(x)
        print(i, end="")


a = [0, 1, 2, 3, 4, 5, 6]
f1(a)


# Common leading prefix
def longest_common_prefix(strs):
    longest_pre = []
    if strs and len(strs) > 0:
        strs = sorted(strs)
        # e.g. before sort: ["flower","flow","flight","fake"]
        # after sort: ['fake', 'flight', 'flow', 'flower']
        first, last = strs[0], strs[-1]
        for i in range(len(first)):
            if len(last) > i and last[i] == first[i]:
                longest_pre.append(last[i])
            else:
                return "".join(longest_pre)
    return "".join(longest_pre)


result = longest_common_prefix(('flake', 'flight', 'flow', 'flower'))
print(result)
