class Solution(object):
    def sortSentence(self, s):
        words= s.split()
        res= ['']*10
        for word in words:
            idx= int(word[-1])
            actual= word[:-1]
            res[idx]=actual
        return ' '.join([word for word in res if word!=''])
