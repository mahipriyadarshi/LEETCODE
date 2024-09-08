from collections import *
from math import *
class solution:
    def minOperations(self, nums: list[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for c in counter.values():
            if c == 1:
                return -1
            ans += ceil(c / 3)
        return ans
if __name__=="__main__":
    pointer=solution()

    x=pointer.minOperations([14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12])
    print(x)