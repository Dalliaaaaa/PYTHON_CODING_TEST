n = map(int, input('원하는 시간을 입력하시오: '))
cnt = 0

for i in range (n+1): #입력한 시간까지 반복
    for j in range(60): #분
        for k in range(60): #초
            if '3' in str(i) + str(j) + str(k): #매시각 안에 '3'이 하나라도 포함되어 있다면 참
                cnt += 1 #카운트 증가
        print(cnt)
        
print('최종 3이 카운트 된 결과는: ', cnt)