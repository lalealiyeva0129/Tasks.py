print("Sual1")
list1=[5,22,10,49,58,2,9,100,6,13] #listindeki 10-dan boyuk elementleri cap et
for i in list1:
    if i>10:
        print("i:", i)
        
print("Sual2") 
list2=[2,4,6,8,10,12,14,16,18,20] #listdeki her elementi ikiye vurub yeni list yaratmaq
list3=[x*2 for x in list2 ]
print(list3)

print("Sual3") 
list4=[2,5,6,10,11,13,16] #listdeki elementlerin 2-ye bolunende qaliqsiz olanlarin bir liste yig
list5=[x//2 for x in list4]
print(list5)
         
print("Sual4")
list6=["school","class","university","bachelor","book","student"] #listindeki elementlerde 'c'den istifade olunmayanlari yeni list yaradib ora elave edin
list7=[y for y in list6 if "c" not in y]

print(list7)