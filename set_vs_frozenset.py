# Set A set is an unordered and unindexed collection of unique elements. Sets are mutable, you can change the
# elements using a built-in function like add(), remove(), etc. Since the elements are mutable and not in order,
# they don’t have hash values. So you can’t access the elements with the help of index numbers.

# Note: Sets can’t be used as a dictionary key or as elements of another set. They can be used as a dictionary value.

fruits = {"Apple", "Banana", "Cherry", "Apple", "Kiwi"}

print("Unique elements:", fruits)

# Add new fruit
fruits.add("Orange")
print("After adding new element:", fruits)

# Size of the set
print("Size of the set:", len(fruits))


# Python frozenset()¶

# A frozenset is an unordered and unindexed collection of unique elements. It is immutable and it is hashable. It is
# also called an immutable set. Since the elements are fixed, unlike sets you can't add or remove elements from the set.

# Frozensets are hashable, you can use the elements as a dictionary key or as an element from another set. Frozensets
# are represented by the built-in function which is frozenset(). It returns an empty set if there are no elements
# present in it. You can use frozenset() if you want to create an empty set.

fruits = {"Apple", "Banana", "Cherry", "Apple", "Kiwi"}
basket = frozenset(fruits)

print("Unique elements:", basket)

# Add new fruit throws an error!
basket.add("Orange")
print("After adding new element:", basket)
