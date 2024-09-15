"""s="hello"

lale_dict={
    "Ad": "Lale",
    "Yas" : "19",
    "Ixtisas": "Riyaziyyat M"
}
print(len(lale_dict))

dict1=dict(Ad ="Lale",Yas = "19",Ixtisas= "Riyaziyyat M")
d=dict1.keys()
print(d)
d=dict1.values()
print(d)
d=dict1.items( )
print(d)
d=dict1.get("Ad")
print(d)"""

#Practice_1
#add_book adlı bir funksiya yaradın ki, bu funksiya başlıq, müəllif və nəşr ili alaraq, bu məlumatlarla yeni bir kitabı kataloqa "mövcuddur" olaraq əlavə 
"""
dict1={
    "ad": "Lale",
    'Soyad': "Aliyeva"
}
dict1.popitem()
print(dict1)
dict2=dict1.copy()
print(dict2)
"""
my_dict = {'ad': 'Ali', 'yaş': 30, 'şəhər': 'Bakı'}
my_dict.pop('şəhər')
print(my_dict)  # 'Bakı'
print(my_dict)  # {'ad': 'Ali', 'yaş': 30}

