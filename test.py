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

    
