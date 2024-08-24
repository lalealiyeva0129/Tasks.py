a=[1,2,3]
b=a[:]
b[0]=5
print(a)
print(b)#[1,2,3] [5,2,3]????

x1=[10,11,12,13,14]
x2=x1[::-1].append(15)
print(x2)#none cunki listde iki emeliyyat birlikde yerine yetirile bilmez.

print(type(5/2))#2.5 olur cavab. Cunki / bu adi bolmedi. onda cavab float olur.
print(type(5//2))#2 olur cavab . Cunki // bu bolur ve tami gosterir. onda cavab int olur.

a=[1,2,3]
b=a
b.append(4)
print(a)#??


x=3
y="3"
print(x==y)#false. Cunki  x- int, y- str'dir

print(10//3)#//-bele bolmede emeliyyat aparilir ve tam hisse goturulur.

x=[0,1,2,3,4]
x[1:4]=[9,8,7]
print(x)#x[0,9,8,7,4]

a=9
b=18
a=a+(b!=a)
print(a)#10 cunki b a-ya beraber deyil,yeni dogrudur. bu da bize true verer. onun da qiymeti 1 oldugundan 1+9=10 eder

i=1
while i<10:
    if i in range(10,0,-1):
        print(i)
    i=i+3#1,4,7 her ikisi ucun ortaq olani

i=1
while i<10:
    if i in range(1,11,3):
        i+=1
        continue
    print(i)
    i=i+2#2,5,8
    
i=1
while i<10:
    if i in range(2,11,3):
     break
    print(i)
    i=i+2  #1,3
    
l=["py","java","cpp","c"]
for i ,j in enumerate(l,1):
    print(i,j)#1py,2java,3cpp
    
i=1
while i<10:
    if i in range(1,11,2):
        pass
    print(i)
    i=i+3#1,4,7
    
i=1
while i<10:
    i+=1
    if i in range(1,11,3):
        break
    print(i)
    i=i+2#2,5bildim 8 de capa veriri. o niye?
    
i=1
while i<10:
    if i in range(2,11,3):
     break
    i+=2
    print(i)#3,5
     
i=1
while i<10:
    if i in range(1,11,3):
        i+=2
        continue
    print(i)
    i=i+2#3,5,9
    
i=1
while i<10:
    if i in range(1,11,3):
        i+=1
        continue
    print(i)
    i=i+2#2,5,8
    
i=1
while i<10:
    if i in range(10,0,-1):
        print(i)
        i=i+3#1,4,7
        
i=1
while i<10:
    if i in range(1,11,3):
        print(i)
    i=i+2#1,7

number=[1,3,5,7,10,12,14]
total=0
for num in number:
    if num %2==0:
        total+=num
    elif num %3==0:
        total -=num
    else:
        total+=1
print(total)#??


t=(1,2,3,4,5)
for x in t:
    if x %2==0:
        t=t+(x,)
print(len(t))
    
