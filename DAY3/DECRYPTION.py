num = input('주민등록번호를 입력하시오: ')
num.split('-')

print(num)

if len(num) == 14:
    print("올바르")
    for i in range(len(14)):
        