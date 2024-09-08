#Two SUm

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_indices = {}
        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i
    
        return []
if __name__=="__main__":
    pointer=Solution()
    x=pointer.twoSum([2,3,4,5,6],6)
    print(x)