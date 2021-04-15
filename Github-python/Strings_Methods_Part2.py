# ---------------------
# -- Strings Methods --
# ---------------------

# split() rsplit()

a = "I Love Python and PHP and MySQL"
print(a.split())   # تقسم الكلمات لك  والتقسيم الافتراضي هو المسافه

b = "I-Love-Python-and-PHP-and-MySQL"
print(b.split("-"))  # - تقسم لك الكلمات من علامة

c = "I-Love-Python-and-PHP-and-MySQL"
print(c.split("-", 3))  # يفصل لك اول ثلاث كلمات فقط

d = "I-Love-Python-and-PHP-and-MySQL"
print(d.rsplit("-", 3))  # يفصل لك اول ثلاث كلمات من اليمين فقط

# center()   تضيف لك  اي شي على الكلمة ويجب انك تضيف عدد القيمه اللتي سوف ترجع

e = "Rayan"
print(e.center(9))  # Spaces
print(e.center(9, "#"))  # Hashes
print(e.center(15, "@"))  # @

# count()  يبحث لك عن الكلمة ويكتب لك كم عدد المرات اللي موجوده فيه الكلمة
# حساسه الاحرف
f = "I Love Python and PHP Because PHP is Easy"
print(f.count("PHP"))  # 2 PHP Words
# Only One PHP Word     يبد من اندكس الى اخر عدد اندكس
print(f.count("PHP", 0, 25))

# swapcase()   تعكس لك الاحرف اذا كان كبير تخليه صغير واذا كان صغير تخليه كبير

g = "I Love Python"
h = "i lOVE pYTHON"

print(g.swapcase())
print(h.swapcase())

# startswith()  False او True  اذا كان يبدا في الحرف او الكلمة يرجع لك القيمة

i = "I Love Python"
print(i.startswith("I"))    # True لانه يبدا بحرف اي
print(i.startswith("S"))    # False خطا لانه لا يبدا بحرف الاس
# True من اول الانسدكل ٧ الى الانديكس ١٢ هل اول حرف يبدا بحرف البي
print(i.startswith("P", 7, 12))

# endswith()      False او True  اذا كان ينتهي في الحرف او الكلمة يرجع لك القيمة

j = "I Love Python"
print(j.endswith("n"))  # True  هل ينتهي بحرف ان
print(j.endswith("S"))  # False هل ينتهي بحرف اس
# True من اول الانسدكل٢ الى الانديكس ٦ هل تنتهي بحرف الاي
print(j.endswith("e", 2, 6))
