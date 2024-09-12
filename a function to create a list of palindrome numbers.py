#A number is a palindrome if it remains the same when its digits are reversed.

def generate_palindromes(start, end):
  pali_list = []
  for i in range(start, end):
    i = str(i)
    if i[::-1] == i:
        i = int(i)
        pali_list.append(i)
  return pali_list

print(generate_palindromes(1,100))

input()

#And here's another solution but with list comprehension

def generate_palindromes2(start, end):
  return [i for i in range(start,end) if str(i) == str(i)[::-1]]

print(generate_palindromes2(1,100))
