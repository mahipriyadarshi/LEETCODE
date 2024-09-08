
class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        if not prices:
            return 0  # If prices list is empty, no purchase can be made
        
        if len(prices) < 2:
            return min(money, prices[0])  # If there is only one or fewer prices
        
        m1 = 101
        m2 = 101
        
        for i in prices:
            if i < m1:
                m2 = m1
                m1 = i
            elif i < m2:
                m2 = i
        
        if m1 + m2 > money:
            return money
        
        return money - (m1 + m2)
if __name__=="__main__":
    pointer=Solution()
    x=pointer.buyChoco([34,100,78,93],100)
    print(x)