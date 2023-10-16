#This program will print out a function f(x)

def f(x):
	return x**3 + 8

#The input of the function will be 9

def main():
	x = 9
	result = f(x)
	print(result)

	if result > 27:
		print("YAY!")

if __name__ == '__main__':
	main()