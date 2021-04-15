# -------------------
# -- Lists Methods --
# -------------------

# clear()

a = [1, 2, 3, 4]
a.clear()
print(a)

# copy()  نسخ

b = [1, 2, 3, 4]
c = b.copy()

print(b)  # Main List
print(c)  # Copied List

b.append(5)

print(b)  # Main List
print(c)  # Copied List

# count() عد

d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(d.count(1))

# index() بحث

e = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
print(e.index("Ramy"))

# insert()  تحط كلمة قبله

f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(0, "Test")
f.insert(-1, "Test")

print(f)

# pop()  يطبع لك اي عدد مشابه ل الانديكس

g = [1, 2, 3, 4, 5, "A", "B"]
print(g.pop(-3))
