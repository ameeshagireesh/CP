n, x = map(int, input().split())
limit = list(map(int, input().split()))
 
temp = limit[x-1]
count = 0
 
for i in limit:
    if (i >= temp and i > 0):
        count += 1
print(count)