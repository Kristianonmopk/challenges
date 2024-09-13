""""Instructions:

A number is considered Disarium when the sum of its digits, each raised to the power of their respective positions, equals the number itself.
For example, consider the number 175. Here,
1^1+ 7^2 + 5^3 175
So, 175 is a Disarium."""
def is_disarium_number(num):
  new_num = 0
  num = str(num)
  counter = 1
  for digit in num:
      empty_int = int(digit)
      new_num += (empty_int**counter)
      counter += 1
  num = int(num)
  if num == new_num:
      return True
  return False
