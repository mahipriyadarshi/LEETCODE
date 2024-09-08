class Solution:
    def canAliceWin(self, nums: list[int]) -> bool:
        alice_sing,bob_double,alice_double,bob_sing=0,0,0,0

        for i in nums:
            if i<10:
                bob_sing+=i
                alice_sing+=i
            else:
                alice_double+=i
                bob_double+=i
        return (alice_sing>bob_double) or (alice_double>bob_sing)


if __name__=="__main__":
    pointer=Solution()
    nums=[1,2,3,4,5,14]
    print(pointer.canAliceWin(nums))