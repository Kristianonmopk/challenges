#Define a function named convert that takes a list of numbers as its only parameter and returns a list of each number converted to a string.
#For example, the call convert([1, 2, 3]) should return ["1", "2", "3"].
#What makes this tricky is that your function body must only contain a single line of code!

#To solve this problem we use list comprehension to convert the list of numbers to a list of strings in only one line
#Alternatively, we could have used the map function to convert the list of numbers to a list of strings in a single line of code

def convert(list_num):
  return [str(i) for i in list_num]
