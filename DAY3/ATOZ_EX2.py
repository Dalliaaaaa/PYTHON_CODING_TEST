s = input('문자열을 입력하세요: ')
arr = [-1] * 26

for i in range(0, len(s)):
    n = int(ord(s[i])) - int(ord('a')) #a의 아스키 코드 값인 97에서 입력된 문자의 아스키 코드 값을 뺀 인덱싱 값
    if arr[n] == -1:
        arr[n] = i #인데싱 값에 입력받은 문자열 인덱싱 값을 넣음

print(arr)