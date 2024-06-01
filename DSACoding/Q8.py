#Program to find the maximum element in a Matrix
"""
Given an NxM matrix. The task is to find the maximum element in this matrix.
Input: mat[4][4] = {{1, 2, 3, 4},
                    {25, 6, 7, 8},
                    {9, 10, 11, 12},
                    {13, 14, 15, 16}};
Output: 25
Input: mat[3][4] = {{9, 8, 7, 6},
                    {5, 4, 3, 2},
                    {1, 0, 12, 45}};
Output: 45
"""
mat = [[9, 8, 7, 6],[150, 4, 3, 2], [1, 0, 12, 45]]
big=0
for i in mat:
    for j in i:
        if big < j:
            big = j 
        
print(big)    
