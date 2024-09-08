class Solution:
    def maxProduct(self,nums:list)-> int:
        largestNum,secondlargestNum=0,0
        smallestNum,secondSmallestNum=float("inf"),float("inf")
        
        for n in nums:
            if n<smallestNum:
                secondsmallestNum=smallestNum
                smallestNum=n
                
            elif n<secondsmallestNum:
                secondsmallestNum=n
            if n>largestNum:
                secondlargestNum=largestNum
                largestNum=n
            elif n>secondlargestNum:
                secondlargestNum=n
                
        return (largestNum*secondlargestNum)-(smallestNum*secondsmallestNum)
if __name__=="__main__":
    pointer=Solution()
    x=pointer.maxProduct([2,3,4,5,6])
    print(x)