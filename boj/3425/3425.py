import sys

input = sys.stdin.readline
MAX_VALUE = 10**9

def num(stack, x):
    stack.append(x)
    return True

def pop(stack):
    if not stack:
        return False
    stack.pop()
    return True

def inv(stack):
    if not stack:
        return False
    stack[-1] = -stack[-1]
    return True

def dup(stack):
    if not stack:
        return False
    stack.append(stack[-1])
    return True

def swp(stack):
    if len(stack) < 2:
        return False
    stack[-1], stack[-2] = stack[-2], stack[-1]
    return True

def add(stack):
    if len(stack) < 2:
        return False
    b = stack.pop()
    a = stack.pop()
    result = a + b
    if abs(result) > MAX_VALUE:
        return False
    stack.append(result)
    return True

def sub(stack):
    if len(stack) < 2:
        return False
    b = stack.pop()
    a = stack.pop()
    result = a - b
    if abs(result) > MAX_VALUE:
        return False
    stack.append(result)
    return True

def mul(stack):
    if len(stack) < 2:
        return False
    b = stack.pop()
    a = stack.pop()
    result = a * b
    if abs(result) > MAX_VALUE:
        return False
    stack.append(result)
    return True

def div(stack):
    if len(stack) < 2:
        return False
    b = stack.pop()
    a = stack.pop()
    if b == 0:
        return False
    
    result = abs(a) // abs(b)
    if (a < 0) != (b < 0):
        result = -result
    
    if abs(result) > MAX_VALUE:
        return False
    stack.append(result)
    return True

def mod(stack):
    if len(stack) < 2:
        return False
    b = stack.pop()
    a = stack.pop()
    if b == 0:
        return False
    
    result = abs(a) % abs(b)
    if a < 0:
        result = -result
    
    if abs(result) > MAX_VALUE:
        return False
    stack.append(result)
    return True

while True:
    operations = []
    while True:
        op = input().strip()
        if op == "QUIT":
            exit()
        if op == "END":
            break
        operations.append(op)
    
    n = int(input())
    result = []
    
    for _ in range(n):
        stack = []
        stack.append(int(input()))
        error = False
        
        for op in operations:
            if op.startswith("NUM"):
                error = not num(stack, int(op.split()[1]))
            elif op == "POP":
                error = not pop(stack)
            elif op == "INV":
                error = not inv(stack)
            elif op == "DUP":
                error = not dup(stack)
            elif op == "SWP":
                error = not swp(stack)
            elif op == "ADD":
                error = not add(stack)
            elif op == "SUB":
                error = not sub(stack)
            elif op == "MUL":
                error = not mul(stack)
            elif op == "DIV":
                error = not div(stack)
            elif op == "MOD":
                error = not mod(stack)
            
            if error:
                break
        
        if error or len(stack) != 1:
            result.append("ERROR")
        else:
            result.append(stack[0])
    
    for r in result:
        print(r)
    print()
    
    try:
        input()
    except:
        break