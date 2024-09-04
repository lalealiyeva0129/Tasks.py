"""## List ve Tuple arasindaki ferqleri yazmaq 
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
print((len(tup_1)*2))"""

## thistuple = ("salam" , 42 ,True , "hi") tupllenin sonuna 21 reqemini elave etmek 
## thistuple = ("salam" , 42 ,True , "hi") tuple-in ortasına alma sozunu elave etmek 
## thistuple = ("salam" , 42 ,True , "hi") birinci elementi sagol ile deyismek 
## thistuple = ("salam" , 42 ,True , "hi") True-ni silmek 
## thistuple = ("salam" , 42 ,True , "hi" , False, 91 , 33 , "alma") tuple-ni ele 3 hisseye bolmek ki ilk hissede daha cox element olsun 
## thistuple = ("salam" , 42 ,True , "hi") tuple-nin elementlerini ayri ayri cap etmek 
## thistuple = ("salam" , 42 ,True , "hi") tuplenin elementlerini 4 defe tekrar eletdirmek (tuple icinde)

"""print("task1")
thistuple = ("salam" , 42 ,True , "hi")
lis=list(thistuple)
lis.append(21)
print(tuple(lis))

print("task2")
thistuple = ("salam" , 42 ,True , "hi")
list1=list(thistuple)
list1.insert(2,"alma")
print(tuple(list1))

print("task3")
thistuple = ("salam" , 42 ,True , "hi")
list2=list(thistuple)
list2[0]="sagol"
print(tuple(list2))

print("task4")
thistuple = ("salam" , 42 ,True , "hi")
list3=list(thistuple)
list3.pop(2)
print(tuple(list3))

print("task5")
thistuple = ("salam" , 42 ,True ,"hi",False,91,33,"alma")
(*a,b,c)=thistuple
print(a)
print(b)
print(c)

print("task6")
thistuple = ("salam" , 42 ,True , "hi")
(a,b,c,d)=thistuple
print(a)
print(b)
print(c)
print(d)

print("task7")
thistuple = ("salam" , 42 ,True , "hi")
print(thistuple*4)
"""
