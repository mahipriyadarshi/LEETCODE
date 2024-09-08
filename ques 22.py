# Python3 implementation of the above approach
n = 9
a = [34, 8, 10, 3, 2, 80, 30, 33, 1]

start=0
end=n-1
ans=0
while start<end:
    mid=(start-end)//2
    if a[start]<a[end]:
        ans=max(ans,end-start)
        if a[start+1] < a[end]:
            start = start +1
        else:
            end = end - 1
    else:
        print("HI")