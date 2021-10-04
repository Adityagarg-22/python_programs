#multiplication of two matrix#
r1=int(input("enter no of rows in 1 matrix"))
c1=int(input("entr no of columns in 1 matri0x"))
r2=int(input("enter no of rows in 2 matrix"))
c2=int(input("enter no of columns in 2 matrix"))

if(c1!=r2):
    print("multiplication is not possible")
else:
    for i in range(r1):
        temp=[]
        for j in range(c1):
            x=int(input(""))
            temp.append(x)
a.append(temp)
print("enter 2nd matrix")
b=[]
for i in range(r2):
    temp=[]
    for j in range(c2):
        x=int(input(""))
        temp.append(x) 
a.append(temp) 
c=[]
for i in range(r1):
    temp=[]
    for j in range(c2):
        sum=0
        for k in range(c1):
            sum+=a[i][k]*b[k][j]
            temp.append(sum) 
c.append(temp)        