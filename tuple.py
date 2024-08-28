## List ve Tuple arasindaki ferqleri yazmaq 
## tup_1 = ("alma" , 4 , True , 32 , "salam" , 0) tupleinda almadan 32 e qeder elementleri cap etmek 
## tup_1 = ("alma" , 4 , True , 32 , "salam" , 0) tupleinda sondan 3 elementi cap etmek 
## tup_1 = ("alma" , 4 , True , 32 , "salam" , 0) tupleinda sonuncu elementi cap etmek 
## tup_1 = ("alma" , 4 , True , 32 , "salam" , 0) tuplenin uzunlugunu 2 e vurmaq 


print("task1")
print("Lisleri [],tuple'ni ise () ile yazilir. List 1 elementden ibaret ola biler, amma tuple(demet) min 2 elementi olmalidir. n\
    Liste nelerise eleve etmek olar.Tuplede bele bir sey yoxdur. Tuplede sadece verilen elmentler uzerinde emeliyyatlar(say gostermek,copy elemek,index gostermek vs) icra edile biler")
 
print("task2")
tup_1= ("alma" , 4 , True , 32 , "salam" , 0)
print(tup_1[:3])

print("task3")
print(tup_1[-3:])#bunu ne qeder eledim tapa bilmedim.

print("task4")
print(tup_1[-1])

print("task5")
print((len(tup_1)*2))


mytuple1=(2,4,3)
mytuple3=mytuple1*2
print(mytuple3)

print(True**False/True)
"""
i=(12,20,1,0,25)
i.sort()
print(i)#atribute error cunki tuplede siralama ozelliyi yoxdu"""

i=2,10
j=3,5
add=i+j
print(add)

a=3
b=4
print(a,b)
a,b=b,a
print(a,b)

x,y=12,14.0
if(x+y==26):
    print("true")
else:
    print("false")
    
name=['BOB','TOM','JERRY']
print(name[1][-1])

l=[None]*10
print(len(l))

num=[1,2,3,4]
print(num[-1],end=' ')
print(num[-3])

z=set('abc$de')
print('f' in z) 

list1=[0,1,2,3]
list2=list1[1::-1]
print(list2)

t=(2,5,7)
l=[]
for i in t:
    l.append(i)
    if i==5:
        l.pop()
print(l)



