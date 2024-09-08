# Roman To Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        dataSet={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ans=0
        prev_value=0
        for i in s:
            value=dataSet[i]
            if value>prev_value:
                ans+=value-2*prev_value
            else:
                ans+=value
            prev_value=value
        return ans
if __name__=="__main__":
    pointer=Solution()
    x=pointer.romanToInt("XVIII")
    print(x)