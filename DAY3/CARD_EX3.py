N, M = int(input('행과 열을 입력하세여: ').split(" "))
result = 0 #가장 큰 수 초기화

for i in range(n):
    data = list(map(int, input().split())) #한 줄씩 입력받아 확인
    min_value = min(data) #현재 줄에서 가장 작은 수 찾기
    result = max(result, min_value) #'가장 작은 수'들 중에서 가장 큰 수 찾기
print(result)