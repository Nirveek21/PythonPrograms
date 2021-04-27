def convert(b,c1):
    m=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    n=input("Enter a number")
    hex=0
    c=0
    l=len(n)
    while(l!=0):
        r=m.index(n[l-1])
        hex+=r*pow(b,c)
        c=c+1
        l=l-1
    conv =""
    n1=int(hex)
    if ((c1==16)|(c1==8)|(c1==2)|(c1==10)):
        while(n1!=0):
            r1=n1%c1
            n1=int(n1/c1)
            conv+=m[r1]
        print(conv[::-1])
    else:
        print("Base non-existant")        
x=int(input("Enter base number is in : "))
y=int(input("Enter base to convert to : "))
convert(x,y)