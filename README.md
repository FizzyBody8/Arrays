# Arrays

Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
  ```
  def countEvens(numbers):
      evens = 0
      for number in numbers:
          if number % 2 == 0:
              evens = evens + 1

      return evens

  print countEvens([1, 2, 3, 4, 5, 6, 7, 8, 9]) #Expect 4
  ```

Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in Math.min(v1, v2) and Math.max(v1, v2) methods return the smaller or larger of two values.
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
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.
  ```
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
  ```
