#Mapping-Xeritelesdirme usulu,listlerde xerite ve filtrleme usulu ile yazilis var. Bu yazilisda az setirden istifade etmek ucundur. Yer az tutur ve cod seliqeli gorsenir.
#dustur list1=[i for i in x]
x= [1, 4, 6, 12, 3]
map = [n ** 3 for n in x]

print(map)  # [1, 64, 216, 1728, 27]

#Filtering-filterleme movcud siyahidan mueyyen bir sertle cavab veren elementleri secmek ve yalniz bu elementleri ehtiva eden yeni siyahi duzeltmekden ibaretdir.
x= ['pony', 'confine', 'utter', 'decrease', 'entertain']
filter = [y for y in x if 'a' in y]

print(filter)  # ['decrease', 'entertain']

#Practice_1
#Bu task'da yalnız 3-ə tam bölünən ədədləri seçib, onları 3-ə bölüb nəticələri yeni bir siyahıda saxlayırıq.
nums=[10, 15, 20, 25, 30, 35, 40, 45, 50]
x=[i//3 for i in nums if i %3==0]
print(x)#[5,10,15] Burda hem mapping'den hem de filtering'den istifade olunur.

#Practice_2
#Verilmiş bir üçlü set'den  ibarət list var. Bu siyahıdan ədədlərinin cəmi 20-dən böyük olan üçlükləri seçin və hər bir üçlüyü azalan sıraya düzün. Nəticədə əldə olunan yeni siyahını (new_lst) yaradın.
list1=[(1, 5, 15), (7, 8, 10), (6, 6, 6), (2, 3, 30)]
list2=[ tuple(sorted(i,reverse=True)) for i in list1 if sum(i)>20]
print(list2)# [(15,5,1),(10,8,7),(30,3,2)]

#Practice_3
#İki siyahı (nums1 və nums2) verilir. Bu siyahılardakı ədədlərin hər bir kombinasyonunun hasilini hesablayıb total_nums adında bir siyahıya yığın.
num1=[1,2,3]
num2=[4,5]
total_num=[i*j for i in num1 for j in num2]
print(total_num)#[4,5,8,10,12,15]

#Practice_4
#Tam ədədlərin, ədədlərin siyahısını götürən və yalnız rəqəmlərinin cəminə bölünən tam ədədləri ehtiva edən bölünən adlı yeni siyahı qaytaran siyahı anlayışı yaradın.
nums = [12,23,45,74,95]  # Məsələn bir siyahı
divisible = [i for i in nums if i % sum(int(n) for n in str(i)) == 0]
print(divisible)

