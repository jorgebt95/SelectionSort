def sort(numbers): 

	for i in range(5):
		mainposition = i
		for j in range(i,6):
			if numbers[j] < numbers[mainposition]:
				mainposition = j

		temp = numbers[i]
		numbers[i] = numbers[mainposition]
		numbers[mainposition] = temp

numbers = [5,6,4,3,7,8]
sort(numbers)

def test_check():
 assert numbers == [3,4,4,6,7,8]

