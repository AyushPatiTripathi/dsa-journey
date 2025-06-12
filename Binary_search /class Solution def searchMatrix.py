class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        
        # Step 1: Find the row where target could be
        floor = -1
        for i in range(r):
            if matrix[i][0] <= target <= matrix[i][c - 1]:
                floor = i
                break
        
        if floor == -1:
            return False  # target not in any row range

        # Step 2: Apply binary search on that row
        left = 0
        right = c - 1
        while left <= right:
            m = left + ((right - left) // 2)
            if target == matrix[floor][m]:
                return True
            elif target < matrix[floor][m]:
                right = m - 1
            else:
                left = m + 1
                
        return False

