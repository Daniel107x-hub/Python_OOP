import copy

a = ([1, 2, 3, 4], "Hello", 5)

# Shallow copy
b = a[:]
c = copy.copy(a)
print("Shallow copies: ")
print(f"ID a: {id(a)}, ID b: {id(b)}, ID c: {id(c)}")
print(f"ID list in a: {id(a[0])}, ID list in b: {id(b[0])}, ID list in c: {id(c[0])}")

# Deep copy
b = copy.deepcopy(a)
print("\nDeep copy")
print(f"ID a: {id(a)}, ID b: {id(b)}")
print(f"ID list in a: {id(a[0])}, ID list in b: {id(b[0])}")

