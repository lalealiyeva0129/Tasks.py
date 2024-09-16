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

s1="abc"
s2="def"
result=s1+s2*2
print(result)
#lalealiyeva
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
b=[14,24,34,44,54,64,74,84,94,104,114,124,134]
c=["alma","hello",True,55,"python",44,False]

#c listinin ilk elementini salam sozu ile deyismek 
#c listinin son  elementini 11 reqemi ile deyismek
#a listinin son 4 elementini heriflerle deyismek 
#b listinin ilk 3 elementini sozlerle evez etmek
c[0]=("salam")
print(c)
c[-1]=11
print(c)
#1
a[-4:]=("a","b","c","d")
print(a)
#2
a[10:15]=("a","b","c","d")
print(a)
b[:3]=("hi","qara","ok")
print(b)