def countEvens(numbers):
    evens = 0
    for number in numbers:
        if number % 2 == 0:
            evens = evens + 1

    return evens

print countEvens([1, 2, 3, 4, 5, 6, 7, 8, 9]) #Expect 4

def bigDiff(numbers):
    max = numbers[0]
    min = numbers[0]
    for number in numbers:
        if number > max :
            max = number
        if number < min :
            min = number
    return max - min

print bigDiff([1, 2, 3, 4, 5, 6, 7, 8, 9]) # expect 8

def centeredAverage(numbers):
    max = numbers[0]
    min = numbers[0]
    sum = 0
    for number in numbers:
        if number > max :
            max = number
        if number < min :
            min = number
    for number in numbers:
        sum = sum + number
    return (sum - min - max)/(len(numbers) - 2)

print centeredAverage([1, 2, 3, 4, 5, 6, 7, 8, 9]) #Expect 5
