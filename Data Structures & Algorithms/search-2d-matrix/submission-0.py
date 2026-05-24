class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # identify which row it may potentially be in
        # iterate through that row to see if it exists

        l = 0
        r = len(matrix)-1

        while l <= r:
            mid = (l+r) // 2
            midRow = matrix[mid]

            if midRow[0] <= target <= midRow[-1]:
                # iterate through the list to see if it exists
                for num in midRow:
                    if num == target:
                        return True
                
                return False
            else:
                if target < midRow[0]:
                    r = mid-1
                else:
                    l = mid+1
        
        return False
        