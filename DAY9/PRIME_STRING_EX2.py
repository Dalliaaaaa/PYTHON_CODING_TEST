import math

def is_prime_number(n):
    li = [1] * (n+1)
    for i in range(2, int(math.sqrt(n))+1): #에라토스테네스의 체 적용
        if li[i]:
            for j in range(i+i, n+1, i):
                li[j] = 0
    p = [i for i in range(2, n+1) if li[i]] #소수를 함수 안에서 저장
    return p #소수를 리턴

while 1:
    s = input()
    max_string = []
    
    if s == '0': #0이면 종료
        break
    p = is_prime_number(100000) #10만 범위 정수 입력
    res = 2
    for n in p:
        if str(n) in s: #문자 안에 소수가 존재하면
            res = n
            max_string.append(res)
    print(max_string) #리스트 내부 소수 확인
    print(max(max_string)) #리스트 중 가장 큰 소수값 출력