#lalealiyev

#bos bir list qurub,append metod istifade ederek liste hem string,hem int hem de boolean elementi daxil etmek

#1-ci taski etdikden sonra elave etdiyiniz elementlerin uzerinde listin 2-ci elementi olacaq sekilde yeni element daxil etmek

#2-ci taski etdikden sonra listin ilk elementini onun adindan istifade ederek silmek

#eyni listin son elementini silmek 

#eyni listin her hansisa elementini indeksini gostererek silmek(her iki usul ile)

#sonda listin daxilindeki butun elementleri silmek 


"""
abc=[1,44,'kitab',25,"qelem"]

abc.append(23)
abc.append(True)
abc.append("red")
print(abc)

abc.insert(2,False)
print(abc)

abc.remove(1)
print(abc)

abc.pop()
print(abc)

abc.pop(2)
print(abc)

del abc[2]
print(abc)

abc.clear()
print(abc)
"""
"""
abc=[1,44,'kitab',25,"qelem"]
for i in abc:
  print(i)
a="Lale"
for i in a:
    print(i)
    
task2=[11,22,33,44,55]
for i in range(len(task2)):
    print(task2[i])"""
    

"""task3=["alma","armud","heyva"]
i=0
while i < len(task3):
    print("i=",i,task3[i])
    i=i+1"""
    
"""task2=["112","22","33","44"",55"]
newtask=[]
 
for i in task2:
    if "2" in i:
        newtask.append(i)
print(newtask)"""
task2=[1,2,3,4,5,6,7,8,9]
task3=[]
for x in task2:
    if x<5:
        task3.append(x)
print(task3)