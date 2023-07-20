j, M = map(int, input().split()) #수열의 크기, 원하는 합의 값
A = list(map(int(input("데이터 직접 입력: ")).split()))

count = 0
interval_sum = 0
end = 0


#start를 차례대로 증가시키며 반복
for start in range(j):
    #end를 가능한 만큼 이동시키기
    while interval_sum < M and end < j:
        interval_sum += A[end]
        end += 1
        
    if interval_sum == M:
        print("중간 카운트: ", count)
        count += 1
    interval_sum -= data[start]
    
print(count)