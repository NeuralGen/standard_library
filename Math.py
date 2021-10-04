class List:
	import math

	def add(self, _list):
		result = 0
		
		added = []
		args = list(_list)

		currentLen = len(args[0])
		for _list in args:
			if len(_list) == currentLen:
				currentlen = len(_list)
			else: raise Exception("The length of the lists aren't same")

		for i in range(len(args[0])):
			added.append(args[0][i] + args[1][i])

		return added

	def subtract(self, _list):
		result = 0

		subtracted = []
		args = list(_list)

		currentLen = len(args[0])
		for _list in args:
			if len(_list) == currentLen:
				currentlen = len(_list)
			else: raise Exception("The length of the lists aren't same")

		for i in range(len(args[0])):
			subtracted.append(args[0][i] - args[1][i])

		return subtracted


	def multiply(self, _list):
		result = 1

		multiplied = []
		args = list(_list)

		currentLen = len(args[0])
		for _list in args:
			if len(_list) == currentLen:
				currentlen = len(_list)
			else: raise Exception("The length of the lists aren't same")

		for i in range(len(args[0])):
			multiplied.append(args[0][i] * args[1][i])

		return multiplied

	
	def divide(self, _list):
		result = 0

		divided = []
		args = list(_list)

		currentLen = len(args[0])
		for _list in args:
			if len(_list) == currentLen:
				currentlen = len(_list)
			else: raise Exception("The length of the lists aren't same")

		for i in range(len(args[0])):
			divided.append(args[0][i] / args[1][i])

		return divided


	def remainder(self, _list):
		result = 0

		divided = []
		args = list(_list)

		currentLen = len(args[0])
		for _list in args:
			if len(_list) == currentLen:
				currentlen = len(_list)
			else: raise Exception("The length of the lists aren't same")

		for i in range(len(args[0])):
			divided.append(args[0][i] % args[1][i])

		return divided


	def power(self, base, power=2):
		powered = []

		for i in base:
			powered.append(i ** power)

		return powered


	def root(self, base, root=2):
		import math
		rooted = []

		currentLen = len(base)
		for i in base:
			if round(math.pow(i, (1/root))) ** 3 == i:
				rooted.append(round(math.pow(i, (1/root))))
			else:
				rooted.append(math.pow(i, (1/root)))

		return rooted


	def mean(self, _list):
		mean_val = 0
		for i in _list:
			mean_val += i
		return mean_val/len(_list)


	def is_same(self, x, y):
		if not len(x) == len(y):
			raise Exception("The length of the lists are not same")
		else:
			return (x == y)

	
	def factorial(self, nums):
		result = []
		for i in nums:
			result.append(Number().factorial(i))

		return result



class Number:
	import math
	pi = 3.141592653589793238462633832795028841971
	e = 2.718281828459045235360287471352662497757


	def add(self, *args):
		result = 0

		if type(args[0]) is list:
			args = args[0]

		args = list(args)

		for n in args:
			result += n

		return result


	def subtract(self, *args):
		result = 0

		if type(args[0]) is list:
			args = args[0]

		args = list(args)

		for n in args:
			result -= n

		return result + args[0]*2


	def multiply(self, *args):
		result = 1

		if type(args[0]) is list:
			args = args[0]

		args = list(args)

		for n in args:
			result = result*n

		return result


	def divide(self, *args):
		result = 0

		if type(list(args)[0]) is list:
			args = list(args)[0]

		if len(list(args)) > 2:
			raise Exception("Can't divide more than two numbers")
		else:
			return list(args)[0] / list(args)[1]


	def remainder(self, *args):
		result = 0

		if type(list(args)[0]) is list:
			args = list(args)[0]

		if len(list(args)) > 2:
			raise Exception("Can't divide more than two numbers")
		else:
			return list(args)[0] % list(args)[1]


	def factorial(self, n):
		result = 1
		for i in range(1,n+1):
			result*=i

		return result


	def power(self, base, power):
		return base ** power


	def harmonic_mean(self, *args):
		_list = list(args)
		if len(_list) == 2:
			return (2*_list[0]*_list[1])/(_list[0]+_list[1])

		else: raise Exception("Can't calculate harmonic mean of more or less than 2 values")


	def is_odd(self, n):
		if n%2 == 0:
			return False
		else: return True


	def is_even(self, n):
		if n%2 == 0:
			return True
		else: return False


	def root(self, base, root=2):
		if round(self.power(base, (1/root))) ** 3 == base:
			return round(self.power(base, (1/root)))
		else:
			return self.power(base, (1/root))


	def log(self, n, base=10):
		return self.math.log(n, base)


	def In(self, n):
		return self.math.log(n, self.e)


	def sin(self, n):
		return self.math.sin(n)


	def cos(self, n):
		return self.math.cos(n)


	def tan(self, n):
		return self.math.tan(n)


	def sec(self, n):
		return (1 / self.math.cos(n))


	def cosec(self, n):
		return (1 / self.math.sin(n))


	def cot(self, n):
		return (self.math.cos(n) / self.math.sin(n))


	def to_degrees(self, rad):
		return (self.math.radians(rad))


	def to_radians(self, deg):
		return (self.math.degrees(deg))



c = Number()
l = List()
print(l.factorial([2,3,4,5,6]))
