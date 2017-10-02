#map(関数, イテレータ)
#lambda 引数: 処理

def triple(n):
	return n * 3

print(list(map(triple, [1, 2, 3])))


print(list(map(lambda n: n * 3, [4, 5, 6])))
