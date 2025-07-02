class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dictionary= {}
        for i in nums:
            if i in dictionary:
                dictionary[i]+=1
            else:
                dictionary[i]=1
            if dictionary[i] > len(nums)//2:
                return i
