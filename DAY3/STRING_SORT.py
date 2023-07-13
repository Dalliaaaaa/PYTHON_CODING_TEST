s = input('문자열을 입력하시오: ')
lst = []
total = 0

for i in s: #문자 리스트 정렬
    if i.isalpha():
        lst.append(i)
    else:
        total += int(i)
        lst.sort()

if total != 0:
    lst.append(str(total))
    
print(''.join(lst))