class User():
	def __init__(self, name):
		self.name = name

	def say_hi(self):
		print("hi {0}".format(self.name))


class AdiminUser(User):
	def __init__(self, name, age):
		super().__init__(name)
		self.age = age

	def say_hello(self):
		print("helo {0} ({1})".format(self.name, self.age))

	def say_hi(self):
		print("[adimin] hi {0}".format(self.name))
