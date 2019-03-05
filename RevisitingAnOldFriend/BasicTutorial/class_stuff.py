# some new python stuff xd


class A:
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return print("My value is " + str(self.value))

	@property
	def who(self):
		print("HELLO I AM RETURNING A VALUE")
		return print(str(self.value))

	@who.setter
	def who(self, value):
		self.value = value

	@who.deleter
	def who(self):
		del self.value


class B:
	def __init__(self, value=15):
		self.value = value

	def __str__(self):
		return str(self.value)

	@classmethod
	def create_element(cls, value):
		return cls(value + 25)


def main():
	a1 = A(5)
	a1.who
	a1.who = 35
	a1.who
	del a1

	b1 = B()
	b2 = B.create_element(25)
	print(b1, b2)


if __name__ == '__main__':
	main()




