"""
Matusyma Tomoya
30/09/2017
"""

class A():
	def say_a(self):
		print("A!")

class B():
	def say_b(self):
		print("B!")

class C(A, B):
	pass

c = C()

c.say_a()
c.say_b()
