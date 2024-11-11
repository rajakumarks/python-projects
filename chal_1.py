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

'''challenge#2:
you are given a sorted array nums of n non-negative integers and an integer maximumBit,  you want to perform the following query n times:
1. find the non-negative int k < 2 * maximumBit such that nums[0] XOR nums[1] XOR ... nums[nums.length -1] XOR k ks maximized
   prexor[0] = num[0], prexor[1] = nums[0] ^ nums[1], prexor[2] = xor of nums[0], nums[1], nums[2]....
2. Remove the last element from the current array nums, prexor[i] xor (2*maxBit)-1 in reverse order
ex. nums = [0,1,1,3],2 -> [0,3,2,3]; [2,3,4,7],3->[5,2,6,5]'''
nums = [0,1,2,2,5,7]
def getMaxXor(nums, maxBit):
  e = 2 ++ maxBit
  n = len(nums)
  prexor = [0] * n
  prexor[0] = nums[0]
  for i range(1,n):
    prexor[i] = prexor[i-1] ^ nums[i]
  # part 2
  ans = []
  for i in range(n-1, -1, -1):
    ans.append((e-1) ^ prexor[i]
  return ans

print(getMaxXor(nums,3))

