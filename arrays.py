def countEvens(numbers):
    evens = 0
    for number in numbers:
        if number % 2 == 0:
            evens = evens + 1

    return evens

print countEvens([1, 2, 3, 4, 5, 6, 7, 8, 9]) #Expect 5
