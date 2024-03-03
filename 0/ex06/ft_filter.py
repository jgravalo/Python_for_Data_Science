def ft_filter(func, iter):
	newlist = []
	for x in iter:
		if func(x) == True:
			newlist.append(x)
	yield newlist

def test1():
	ages = [5, 12, 17, 18, 24, 32]

	def myFunc(x):
		if x < 18:
			return False
		else:
			return True

	adults = list(filter(myFunc, ages))
	adults2 = list(ft_filter(myFunc, ages))
	print(adults)
	print(adults2)
		
def test2():
	def check_even(number):
		if number % 2 == 0:
			return True  
		return False

	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

	even_numbers = list(filter(check_even, numbers))
	even_numbers2 = list(ft_filter(check_even, numbers))
	print(even_numbers)
	print(even_numbers2)

def main():
	test1()
	test2()

if __name__ == "__main__":
	main()