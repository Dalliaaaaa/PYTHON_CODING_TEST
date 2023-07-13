input_data = input("나이트의 위치를 입력하세요: ")

row = int(input_data[1]) #정수형 입력 받음, 1
column = int(ord(input_data[0])) - int(ord('a')) + 1 #아스키 코드로 변환, 인덱스 값 계산을 위해 a를 뺀다. 이후 1 더하기

#나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] #시뮬레이션 문제와 같이 좌표 이동 정의
result = 0

for step in steps: #steps 8가지 방향을 순서대로 수행
    next_row = row + step[0] #steps 요소 더하기
    next_column = cloumn + step[1] #steps 요소 더하기
    print(next_row, next_column) #내부 좌표 디버깅
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8: #체스판 바깥으로 나갔을 때
        result += 1 #해당 위치로 이동이 가능하다면 카운트 증가
        
    print(result)