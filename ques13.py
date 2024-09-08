class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        ans = []
        for i in range(len(points)):
            ans.append(points[i][0])

        ans.sort()
        answer = 0

        for j in range(1, len(ans)):
            dif = ans[j] - ans[j - 1]
            if dif > answer:
                answer = dif
        return answer
if __name__=="__main__":
    pointer= Solution()
    x=pointer.maxWidthOfVerticalArea([[2,3],[3,4],[4,5]])
    print(x)