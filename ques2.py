#4. Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n=len(nums1)
        m=len(nums2)
        if m>n:
            return self.findMedianSortedArrays(nums2,nums1)
        else:
            if (n+m)%2!=0:
                if (nums1!=[]) and (nums2!=[]):
                    if nums1[-1]>nums2[0]:
                        return nums2[0]
                    else:
                        return nums1[-1]
                else:
                    return nums1 or nums2
            else:
                return (nums1[-1]+nums2[0])/2
if __name__=="__main__":
    pointer=Solution()
    x=pointer.findMedianSortedArrays([2,3,4,5,6],[4,5,6,7])
    print(x)