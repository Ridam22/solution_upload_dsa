class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s_t= {}
        t_s= {}
        for a,b in zip(s,t):
            if(a in s_t and s_t[a]!=b) or (b in t_s and t_s[b] != a):
                return False
            s_t[a]= b
            t_s[b]= a
        return True
