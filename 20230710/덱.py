class StackDef:
    def push_back(stack, value):
        stack.append(value)
        return stack
    
    def push_front(stack, value):
        stack.insert(0, value)
        return stack
    
    def pop_back(stack, result):
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(int(stack[-1]))
            stack.pop()
        return stack, result
    
    def pop_front(stack, result):
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(int(stack[0]))
            stack.pop(0)
        return stack, result
    
    def size(stack, result):
        result.append(len(stack))
        return stack, result
    
    def empty(stack, result):
        if len(stack) == 0:
            result.append(1)
        else:
            result.append(0)
        return stack, result
    
    def back(stack, result):
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(int(stack[-1]))
        return stack, result
    
    def front(stack, result):
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(int(stack[0]))
        return stack, result

stack = []
result = []
for i in range(int(input())):
    inputValue = input().split()
    if len(inputValue) == 1:
        stack, result = getattr(StackDef, inputValue[0])(stack, result)
    else:
        stack = getattr(StackDef, inputValue[0])(stack, int(inputValue[1]))
    
for j in result:
    print(j)