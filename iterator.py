#イテレーター


scores = [40, 50, 60, 80]

it = iter(scores)
print(next(it))
print(next(it))
print("hello")
print(next(it))

def get_infinite():
	i = 0
	while True:
		yield i * 2
		i += 1

g = get_infinite()

print(next(g))
print(next(g))
print(next(g))
