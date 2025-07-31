class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sum= 0
        for i in grid:
            for j in i:
                if j<0:
                    sum+=1
        return sum 
