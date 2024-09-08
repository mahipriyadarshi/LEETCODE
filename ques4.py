# longest substrings
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings={}
        ans=0
        start=0

        for end in range(len(s)):
            if s[end] in substrings and substrings[s[end]]>=start:
                start=substrings[s[end]]+1
            substrings[s[end]]=end
            ans=max(ans,end-start+1)
        return ans

if __name__=="__main__":
    pointer=Solution()
    x=pointer.lengthOfLongestSubstring("123434211234")
    print(x)

        