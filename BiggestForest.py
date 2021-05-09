def treeCount(fores, i, j, n):
    if i < 0 or i > n-1 or j <0 or j > n-1 or fores[i][j] != 'T':
        return 0
    else:
        forest[i][j] = 'X'
        count = 1
        count += treeCount(fores, i - 1, j, n)
        count += treeCount(fores, i + 1, j, n)
        count += treeCount(fores, i, j - 1, n)
        count += treeCount(fores, i, j + 1, n)

        return count


size = int(input())
forest = []
for a in range(size):
    r = input().split()
    forest.append((r))
result = 0
for p in range(size):
    for q in range(size):
        if forest[p][q] == 'T':
            k=treeCount(forest,p,q,size)
            print(k,end=" ")
            result = max([result,k])
if result == 0:
    result= -1
print (result)

