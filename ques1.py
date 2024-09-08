#1768. Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        temp=''
        
        if len(word1)>=len(word2):
            for i in range(len(word1)):
                temp+=word1[i]
                if i<len(word2):
                    temp+=word2[i]
                else:
                    temp+=word2[i:]
        else:
            for j in range(len(word2)):
                if j<len(word1):
                    temp+=word1[j]
                else:
                    temp+=word1[j:]
                temp+=word2[j]
        return temp
if __name__=="__main__":
    #hellow testing....
    pointer=Solution()
    x=pointer.mergeAlternately("hello","motto")
    print(x)