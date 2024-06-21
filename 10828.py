import sys

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    order = sys.stdin.readline().split()
    if order[0] == "push" :
        stack.append(int(order[1]))
    elif order[0] == "pop" :
        print(stack.pop() if stack else -1)
    elif order[0] == "size":
        print(len(stack))
    elif order[0] == "empty" :
        print(0 if stack else 1)
    elif order[0] == "top" :
        print(stack[-1] if stack else -1)
        