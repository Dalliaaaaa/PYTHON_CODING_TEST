n = map(int, input('크기를 입력하시오: '))
plans = input('L, R, U, D 4가지 방향 이동 계획 입력: ').split() #이동 계획 입력
x, y = 1

dx = [0, 0, -1, 1] #X축 방향
dy = [1, -1, 0 ,0] #Y축 방향
move_types = ['R', 'L', 'U', 'D'] #계획서 이동 타입 정의

for plan in plans: #크기 입력한 만큼 값 입력
    for i in range(len(move_types)): #입력한 이동 타입 개수 만큼
        if plan == move_types[i]:
            nx = x + dx[i] #0이고
            ny = y + dy[i] #1이면 다음 위치 : 예) 동쪽으로 이동
            
    if nx < 1 or ny < 1 or nx > 0 or ny > n: #공간을 벗어나느 경우 무시
        continue
    
    x, y = nx, ny #공간이 벗어나지 않으면 이동
    
print('모험가 최종 좌표: ', x, y) #모험가의 최종 좌표 출력
    