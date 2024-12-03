import re

def multiply(input):
	pattern = re.compile(r'mul\((\d+),(\d+)\)')

	matches = pattern.findall(input)

	totalSum = 0

	for match in matches:
		x, y = map(int, match)
		totalSum += x * y

	return totalSum

def main():
	with open('input.txt', 'r') as file:
		input = file.read()

	result = multiply(input)

	print(result)

if __name__ == '__main__':
	main()