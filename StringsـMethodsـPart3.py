# ---------------------
# -- Strings Methods --
# ---------------------
# index و find الفرق بين
# index => اذا لم تجد الحرف يحصل خطأ
# find => -1 اذا لم تجد الحرف تطبع

# index(SubString, Start, End) يبحث عن الكلمة

a = "I Love Python"
# print(a.index("P"))  # Index Number 7
# print(a.index("P", 0, 10))  # Index Number 7
# print(a.index("P", 0, 5))  # Through Error

# find(SubString, Start, End)

b = "I Love Python"
print(b.find("P"))  # Index Number 7
print(b.find("P", 0, 10))  # Index Number 7
print(b.find("P", 0, 5))  # -1

# rjust(Width, Fill Char) ljust(Width, Fill Char)

# rjust => اضافة مسافات من اليمين واذا لم يتم تحديد العلامة القيمة الافتراضيه هي المسافة
# ljust => اضافة المسافة من اليسار واذا لم يتم تحديد العلامة القيمة الافتراضيه هي المسافة

c = "Ran"
print(c.rjust(10))
print(c.rjust(10, "#"))

d = "Ran"
print(d.ljust(10))
print(d.ljust(10, "#"))

# splitlines()   => List وضع النص في قائمة او

e = """First Line
Second Line
Third Line"""

print(e.splitlines())

f = "First Line\nSecond Line\nThird Line"

print(f.splitlines())

# expandtabs()    التحكم في التاب وعدد التاب

g = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(2))      # عدد التاب اثنين بين كل تاب

#  title  هل النص هاذا
one = "I Love Python And 3G"  # True لانه احول حرف كبير والحروف اللي بعد الادقام كبيره
two = "I Love Python And 3g"  # False لان الحرف اللي بعد الرقم صغير
print(one.istitle())
print(two.istitle())

# هل هاذي مسافه او لا
three = " "
four = ""
print(three.isspace())  # True
print(four.isspace())  # False

# هل هو حروف صغيره او لا
five = 'i love python'
six = 'I Love Python'
print(five.islower())  # True
print(six.islower())  # False

# هل ينفع ان يكون متغير او لا ؟
seven = "osama_elzero"
eight = "OsamaElzero100"
nine = "Osama--Elzero100"

print(seven.isidentifier())  # True
print(eight.isidentifier())  # True
print(nine.isidentifier())  # False

# a-z هل هيا الفا يعني من
x = "AaaaaBbbbbb"
y = "AaaaaBbbbbb111"
print(x.isalpha())  # True
print(y.isalpha())  # False

# a-z 0-9 هل هم ارقام وحروف يعني
u = "AaaaaBbbbbb"
z = "AaaaaBbbbbb111"
print(u.isalnum())  # True
print(z.isalnum())  # True
