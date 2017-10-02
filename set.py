# セット

# a = set([1, 2, 4])
a = {1,3,5}

print(a)
print(0 in a)
a.add(2)
print(a)
a.add(0)
print(a)
a.remove(0)
print(a)
a.add(0)
print(0 in a)
print(len(a))

b = {1, 2, 3, 4, 5}

print(a | b) #{0, 1, 2, 3, 4, 5}
print(a & b) #{1, 2, 3, 5}
print(a - b) #{0}
