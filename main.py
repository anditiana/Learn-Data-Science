#matrix challenge

#1. matrix times 2

var_mat = [[5,0],
          [1,-2]]

result_mat = [[0 for column in range(2)] for row in range(2)]

for row in range(len(var_mat)):
 for column in range(len(var_mat[0])):
  result_mat[row][column] = var_mat[row][column]*2

print(result_mat)


#for easiest way we can use numpy lib
import numpy as np
var_mat2 = np.array([[5, 0],
 [1, -2]])

result = var_mat2 * 2
print(result)