class Basic:
    def orr(x,y):
        if x==1:
            return 1
        elif y==1:
            return 1
        else:
            return 0
    def andd(x,y):
        if x==1:
            if y==1:
                return 1
            else:
                return 0
        else:
            return 0
    def nott(x):
        if x==1:
            return 0
        else:
            return 1
    def nandd(x,y):
        m=aand(x,y)
        if m==1:
            return 0
        else:
            return 1
    def norr(x,y):
        v=oor(x,y)
        if v==1:
            return 0
        else:
            return 1        
x=1    
while x==1:    
    a=int(input('::'))
    b=int(input('::'))
    s=input('Select gate (and,or,not,nand,nor) ::')
    if s=='or':
        print (Basic.orr(a,b))
    elif s=='and':
        print(Basic.andd(a,b))
    elif s=='nand':
        print(Basic.nandd(a,b))
    elif s=='nor':
        print(Basic.norr(a,b))
    elif s=='not':
        print(Basic.nott(a))
    else:
        print('Invalid') 
    x=int(input('continue(1/0)::'))  
