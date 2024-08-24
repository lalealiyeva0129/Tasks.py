#lalealiyev

#bos bir list qurub,append metod istifade ederek liste hem string,hem int hem de boolean elementi daxil etmek
#1-ci taski etdikden sonra elave etdiyiniz elementlerin uzerinde listin 2-ci elementi olacaq sekilde yeni element daxil etmek
#2-ci taski etdikden sonra listin ilk elementini onun adindan istifade ederek silmek
#eyni listin son elementini silmek 
#eyni listin her hansisa elementini indeksini gostererek silmek(her iki usul ile)
#sonda listin daxilindeki butun elementleri silmek 

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

