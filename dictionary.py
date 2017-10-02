#辞書型

sales = {"tomoya": 20, "izu": 20}

print(sales)
print(sales["tomoya"])
sales["tomoya"] = 19
print(sales)
sales["yuki"] = 20
print(sales)
sales["yyy"] = 21
print(sales)
del(sales["yyy"])
print(sales)


for key, value in sales.items():
	print("{0}は: {1}歳です".format(key, value))
