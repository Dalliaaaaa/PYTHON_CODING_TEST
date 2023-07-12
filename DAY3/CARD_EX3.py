N, M = int(input('행과 열을 입력하세여: ').split(" "))
arr = [] #열
lst = [arr * N] #행의 개수

for i in arr:
    arr[i].append(int(input().split(' ')))
