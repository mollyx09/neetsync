class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = 0
        c = len(matrix[0]) - 1
        while ( r < len(matrix) and -1 < c < len(matrix[0])):
            if matrix[r][c] > target:
                c = c - 1
            elif matrix[r][c] < target:
                r = r + 1
            else:
                return True
        return False
        #Brute force, TC = O(m*n)
        # rows = len(matrix)
        # cols = len(matrix[0])
        # for i in range(rows):
        #     for j in range(cols):
        #         if matrix[i][j] == target:
        #             return True
        
        # return False

        