FIB_LIM = [2 ** x for x in range(8,31)]
MODULO = [2 ** x for x in range(8,21)]
#n=FIB_LIM
def F():
    x, y = 0, 1
    for i in range(0,1073741824):
        x, y = y, x + y
    return y

def fibonacci_modulo(lim=FIB_LIM, mod=MODULO):
    fibs = []
    fib_seq = F()
    for n in range(len(lim)):
        for m in range(len(mod)):
            fibs.append(next(fib_seq) % mod)
    return fibs
print(fibonacci_modulo(lim=FIB_LIM, mod=MODULO))
#for i in range(len(FIB_LIM)):
#    for j in range(len(MODULO)):
#        print(i,'%',j,fibonacci_modulo(i,j))
