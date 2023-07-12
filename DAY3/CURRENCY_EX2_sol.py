N, K = map(int, input('화폐 개수와 돈의 가격 입력: ').split()) #N : 화폐 종류 수, K: 거슬러 줄 돈
coins = [] #동전 가치를 저장할 리스트 생성

for _ in range(N): #for i in range(n, 0, -1): 반복문 역탐색 방법, for i in reversed(range(n)): 리스트 역 반환 방법
    coins.append(int(input('동전 가격을 개수만큼 입력: '))) #동전 종류 별 가격 입력
coins.sort(reverse=True) #coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

count_currency = 0
for coin in coins:
    if K >= coin: #화폐보다 거스름돈이 크면
        count_currency += K//coin #몫만큼 더하기
        K %= coin #나머지 할당
        if K <= 0: #만약 K가 0이면 반복문을 탈출합니다.
            break
        
print('거슬러 준 동전 화폐의 수: ', count_currency) #거슬러 준 동전 화폐의 수