n = int(input('거스름돈을 가격(정수)로 입력해 주세요: ')) #가격 입력을 받기 위해 정수 캐스팅
cnt = 0

arr = [500, 100, 50, 10] #동전 리스트
for coin in arr:
    cnt += n // coin
    n %= coin

print('동전의 거스름돈 최소 개수는: ', count) #개수 결과 출력