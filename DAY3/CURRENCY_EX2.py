import time
import os
import psutil

process = psutil.Process(os.getpid()) # 공간 복잡도를 위한 프로세스 id 얻기
start_time = time.time() # 시간 측정 시작, 입력 직접 받으면 대기시간 만큼 시간 증가

lst = [1, 10, 500, 100, 1000, 5000, 10000, 50]
N, K = map(int,input('동전 종류 개수와 가격을 입력하시오: ').split(' '))

if  1 <= N <= 10 and 1 <= K <= 100000000:
    cnt = 0

    #for coin in range(N):
    #    coin = int(input('동전 종류를 입력하시오: '))
    #    lst.append(coin)

    lst.sort()
    lst.sort(reverse = True) # 역정렬

    for coin in lst: #가장 큰 동전부터 나눠 동전 수 카운팅    
        cnt += K // coin
        K %= coin

print('동전의 거스름돈 최소 개수는: ', cnt) 

end_time = time.time() # 측정 종료
print("time:", format(end_time - start_time, '.10f')) # 정확도 소수 아래 10자리로 수행 시간 출력
print('MB bytes :', process.memory_info().rss / (1024.0 * 1024.0)) # 해당 프로세스 메모리 공간, 메가 바이트 단위 출력