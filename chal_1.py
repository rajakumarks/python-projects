'''Given a square matrix, mat, return the sum of the matrix diagonals
only include the sum of all the primary diagonal & all the elements of secondary diggonal that are not part of the primary diagonal
'''
mat = [[1,2,3],[4,5,6],[7,8,9]]
def diagonalsum_np(mat):
  import numpy as np
  a = np.array(mat)
  b = np.flipr(a)
  if len(a) % 2 == 0:
    return np.trace(a) + np.trace(b)
  else:
    return np.trace(a) + np.trace(b) - a[len(a)//2][len(a}//2]
def diagonalsum(mat):
  n = len(mat)
  sum = 0
  for i in range(n):
    sum += mat[i][i] + mat[i][n-i-1]
  if n % 2 == 0:
    return sum
  else:
    rerurn sum - mat[n///2][n//2]
print(diagonalsum(mat), diagonalsum_np(mat))
