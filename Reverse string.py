class Solution(object):Add commentMore actions
    def reverseString(self, s):
        l= 0
        r= len(s)-1
        while l < r:
            copy= s[l]
            s[l]= s[r]
            s[r]= copy
            l+=1
            r-=1
