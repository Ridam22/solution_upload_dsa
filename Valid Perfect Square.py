class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        import math
        sqrt= int(math.sqrt(num))
        if sqrt*sqrt== num:
            return True
        return False
