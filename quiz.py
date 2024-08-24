#alizadelale
print("task2")
#  1
#  1 2
#  1 2 3
#  1 2 3 4
#  1 2 3 4 5   
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=(" "))
    print("")
    
print("task3")
# Istifadeciden eded qebul edib, 1 den bu edede qeder olan elementlerin cemini yazdirmaq.
x=int(input("Zehmet olmasa ededi daxil edin:"))    
print(x)
for i in range(1,x+1):
    if i>0:
       s=(((x+1)*x)/2)
print("Cem=",s)

print("task4")
#Verilmis ededin vurma cedvelin qurun.
n=7
for i in range(1,11,1):
    x=i*n
    print(x)

print("task5")
# Nömrə beşə bölünməlidir
 #Əgər rəqəm 150-dən çox olarsa, onu keçin və növbəti nömrəyə keçin
 #Əgər rəqəm 500-dən çox olarsa, döngəni dayandırın 
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i%5==0:
        if i>=150:
            continue
            if numbers<500:
                break
        print(i)
 
print("task6")
#Bir ədəddəki rəqəmlərin ümumi sayını hesablayın
y=input("Zehmet olmasa ededi daxil edin:")
for i in (y):
    print(int(i))
    
print("task7")
#Aşağıdakı nümunəni çap edin
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=(" "))
    print("")
    
print("task8")
#list1=[10,20,30,40,50] donguden istifade ederek  siyahini ters qaydada cap edin.
list1=[10,20,30,40,50]
list2=[]
for i in list1:
    list2.append(i)
    list2.sort(reverse=True)
    print(list2)
    for x in list2:
        print(x)

print("task9")
#for döngəsindən istifadə edərək -10-dan -1-ə qədər rəqəmləri göstərin   
for i in range(-10,0,1):
    print(i)
    
print("task10 ") 
# For döngəsinin uğurla icrasından sonra “Bitti” mesajını göstərmək üçün else blokundan istifadə edin.
for i in range(5):
    print(i)
else:
    print("Bitdi!")
    
print("task11") 
#Bir diapazonda bütün sadə ədədləri göstərmək üçün proqram yazın
print("25 ile 50 arasinda olan sade ededler:")   
for i in range(25,50):
    if i%2!=0 and i%3!=0 and i%7!=0 and i%5!=0:
        print(i)

    
print("task12")
#Fibonacci seriyasını 10 terminə qədər göstərin:0 1 1 2 3 5 8 13 21 34
x=0
y=1
for i in range(5,-1):
    n=i*(i+1) 
print(n)



