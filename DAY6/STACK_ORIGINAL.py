stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
print(len(stack)) #개수(크기)
stack.pop() #맨 뒤 stack 삭제
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) #최상단 원소부터 츨력
print(stack)