num = int(input('모험가 수를 입력하시오: '))
n = []

for _ in range(N):
    n.append(int(input()).split(" "))
n.sort(reverse=True)

for i in n:
    