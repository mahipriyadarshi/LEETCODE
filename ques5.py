#integer to roman 
class Solution:
    def intToRoman(self, num: int) -> str:
        dataset = {
            1: "I", 4: "IV", 5: "V", 9: "IX",
            10: "X", 40: "XL", 50: "L", 90: "XC",
            100: "C", 400: "CD", 500: "D", 900: "CM",
            1000: "M"
        }
        
        roman_numeral = ""
        for value, numeral in sorted(dataset.items(), reverse=True):
            while num >= value:
                roman_numeral += numeral
                num -= value
        
        return roman_numeral
if __name__=="__main__":
    pointer=Solution()
    x=pointer.intToRoman(456)
    print(x)