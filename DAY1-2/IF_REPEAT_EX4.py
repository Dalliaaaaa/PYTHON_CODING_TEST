n = int(input("정수(1~100) 1개를 입력하시오: "))
i = 0
total = 0

while i <= n:
    if i%2==0:
        total += i
    i += 1

print(total)

while True:
    a = input("문자를 입력하시오: ")
    if a=="q":
        break
    print(a)