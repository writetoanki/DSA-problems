array=list(map(int,input().split(",")))
n=len(array)
water=0
left=[0]*n
right=[0]*n
left[0]=(array[0])

for i in range(1,n):
    left[i]=max(left[i-1],array[i])
right[n-1]=array[n-1]
for i in range(n-2,-1,-1):
    right[i]=max(right[i+1],array[i])
for i in range(0,n):
    water+=min(left[i],right[i])-array[i]
print(water)