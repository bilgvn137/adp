# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside Push() and Pop() - move TopOfStack yourself.

# Exercise 1
Stack = []
TopOfStack = -1
for i in range(10):
    Stack.append(-1)


def IsEmpty():
    return TopOfStack == -1
    pass


def IsFull():
    return TopOfStack == 9
    pass


# Exercise 2
def Push(Item):
    global Stack, TopOfStack
    if  TopOfStack==9:
        return False
    else:
        TopOfStack=TopOfStack+1
        Stack[TopOfStack]=Item
        return True
    pass


# Exercise 3
def Pop():
    global Stack, TopOfStack
    if TopOfStack==-1:
        return -1
    else:
        item=Stack[TopOfStack]
        TopOfStack=TopOfStack-1
        return item
    pass


# Exercise 4
def Peek():
    global Stack, TopOfStack
    if TopOfStack == -1:
        return -1
    else:
        item = Stack[TopOfStack]
        return item
    pass


def Size():
    global Stack, TopOfStack
    return TopOfStack+1
    pass


# Exercise 5
def ReverseWord(Word):
    TopOfStack=-1
    for i in range(len(Word)):
        TopOfStack = TopOfStack+1
        Push(Word[i])
    str=""
    for j in range(len(Word)):
        a=Pop()
        TopOfStack = TopOfStack - 1
        str=str+a
    return str
    pass

