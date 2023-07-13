import time

start_time = time.time() # 시간 측정 시작, 입력 직접 받으면 대기시간 만큼 시간 증가

n = 5
#n = int(input('원하는 시간을 입력하시오: '))
cnt = 0

for i in range(n+1): #입력한 시간까지 반복
    for j in range(60): #분
        for k in range(60): #초
            if '3' in str(i) + str(j) + str(k): #매시각 안에 '3'이 하나라도 포함되어 있다면 참
                cnt += 1 #카운트 증가
        print(cnt)
        
print('최종 3이 카운트 된 결과는: ', cnt)

end_time = time.time() # 측정 종료
print("time:", format(end_time - start_time, '.10f')) # 정확도 소수 아래 10자리로 수행 시간 출력
print('MB bytes :', process.memory_info().rss / (1024.0 * 1024.0)) # 해당 프로세스 메모리 공간, 메가 바이트 단위 출력
