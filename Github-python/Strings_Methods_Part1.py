# ---------------------
# -- Strings Methods --
# ---------------------

# strip() rstrip() lstrip()

a = "    I Love Python    "
print(len(a))  # يحسب لك الخانات
print(a.strip())                # تشيل المسافات من اليمين واليسار
print(a.rstrip())               # تشيل المسافات من اليمين
print(a.lstrip())               # تشيل المسافات من اليسار
# اذا حددت لها شي في الاقواس سوف تحذفه اما اذا لم تحدد سوف تحذف المسافه
a = "#####I Love Python####"
print(a.strip("#"))         # تشيل الشباك من اليمين واليسار
print(a.rstrip("#"))        # تشيل الشباك من اليمين
print(a.lstrip("#"))        # تشيل الشباك من اليسار
# نفس الكلام ينطبق على اي شي
a = "@#@#@#I Love Python@#@#@#"
print(a.strip("@#"))
print(a.rstrip("@#"))
print(a.lstrip("@#"))

# title()

b = "I Love 2d Graphics and 3g Technology and python"   #
print(b.title())                # اي حرف بعد المسافة او بعد الرقم يكون حرف كبير

# capitalize()

b = "I Love 2d Graphics and 3g Technology and python"
# اول حرف من كلمة يبقى كبير لكن الحروف اللي بعد الارقام تكون صغيره
print(b.capitalize())

# zfill             تضيف لك رقم على الشمال

c, d, e, f = "1", "11", "111", "1111"

print(c)
print(d)
print(e)
print(f)
# تحدد كم خانه يضيف صفر لها  اعلى قيمه
print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
print(f.zfill(4))

# upper()

g = "osama"

print(g.upper())            # يحول لك كل الحروف الى احرف كبيره

# lower()

h = "OSama"

print(h.lower())           # يحول  لك كل الحروف الى احرف صغيرهه
