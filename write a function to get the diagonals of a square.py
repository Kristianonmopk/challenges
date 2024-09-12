def get_diagonals(matrix):
  count = 0
  right_diagonal = []
  left_diagonal = []
  for row in matrix:
      right_diagonal.append(row[count])
      count += 1 
  count2 = (len(matrix) - 1)
  for row in matrix:
      left_diagonal.append(row[count2])
      count2 -= 1  
  return (right_diagonal, left_diagonal)
