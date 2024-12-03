import re

def multiply(input):
	mulPattern = re.compile(r'mul\((\d+),(\d+)\)')
	doPattern = re.compile(r'do\(\)')
	dontPattern = re.compile(r'don\'t\(\)')

	totalSum = 0
	mulEnabled = True

	tokens = re.split(r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))', input)

	for token in tokens:
		if mulPattern.match(token):
			if mulEnabled:
				x, y = map(int, mulPattern.findall(token)[0])
				totalSum += x * y
		elif doPattern.match(token):
			mulEnabled = True
		elif dontPattern.match(token):
			mulEnabled = False

	return totalSum

def main():
	with open('input.txt', 'r') as file:
		input = file.read()

	result = multiply(input)

	print(result)

if __name__ == '__main__':
	main()