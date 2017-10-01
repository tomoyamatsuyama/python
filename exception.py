#例外処理
class MyExeption(Exception):
	pass


def div(a, b):
	try:
		if b < 0:
			raise MyExeption("not minus")
		print(a / b)
	except ZeroDivisionError:
		print("not by Zelo!")
	else:
		print("no exception")
	finally:
		print("----end-----")

div(10, 4)
