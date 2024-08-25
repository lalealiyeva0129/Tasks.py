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
print(tup_1[::-3])#bunu ne qeder eledim tapa bilmedim.

print("task4")
print(tup_1[-1])

print("task5")
print((len(tup_1)*2))
