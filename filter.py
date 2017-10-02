#filter(関数, イテレータ)

def even(n):
	return n % 2 == 0

print(list(filter(even, range(10))))

print(list(filter(lambda n: n % 2 == 0, [0, 1, 2, 3, 4, 5])))
print(list(filter(lambda n: n % 2 == 0, range(10))))
