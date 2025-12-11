# single stack
stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack:", stack)

# Pop
stack.pop()

# stack double
size = 10
stack = [None] * size
top1 = -1
top2 = size

# Push ke stack 1
top1 += 1
stack[top1] = 100

# Push ke stack 2
top2 -= 1
stack[top2] = 200

print("Double Stack:", stack) $ double stack
print("Setelah pop:", stack) # output single stack
