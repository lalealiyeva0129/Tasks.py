print("hello">"Hello">"HELLO")
#SET

#Setlerde eleve etmek:
#add()-yalniz bir element elave etmek olur
alfa = {"a", "b", "c"}
alfa.add("d")
print(alfa)
#update()- birden cox element elave etmek olar.Hemcinin de list,tuple ile verilmis elementleri de sete cevirerek elave edir setin daxiline.
alfa = {"a", "b", "c"}
alfa.update("x")
print(alfa)

#Setden element silmek:
#remove-teyin etdiyimiz elementi silir.Eger hemin element olmazsa, error verir
alfa = {"a", "b", "c"}
alfa.remove("a")
print(alfa)
#discard()- secilmis elementi silir. Element olmazsa, error vermir
alfa = {"a", "b", "c"}
alfa.discard("b")
print(alfa)
#pop()-bu da silir.Amma setde elementlerin yeri deyisdiyi ucun bundan istifade etmek meslehetli deyil
#clear()-setin butun elementlerin silir.

#Setlerde birlesdirme
#union()-biresdirir iki seti
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "date", "fig"}
union_set = set1.union(set2)
print(union_set)  # {'apple', 'banana', 'cherry', 'date', 'fig'}
# | operatordan istifade edilir
union_set = set1 | set2
print(union_set)  # {'apple', 'banana', 'cherry', 'date', 'fig'}

#Setlerde eyni olanlari gostermek
#interesting() metodu
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "date", "fig"}
intersection_set = set1.intersection(set2)
print(intersection_set)  # {'banana'}
#  & operator
intersection_set = set1 & set2
print(intersection_set)  # {'banana'}

#Setlerin bir birinden ferqleri
#difference()-birinci setde olub da ikincide olmyan elementler
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "date", "fig"}
difference_set = set1.difference(set2)
print(difference_set)  # {'apple', 'cherry'}
#  (-) operator
difference_set = set2 - set1
print(difference_set)  #  {'apple', 'cherry'}

#Her iki setde simmetrik ferq(İki çoxluq arasındakı simmetrik fərq hər iki çoxluqda mövcud olan, lakin hər ikisində olmayan elementləri əhatə edir.)
#symmetric_difference() method
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "date", "fig"}
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  #{'apple', 'cherry', 'date', 'fig'}
# ^ operator
symmetric_difference_set = set2 ^ set1
print(symmetric_difference_set)  #{'apple', 'cherry', 'date', 'fig'}