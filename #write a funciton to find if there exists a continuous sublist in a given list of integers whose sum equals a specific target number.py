#write a funciton to find if there exists a continuous sublist in a given list of integers whose sum equals a specific target number

#Instructions
    #1. Define a function that takes a list of integers and a target number as inputs.
    #2. Inside the function, iterate over the list and keep track of the cumulative sum. If at any point, the cumulative sum equals the target or the cumulative sum minus an earlier sum equals the target, return True.
    #3. Return True if such sublist exists, otherwise return False.

#Example
#For this input
#[23, 2, 4, 6, 7]
#6
#Reason:The sublist [2,4] has a sum equal to 6, which is the target number

#Answer:
def check_sublist_sum(nums, k):
  sublists_accumulation = 0
  number_storage = []
  for number in nums:
      if number == k:
          return True
      sublists_accumulation += number
      number_storage.append(number)
      if sublists_accumulation == k:
          return True
      elif sublists_accumulation > k:
          sublists_accumulation = sublists_accumulation - number_storage[0]
          del number_storage[0]
          if sublists_accumulation == k:
              return True
  if sublists_accumulation > k:
      sublists_accumulation = sublists_accumulation - number_storage[0]
      del number_storage[0]
      if sublists_accumulation == k:
          return True
  return False
