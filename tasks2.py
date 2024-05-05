# 1.) verilmiş listdəki ədədlərin hansılarının hər hansı bir ədədin kvadratı olduğunu define funksiyasında yazıb və listin içərisində ekrana çıxarın. 
# mylist=[-4,-16,0,1,4,5,9,16,25,36,49,64,81,100]

#  2)Funksiya yazin list qebul etsin ve tekrarlanmayan elementleri bizə qaytarsın:
#  input:[-1,1,2,2,6,7,7,'say']

# 3) Verilmiş inputdakı bütün rəqəmlərin bir birlərinə hasilini icra edən funksiya yazın

# 4) verilmiş ədədin bölənlərini list comprehension istifadə edərək yazın

# 5)Əlininzdə ayların olduğu bir list var siz ay qarşısında uzunluğu olduğu bir dictionary yaradın və bunu comprehension ilə edin və alınan listi print etdirin.

# mənim listim
# mylist=['may','iyun','iyul']
# bu şəkildə olacaq
# {'may': 3, 'iyun': 4, 'iyul': 4}

# 6)names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
#  verilmiş list-dən yalnız adların olduğu və kiçik hərflərlə yazıldığı list düzəldin və bunu conprehension ilə edin (əlavə olaraq funksiya da 
# istifadə edəbilərsiz).
# ['rick', 'morty', 'summer', 'jerry', 'beth']

# 7) verilmiş iki listdəki ədədlərin indexlərinə uyğun olaraq ortalamasını tapın.
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]

# results=[ 2.5, 3.5, 4.5]

#---------------------------------------------------------------------------------------------------------------

# 1.) verilmiş listdəki ədədlərin hansılarının hər hansı bir ədədin kvadratı olduğunu define funksiyasında yazıb və listin içərisində ekrana çıxarın. 

# 1ci usul
# mylist=[-4,-16,0,1,4,5,9,16,25,36,49,64,81,100]

# for i in mylist 
# import math
# mylist=[-4,-16,0,1,4,5,9,16,25,36,49,64,81,100]
# newlist = []
# for i in mylist :    
#     if i >= 0:
#         kokalti = i ** 0.5
#         newlist.append(kokalti)
#     else :
#         print("menfi ededlerin kokaltisi olmur")
# print( newlist)   

# 2ci usul     
# import math

# mylist = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]

# newlist = [i**0.5 for i in mylist if i >= 0]

# print(newlist)
    

#  2)Funksiya yazin list qebul etsin ve tekrarlanmayan elementleri bizə qaytarsın:
#  input:[-1,1,2,2,6,7,7,'say']
# def mylist(newlist):
#     return list(set(newlist))

# nlist = [1,3,4,2,5,3,4,4,9,6,3,2,5]
# xlist = mylist(nlist)
# print( xlist ,"tekrarlanmayan elementlerdir" )


#-------------------------------------------------------------------------------------------------
# 3) Verilmiş inputdakı bütün rəqəmlərin bir birlərinə hasilini icra edən funksiya yazın

# def reqemlerinhasili(eded):
#     mylist = [int(x) for x in eded]
#     hasil = 1
#     for i in mylist:
#         hasil *= i
#     return hasil

# reqem = input("ededleri daxil edin ")
# print( reqemlerinhasili(reqem))


#----------------------------------------------------------------------------------------------------
# 4) verilmiş ədədin bölənlərini list comprehension istifadə edərək yazın

# def bolenlerinsayi(reqem):
#     bolenler = [ i for i in range(1 ,reqem+1) if reqem % i == 0]
#     return bolenler

# reqem = int(input("ededi daxil edin "))

# print( bolenlerinsayi(reqem))

#----------------------------------------------------------------------------------------------------
# 5)Əlininzdə ayların olduğu bir list var siz ay qarşısında uzunluğu olduğu bir dictionary yaradın və bunu comprehension ilə edin və alınan listi print etdirin.

# mylist=['yanvar','fevral','mart','aprel','may','iyun','iyul','avqust','sentyabr','oktyabr','noyabr','dekabr']
# mydict = {i:len(i) for i in mylist}
# print(mydict)

#----------------------------------------------------------------------------------------------------
# 6)names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
#  verilmiş list-dən yalnız adların olduğu və kiçik hərflərlə yazıldığı list düzəldin və bunu conprehension ilə edin (əlavə olaraq funksiya da 
# istifadə edəbilərsiz).

# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# newlist = [i.split()[0].lower() for i in names]    
# print(newlist)

#----------------------------------------------------------------------------------------------------
# 7) verilmiş iki listdəki ədədlərin indexlərinə uyğun olaraq ortalamasını tapın.

# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]

# def ortalama(nums1,nums2):
#     newlist = [ (i+j)/2 for i,j in zip(nums1,nums2)]
#     return newlist

# print(ortalama(nums1,nums2))
