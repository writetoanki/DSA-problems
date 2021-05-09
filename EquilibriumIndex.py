array = list(map(int, input().split(",")))
index = -1
totalSum = sum(array)
leftSum = 0
for i in range(0, len(array)):
    totalSum -= array[i]
    if totalSum == leftSum:
        index = i
        break
    else:
        leftSum += array[i]
print(index)

#Brute_Force Technique
#array=list(map(int,input().split(",")))
#index=-1
#n=len(array)
#for i in range(0,n):
#   if(sum(array[:i+1])==sum(array[i:])):
#        index=i
#       break
#print(index)