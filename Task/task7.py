# # ──── SUAL 1 ────
# # İstifadəçidən ad və soyad daxil etməsini istəyin.
# # Ekrana "Salam, [ad] [soyad]!" yazısını çap edin.
# # Expected Output:
# # Adınızı daxil edin: Əli
# # Soyadınızı daxil edin: Məmmədov
# # Salam, Əli Məmmədov!

# name = input("Enter your name: ")
# surname = input("Enter your surname: ")
# print(f'Salam {name, surname}!')


# # ──── SUAL 2 ────
# # İstifadəçidən iki tam ədəd (int) daxil etməsini istəyin.
# # Onların cəmini, fərqini, hasilini və qismətini çap edin.
# # Expected Output:
# # Birinci ədəd: 10
# # İkinci ədəd: 3
# # Cəm: 13
# # Fərq: 7
# # Hasil: 30
# # Qismət: 3.3333333333333335

# num1 = int(float(input("Enter the first number: ")))
# num2 = int(float(input("Enter the second number: ")))

# cem = num1 + num2
# ferq = num1 - num2
# hasil = num1 * num2
# qismet = num1 / num2

# print(f'Cem:{cem}, Ferq:{ferq}, Hasil:{hasil}, Qismet:{qismet}')


# # ──── SUAL 3 ────
# # İstifadəçidən bir cümlə daxil etməsini istəyin.
# # Cümlədəki simvolların sayını (uzunluğunu) ekrana çap edin.
# # Expected Output:
# # Cümlə daxil edin: Python çox maraqlıdır
# # Simvol sayı: 21

# user = input("Cumle yaz: ")
# cumle = len(user)
# print(F'Simvol sayi:{cumle}')


# # ──── SUAL 4 ────
# # İstifadəçidən float tipində iki ədəd daxil etməsini istəyin.
# # Onların ortalamasını hesablayıb nəticəni 2 onluq rəqəmə qədər yuvarlaqlaşdırın.
# # Expected Output:
# # Birinci ədəd: 7.5
# # İkinci ədəd: 3.8
# # Ortalama: 5.65

# onluq_reqem1 = int(float(input('Birinci reqemi yaz: ')))
# onluq_reqem2 = int(float(input('Ikinci reqemi yaz: ')))
# ortalama = (onluq_reqem1 + onluq_reqem2) / 2
# print(f'Ortalama:{ortalama}')


# # ──── SUAL 5 ────
# # İstifadəçidən bir söz daxil etməsini istəyin.
# # Sözü böyük hərflərlə, kiçik hərflərlə və ilk hərfi böyük olmaqla çap edin.
# # Expected Output:
# # Söz daxil edin: python
# # Böyük: PYTHON
# # Kiçik: python
# # Başlıq: Python

# soz = input('Söz daxil edin: ')
# boyuk = soz.upper
# kicik = soz.lower
# basliq = soz[0]
# print(f'Boyuk:{boyuk}, \n Kicik:{kicik}, \n Basliq:{basliq}')


# # ──── SUAL 6 ────
# # İstifadəçidən yaşını daxil etməsini istəyin (int).
# # f-string istifadə edərək "Siz X yaşındasınız və Y gün yaşamısınız." yazın.
# # Expected Output:
# # Yaşınızı daxil edin: 20
# # Siz 20 yaşındasınız və 7300 gün yaşamısınız.

# yas = int(input('Yaşınızı daxil edin: '))
# gun = yas * 365
# print(f'Siz {yas} yaşındasınız və {gun} gün yaşamısınız')


# ──── SUAL 7 ────
# İstifadəçidən bir tam ədəd daxil etməsini istəyin.
# Ədədin tək yoxsa cüt olduğunu müəyyən edib çap edin.
# Expected Output (misal 1):
# Ədəd daxil edin: 7
# 7 tək ədəddir.
# Expected Output (misal 2):
# Ədəd daxil edin: 12
# 12 cüt ədəddir.

# eded = int(input('Ədəd daxil edin: '))

# if eded % 2 == 0:
#     netice = f'{eded} cüt ədəddir.'
# else:
#     netice = f'{eded} tək ədəddir.'

# print(netice)


# ──── SUAL 8 ────
# İstifadəçidən bir cümlə daxil edin.
# Cümlədə "a" hərfinin neçə dəfə keçdiyini tapıb çap edin.
# Expected Output:
# Cümlə daxil edin: banan almaq istəyirəm
# "a" hərfinin sayı: 4

# cumle8 = input('Cümlə daxil edin: ')
# herf = 'a'
# say = 0

# for i in cumle8:
#     if i in herf:
#         say += 1

