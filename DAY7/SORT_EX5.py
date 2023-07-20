from bisect import bisect_left

#입력받기
N = int(input("N개의 개수를 입력하세요: "))
arr = []

for i in range(N):
    arr.append(input().split(' '))

M = int(input("M개의 개수를 입력하세요: "))
target = []

result = []
for j in range(M):
    target.append(input().split(' '))
    
    if target[j] in arr:
        result.append(True)
    else:
        result.append(False)
        
print(result)