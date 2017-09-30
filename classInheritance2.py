"""
Matusyma Tomoya
29/09/2017
"""

class User():
	count = 0
	def __init__(self,name):
		User.count += 1
		self.name = name
	def say_hi(self):
		print("hi {0}".format(self.name))

	@classmethod
	def show_info(cls):
		print("{0} instances".format(cls.count))

print(User.count)
tom = User("tom")
bob = User("bob")
print(User.count)
User.show_info()
