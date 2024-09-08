class Solution:
    def imageSmoother(self,img):
        m,n=len(img),len(img[0])
        
        ans=[[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                ans[i][j]=self.smoothen(img,i,j)
                
        return ans
    def smoothen(self,img,x,y):
        m,n=len(img),len(img[0])
        Sum,Count=0,0
        for i in range(-1,2):
            for j in range(-1,2):
                nx,ny=x+i,y+j
                if 0<=nx<m and 0 <=ny <n:
                    Sum+=img[nx][ny]
                    Count+=1
        return Sum//Count
    
if __name__=="__main__":
    pointer=Solution()
    
    x=pointer.imageSmoother([[100,200,100],[200,50,200],[100,200,100]])
    for i in x:
        print(i)