# print(say)


# ──── SUAL 9 ────
# Dairənin radiusunu float olaraq daxil edin.
# Dairənin sahəsini hesablayın (S = 3.14 * r * r) və çap edin.
# Expected Output:
# Radius daxil edin: 5.0
# Dairənin sahəsi: 78.5

# r = int(float(input('Dairənin radiusunu float olaraq daxil edin: ')))
# s = 3.14 ** r
# print(f'Dairenin sahesi:{s}')


# ──── SUAL 10 ────
# İstifadəçidən ad daxil etməsini istəyin.
# Adın ilk 3 hərfini, son 2 hərfini və tərsinə çevrilmiş halını çap edin.
# Expected Output:
# Ad daxil edin: Samir
# İlk 3 hərf: Sam
# Son 2 hərf: ir
# Tərsinə: rimaS

# ad = input('Ad yaz: ')
# ilk_uc = ad[0:3]
# son_iki = ad[:-3:-1]
# ters = ad[::-1]

# print(f'Ilk 3:{ilk_uc}, Son 2:{son_iki}, Ters:{ters}')

# ──── SUAL 11 ────
# 5 ədəddən ibarət list yaradın: [10, 20, 30, 40, 50]
# for dövrü ilə hər bir elementi ekrana çap edin.
# Expected Output:
# 10
# 20
# 30
# 40
# 50

# list11 = [10, 20, 30, 40, 50]

# for i in list11:
#     print(i)    


# ──── SUAL 12 ────
# Boş bir list yaradın.
# İstifadəçidən 3 dəfə söz daxil etməsini istəyin və hər sözü listə əlavə edin.
# Sonda listi çap edin.
# Expected Output:
# Söz daxil edin: alma
# Söz daxil edin: armud
# Söz daxil edin: banan
# ['alma', 'armud', 'banan']

# soz1 = input('Soz 1: ')
# soz2 = input('Soz 2: ')
# soz3 = input('Soz 3: ')
# sozler = soz1, soz2, soz3
# bos_list = []

# for i in sozler:
#     bos_list.append(i)

# print(bos_list)


# ──── SUAL 13 ────
# Ədədlər listi verilmişdir: [10, 25, 3, 48, 7]
# Listdəki ən böyük və ən kiçik ədədi tapıb çap edin.
# Expected Output:
# Ən böyük: 48
# Ən kiçik: 3

# ededler = [10, 25, 3, 48, 7]
# en_boyuk = max(ededler)
# en_kicik = min(ededler)
# print(f'En boyuk:{en_boyuk}, En kicik:{en_kicik}')


# ──── SUAL 14 ────
# List verilmişdir: [5, 10, 15, 20, 25, 30]
# for dövrü ilə yalnız cüt ədədləri çap edin.
# Expected Output:
# 10
# 20
# 30

# ededler = [5, 10, 15, 20, 25, 30]

# for i in ededler:
#     if i % 2 == 0:
#         print(f'Cut ededelr {i}')
        

# ──── SUAL 15 ────
# Meyvələr listi: ["alma", "armud", "banan", "üzüm"]
# İstifadəçidən meyvə adı daxil etməsini istəyin.
# Əgər meyvə listdə varsa "Tapıldı!" yoxdursa "Tapılmadı!" yazın.
# Expected Output (misal 1):
# Meyvə adı: alma
# Tapıldı!
# Expected Output (misal 2):
# Meyvə adı: portağal
# Tapılmadı!

# meyve = input('Meyve adi: ')
# meyveler = ["alma", "armud", "banan", "üzüm"]

# for i in meyveler:
#     if i in meyve:
#         print('Tapildi')
#     elif i not in meyve:
#         print('Tapilmadi')
#         break


# ──── SUAL 16 ────
# Ədədlər listi: [3, 7, 2, 9, 4]
# Listi kiçikdən böyüyə və böyükdən kiçiyə sıralayıb çap edin.
# Expected Output:
# Artan: [2, 3, 4, 7, 9]
# Azalan: [9, 7, 4, 3, 2]

# values = [3, 7, 2, 9, 4]
# artan = values.sort()
# azalan = values.sort(reverse = True)
# print(artan)
# print(f'Artan:{values}, Azalan:{azalan}')     


# ──── SUAL 17 ────
# range() istifadə edərək 1-dən 10-a qədər ədədlər listi yaradın.
# for dövrü ilə hər ədədin kvadratını çap edin.
# Expected Output:
# 1 -> 1
# 2 -> 4
# 3 -> 9
# 4 -> 16
# 5 -> 25
# 6 -> 36
# 7 -> 49
# 8 -> 64
# 9 -> 81
# 10 -> 100

