#Generator of fib

#
def fib(nm):
    '''
    nm : the length of the fib series 
    '''
    a = 1
    b = 1
    n = 1
    if nm>=1:
        while n<=nm:
            if n>1:
                yield b
                a,b = b,a+b
                n +=1
            else:
                yield a
                n += 1
                
#test for fib
for i in fib(1):
    print(i)
#
for i in fib(20):
    print(i)
    
