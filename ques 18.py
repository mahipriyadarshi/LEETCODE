class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        floorDevs = []
        totalBeam= 0
        for floor in bank:
            floorDev = floor.count("1")
            if(floorDev>0): floorDevs.append(floorDev)
        for i in range(len(floorDevs)-1):
            totalBeam += floorDevs[i]*floorDevs[i+1]
        return totalBeam
if __name__=="__main__":
    pointer=Solution()
    x=pointer.numberOfBeams(["011101","111000","110100","001011","010101"])
    print(x)