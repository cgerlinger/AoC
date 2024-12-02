def main():
	with open ('input.txt') as f:
		lines = f.readlines()

	leftNum = []
	rightNum = []

	for line in lines:
		left, right = map(int, line.split())
		leftNum.append(left)
		rightNum.append(right)

	leftNum.sort()
	rightNum.sort()

	totalDistance = 0

	for left, right in zip(leftNum, rightNum):
		totalDistance += abs(left - right)

	# print(f'Total distance: {totalDistance}')

	# Part 2
	from collections import Counter
	right_count = Counter(rightNum)
	similarity_score = 0

	for num in leftNum:
		if num in right_count:
			similarity_score += num * right_count[num]

	print(f'Similarity score: {similarity_score}')

if __name__ == '__main__':
	main()