# ededler = range(1, 11)
# for i in ededler:
#     kvadrat = i ** 2
#     print(f'{i} -> {kvadrat}')


# ──── SUAL 18 ────
# İki list verilmişdir: [1, 2, 3] və [4, 5, 6]
# Bu iki listi birləşdirib yeni list yaradın. Yeni listin uzunluğunu da çap edin.
# Expected Output:
# Birləşmiş list: [1, 2, 3, 4, 5, 6]
# Uzunluq: 6

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list3 = []
# uzunluq = len(list1 + list2)
# list3 += list1+list2
# print(f'Birlesdirilmis list:{list3}, Uzunluq:{uzunluq}')        


# ──── SUAL 19 ────
# Ədədlər listi: [4, 8, 15, 16, 23, 42]
# for dövrü ilə (sum() istifadə etmədən!) listdəki bütün ədədlərin cəmini hesablayın.
# Expected Output:
# Cəm: 108
# ededler = [4, 8, 15, 16, 23, 42]
# cem = 0
# for i in ededler:
#     cem += i

# print(cem)

# ============================================================================
#  BÖLMƏ 3: DICTIONARY (Asan) — Sual 20-26
# ============================================================================


# ──── SUAL 20 ────
# Şagird haqqında dictionary yaradın: ad, yaş, qiymət.
# for dövrü ilə bütün açar-dəyər(key-value) cütlərini çap edin.
# Expected Output:
# ad : Əli
# yaş : 15
# qiymət : 90

# sagirdler = {
#     "ad" : 'eli',
#     "yaş" : 15,
#     "qiymət" : 90
# }

# for i in sagirdler.items():
#     print(i)


# ──── SUAL 21 ────
# Boş dictionary yaradın.
# İstifadəçidən 3 dəfə məhsul adı və qiymətini (float) daxil etməsini istəyin.
# Sonda dictionary-ni çap edin.
# Expected Output:
# Məhsul adı: çörək
# Qiyməti: 1.5
# Məhsul adı: süd
# Qiyməti: 2.3
# Məhsul adı: yağ
# Qiyməti: 5.0
# {'çörək': 1.5, 'süd': 2.3, 'yağ': 5.0}

dic = {}
user1 = int(float(input("Corek: ")))
user2 = int(float(input("Sud: ")))
user3 = int(float(input("Yag: ")))
dict = user1 + user2 + user3

for i in range(dict):
    
            
# ──── SUAL 22 ────
# Şəhərlər dictionary-si: {"Bakı": 2300000, "Gəncə": 335000, "Sumqayıt": 350000}
# İstifadəçidən şəhər adı daxil etməsini istəyin.
# Şəhər varsa əhalisini, yoxdursa "Şəhər tapılmadı" yazın.
#
# Expected Output (misal 1):
# Şəhər daxil edin: Bakı
# Bakı şəhərinin əhalisi: 2300000
#
# Expected Output (misal 2):
# Şəhər daxil edin: Lənkəran
# Şəhər tapılmadı





# ──── SUAL 23 ────
# Qiymətlər dictionary-si: {"riyaziyyat": 85, "fizika": 90, "kimya": 78, "tarix": 92}
# for dövrü ilə bütün fənləri və qiymətləri çap edin.
# Sonda qiymətlərin ortalamasını hesablayıb çap edin.
#
# Expected Output:
# riyaziyyat: 85
# fizika: 90
# kimya: 78
# tarix: 92
# Ortalama qiymət: 86.25





# ──── SUAL 24 ────
# Dictionary verilmişdir: {"a": 1, "b": 2, "c": 3}
# Yalnız açarları (keys) bir listdə, yalnız dəyərləri (values) başqa listdə çap edin.
#
# Expected Output:
# Açarlar: ['a', 'b', 'c']
# Dəyərlər: [1, 2, 3]





# ──── SUAL 25 ────
# İki dictionary verilmişdir:
# d1 = {"a": 1, "b": 2}
# d2 = {"c": 3, "d": 4}
# Onları birləşdirib yeni bir dictionary yaradın və çap edin.
#
# Expected Output:
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}







# ──── SUAL 26 ────
# Dictionary verilmişdir: {"Python": 90, "Java": 85, "C++": 78}
# Ən yüksək qiyməti olan proqramlaşdırma dilini tapıb çap edin.
#
# Expected Output:
# Ən yüksək qiymət: Python - 90







# ============================================================================
#  BÖLMƏ 4: ORTA SƏVİYYƏ (Qarışıq mövzular) — Sual 27-30
# ============================================================================






