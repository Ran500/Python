# ---------------------------
# -- Break, Continue, Pass --
# ---------------------------

myNumbers = [1, 2, 3, 5, 7, 10, 13, 14, 15, 19]

# Continue

for number in myNumbers:

    if number == 13:

        continue   # توقف عن الرقم ١٣ وبعدها تكمل

    print(number)

print("#" * 50)

# Break

for number in myNumbers:

    if number == 13:

        break  # يوقف الفور قبل ال١٣

    print(number)

print("#" * 50)

# Pass

for number in myNumbers:

    if number == 13:

        pass  # يعدي اي شي من غير ما يعطيك ايرور  يعني تطنش

    print(number)
