a =39
b=[1,2,4]
def f1():
    global a
    a = 100 #global
    print(a)

def f2():
    a = 234 #local
    print(a)


def f3():
    b = 3  #local
    print(b)

def f4():
    b[0] = 5 #global
    print(b)

f1()
f2()
f3()
f4()
print(a)
print(b)