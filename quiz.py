#alizadelale
#task1
#  1
#  1 2
#  1 2 3
#  1 2 3 4
#  1 2 3 4 5  
print("Sual1") 
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=(" "))
    print("")
    
#task2
# Istifadeciden eded qebul edib, 1 den bu edede qeder olan elementlerin cemini yazdirmaq.

#task3
#Verilmis ededin vurma cedvelin qurun.
print("Sual3")
n=7
for i in range(1,11,1):
    x=i*n
    print(x)
# istifadeci terfinden eded daxil et, onun vurma cedvelin qur.   
eded=int(input("Ededi daxil edin:"))
for i in range(1,eded+1):
    i=i*2
    print(i)

#task4 
# Nömrə beşə bölünməlidir
 #Əgər rəqəm 150-dən çox olarsa, onu keçin və növbəti nömrəyə keçin
 #Əgər rəqəm 500-dən çox olarsa, döngəni dayandırın 
print("Sual4")
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i%5==0:
        if i>=150:
            continue
            if numbers<500:
                break
        print(i) 
        

    


    
