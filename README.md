# Arrays

###Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
  ```
  def countEvens(numbers):
      evens = 0
      for number in numbers:
          if number % 2 == 0:
              evens = evens + 1

      return evens

  print countEvens([1, 2, 3, 4, 5, 6, 7, 8, 9]) #Expect 4
  ```

###Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in Math.min(v1, v2) and Math.max(v1, v2) methods return the smaller or larger of two values.
  ```
  def bigDiff(numbers):
      max = numbers[0]
      min = numbers[0]
      for number in numbers:
          if number > max :
              max = number
          if number < min :
              min = number
      return max - min

  print bigDiff([1, 2, 3, 4, 5, 6, 7, 8, 9])# expect 8
  ```
