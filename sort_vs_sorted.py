# Python sort()¶

# This function modifies the list in-place which means it modifies the original list and it has no return value. This
# method can be used only with lists as it is of the list class, it can not sort any other sequence like tuple,
# etc. This will sort the elements in ascending order by default.

# Without Any Parameters
colors = ["Black", "Purple", "Green", "Yellow", "Orange"]
colors.sort()
print("Sorted list:", colors)

# With the reverse argument
colors = ["Black", "Purple", "Green", "Yellow", "Orange"]
colors.sort(reverse=True)
print("Sorted list (in descending):", colors)

# Python sorted()¶ This function does not change the original list and returns a sorted list. This method can be used
# on any sequence like list, tuple, string, or any iterable that you want to be sorted. This will sort the elements
# in ascending order by default.

# With iterable argument
colors = ("Black", "Purple", "Green", "Yellow", "Orange")
print("Sorted list:", sorted(colors))
