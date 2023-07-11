a = input('A, B, C, D 문자에서 1개를 입력: ')
if (a == "A"):
    print("A: best!!!")
elif (a == "B"):
    print("B: good!!")
elif (a == "C"):
    print("C: run!")
elif (a == "D"):
    print("D: slowly~")
else:
    print("what?")
    
a = int(input('1~12 사이 숫자를 입력하여 월 판단: '))
if a//3==1: # 3으로 나눠 몫이 1이면 봄
    print("spring")
elif a//3==2: # 3으로 나눠 몫이 2이면 여름
    print("summer")
elif a//3==3: # 3으로 나눠 몫이 3이면 가을
    print("fall")
else: # 아니면 겨울
    print("winter")