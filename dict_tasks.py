#Tapşırıq 1: Lüğət Yaradılması və Əsas Əməliyyatlar
#Tapşırıq:
"""Bir tələbə lüğəti yaradın: {'isim': 'Ali', 'yaş': 20, 'bölüm': 'Kompyuter Mühəndisliyi'}
#Bu lüğətdəki yaş açarının dəyərini 21 olaraq yeniləyin.
#bölüm açarını silin.
#Lüğətdəki bütün açarları və dəyərləri çap edin."""

"""my_dict={
    'isim': 'Lale',
    'yas':20,
    'bolum':'Riyaziyyat M'
}
print(my_dict)
#Bu lüğətdəki yaş açarının dəyərini 23 olaraq yeniləyin.
my_dict['yas']=21
print(my_dict)
#bölüm açarını silin.
my_dict.pop("bolum")
print(my_dict)
#Lüğətdəki bütün açarları və dəyərləri çap edin.
my_dict.items()
print(my_dict)"""

#Tapşırıq 2 (Gücləndirilmiş): Açar və Dəyər Əlavə Edilməsi və İdarə Edilməsi
#Tapşırıq:
"""1.Boş bir lüğət yaradın.
2.Bu lüğətə aşağıdakı açar-dəyər cütlərini əlavə edin:
{'isim': 'Ayşe', 'yaş': 25, 'şehir': 'Ankara'}
3.şehir açarını İstanbul olaraq dəyişdirin.
4.meslek açarını Mühəndis olaraq əlavə edin.
5.yaş açarının dəyərini 30 olaraq yeniləyin.
6.Lüğətdəki açarları və dəyərləri sıralı şəkildə çap edin:
Açarları artan sıraya görə sıralayın.
Dəyərləri sıralı açarlarla uyğunlaşdırın."""
#Boş bir lüğət yaradın.
my_dict1={}
#Bu lüğətə aşağıdakı açar-dəyər cütlərini əlavə edin:
#{'isim': 'Ayşe', 'yaş': 25, 'şehir': 'Ankara'}
my_dict1['isim']='Ayse'
my_dict1['yas']='25'
my_dict1['sehir']='Ankara'
print(my_dict1)
#şehir açarını İstanbul olaraq dəyişdirin.
my_dict1['sehir']='Istanbul'
print(my_dict1)
#meslek açarını Mühəndis olaraq əlavə edin.
my_dict1['meslek']='Muhendis'
print(my_dict1)
#yaş açarının dəyərini 30 olaraq yeniləyin.
my_dict1['yas']=30
print(my_dict1)
#Lüğətdəki açarları və dəyərləri sıralı şəkildə çap edin:
#Açarları artan sıraya görə sıralayın.
#Dəyərləri sıralı açarlarla uyğunlaşdırın.
a=sorted(my_dict1.keys())
print(my_dict1)
for i,j in my_dict1.items():
    print(f'{i}:{j}')