x = int(input()) #정수 x를 입력 받기
d = [0] * 30001 #DP 테이블 초기화, 크기 지정

#다이나믹 프로그래밍 진행(보텀업)
for i in range(2, x+1):
    d[i] = d[i-1] + 1 #현재의 수에서 1을 뺀 수의 경우의 수에 1을 더함  
    if i % 2 == 0: #현재의 수가 2로 나누어 떨어지는 경우
        d[i] = min(d[i], d[i//2]+1) #현재의 수에서 1을 뺀 경우와 현재 수의 경우의 수를 비교하여 최솟값을 저장
    if i % 3 == 0: #현재의 수가 3으로 나누어 떨어지는 경우
        d[i] = min(d[i], d[i//3]+1)
    if i % 5 == 0: #현재의 수가 5로 나누어 떨어지는 경우
        d[i] = min(d[i], d[i//5]+1)

print(d[x])