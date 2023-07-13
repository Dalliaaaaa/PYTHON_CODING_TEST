result = [] #리스트 선언

while True:
    arr = input("내용을 입력하세요:")
    if arr == '':
        break
    else:
        result.append(arr)
    
result = [i for i in result]
print(result)