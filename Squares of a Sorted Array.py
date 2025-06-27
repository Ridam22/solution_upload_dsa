class Solution(object):
    def sortedSquares(self,num):
        l= len(num)
        low= 0
        up= l-1
        jhanda= l-1
        listt= [0]*l
        while low<= up:
            if abs(num[low])> abs(num[up]):
                listt[jhanda]= num[low]**2
                low+=1
            else:
                listt[jhanda]= num[up]**2
                up-=1
            jhanda-=1
        return listt
