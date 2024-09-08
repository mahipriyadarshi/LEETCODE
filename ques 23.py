class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        miss = 1
        result = 0
        i = 0

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                result += 1

        return result
if __name__=="__main__":
    pointer=Solution()
    l=[1,5,10]
    n=22
    x=pointer.minPatches(l,n)
    print(x)