# ──── SUAL 27 ────
# Sözlər listi: ["salam", "dünya", "python", "kod", "öyrən"]
# for dövrü ilə hər sözün uzunluğunu dictionary-də saxlayın.
# Nəticəni çap edin.
#
# Expected Output:
# {'salam': 5, 'dünya': 5, 'python': 6, 'kod': 3, 'öyrən': 5}





# ──── SUAL 28 ────
# İstifadəçidən bir cümlə daxil etməsini istəyin.
# Cümləni sözlərə ayırın. Hər sözü və onun uzunluğunu çap edin.
#
# Expected Output:
# Cümlə: Python öyrənmək çox maraqlıdır
# Python - 6 hərf
# öyrənmək - 8 hərf
# çox - 3 hərf
# maraqlıdır - 10 hərf
# Ən uzun söz: maraqlıdır








# ──── SUAL 29 ────
# İstifadəçidən 5 ədəd daxil etməsini istəyin.
# Ədədləri listdə saxlayın. Hər ədədin neçə dəfə təkrarlandığını
# dictionary-də saxlayıb çap edin.
#
# Expected Output:
# Ədəd: 3
# Ədəd: 7
# Ədəd: 3
# Ədəd: 9
# Ədəd: 3
# Təkrar sayı: {3: 3, 7: 1, 9: 1}







# ──── SUAL 30 ────
# Cümlə verilmişdir: "python proqramlasdirma dili"
# for dövrü ilə cümlədəki hər hərfin neçə dəfə keçdiyini
# dictionary-də saxlayın (boşluqları saymayın). Nəticəni çap edin.
#
# Expected Output:
# {'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, 'r': 2, 'q': 1,
#  'a': 3, 'm': 2, 'l': 2, 's': 1, 'd': 2, 'i': 2}











# ============================================================================
#  BÖLMƏ 5: ÇƏTİN SƏVİYYƏ (Qarışıq mövzular) — Sual 31-33
# ============================================================================


# ──── SUAL 31 ────
# Tələbələr listi verilmişdir:
# telebeler = [
#     {"ad": "Əli", "fənlər": {"riyaz": 80, "fizika": 70}},
#     {"ad": "Nigar", "fənlər": {"riyaz": 95, "fizika": 88}},
#     {"ad": "Vəli", "fənlər": {"riyaz": 60, "fizika": 55}},
# ]
# Hər tələbənin ortalama qiymətini hesablayın.
# Ortalaması 70-dən aşağı olanları "Kəsildi" kimi qeyd edin.
# Ən yüksək ortalaması olan tələbəni tapıb çap edin.
#
# Expected Output:
# Əli - Ortalama: 75.0
# Nigar - Ortalama: 91.5
# Vəli - Ortalama: 57.5 (Kəsildi)
# Ən yüksək: Nigar (91.5)








# ──── SUAL 32 ────
# Sinif jurnalı sistemi:
# Aşağıdakı strukturda məlumat verilmişdir:
# jurnal = {
#     "10A": [
#         {"ad": "Əli", "qiymətlər": [80, 90, 85]},
#         {"ad": "Vəli", "qiymətlər": [70, 60, 75]},
#     ],
#     "10B": [
#         {"ad": "Nigar", "qiymətlər": [95, 88, 92]},
#         {"ad": "Leyla", "qiymətlər": [55, 65, 60]},
#     ]
# }
# Hər sinif üçün: hər şagirdin ortalamasını hesablayın.
# Sinfin ümumi ortalamasını tapın.
# Ən güclü sinfi müəyyən edin.
#
# Expected Output:
# --- 10A ---
# Əli: 85.0
# Vəli: 68.33
# Sinif ortalaması: 76.67
# --- 10B ---
# Nigar: 91.67
# Leyla: 60.0
# Sinif ortalaması: 75.83
# Ən güclü sinif: 10A (76.67)





# ──── SUAL 33 ────
# İstifadəçidən bir cümlə daxil etməsini istəyin.
# Cümlədəki hər sözü dictionary-də saxlayın:
#   - açar: söz
#   - dəyər: {"uzunluq": X, "sait_say": Y, "böyük": söz.upper()}
# Nəticəni çap edin.
# (Sait hərflər: a, e, i, o, u, ə, ü, ö, ı)
#
# Expected Output:
# Cümlə: Python gözəl
# Python: {'uzunluq': 6, 'sait_say': 1, 'böyük': 'PYTHON'}
# gözəl: {'uzunluq': 5, 'sait_say': 2, 'böyük': 'GÖZƏL'}