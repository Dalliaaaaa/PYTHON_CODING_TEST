import sys
import bisect

si= sys.stdin.readline # input 입력 방식보다 빠른 입력방식
n = int(si())
store = sorted(map(int, si().split())) # 부품 종류와 부품 번호 입력 동시에 정렬
m = int(si())
wish = list(map(int, si().split())) # 사용자 요청 종류와 번호 입력

for x in wish:
    idx = bisect.bisect_left(store, x) # 인덱스 번호 반환, 위치 상관없음
    if store[idx] == x: # 존재하면 yes 출력
        print('yes', end=' ')
    else:
        print('no', end=' ')

print()