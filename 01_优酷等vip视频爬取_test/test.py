

L = lambda x:'x > 10' if x > 10 else 'x < 10'
print(L(5))

def L(x):
    if x > 10:
        return 'x>10'
    else:
        return 'x<10'
L(5)