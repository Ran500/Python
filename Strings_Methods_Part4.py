

# ---------------------
# -- Strings Methods --
# ---------------------
# استبدال الكلمة بكلمه اخرى
# replace(Old Value, New Value, Count)
# replace(كم مرهه يتم الاستبدال ، القيمة الجديده، القيمة القديمه )
a = "Hello One Two Three One One"
print(a.replace("One", "1"))
print(a.replace("One", "1", 1))
print(a.replace("One", "1", 2))

# join(Iterable)
# جعل الكلمات من قائمة الى نص
myList = ["Osama", "Mohamed", "Elsayed"]
print("-".join(myList))  # الفارق بين الكلمات -
print(" ".join(myList))  # الفارق بين الكلامات المسافه
print(", ".join(myList))  # الفرق بين الكلمات الفاصله
print(type(", ".join(myList)))
