def multiply (number, factor):
    number = number*factor

def fBool (b):
    if b == True: b = False
    elif b == False: b = True

def fString (s):
    s += "efgh"

def fNone (n):
    n = 1

def multiplyList (l, factor):
    for i in range(len(l)):
        l[i] = l[i]*factor

def multiplyDictionary(d, fact):
    for i in d.keys():
        d[i] = d[i]*fact

if __name__ == "__main__":
    i = 14
    f = 3.
    c = complex(2,1)
    b = True
    s = "abcd"
    n = None
    list = [1,2,3,4,5,6]
    dict = {0:0, 1:1, 2:2, 3:3}

    multiply(i, 2)
    print(i)

    multiply(f, 2)
    print(f)

    multiply(c, 2)
    print(c)

    fBool(b)
    print(b)

    fString(s)
    print(s)

    fNone(n)
    print(n)

    multiplyList(list, 3)
    print(list)

    multiplyDictionary(dict, 3)
    print(dict)

    
