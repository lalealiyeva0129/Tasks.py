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