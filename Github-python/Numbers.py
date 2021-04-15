# -------------
# -- Numbers --
# -------------

# Integer   الرقم الصحيح

print(type(1))
print(type(100))
print(type(10))
print(type(-10))
print(type(-110))

# Float    الرقم العشري

print(type(1.500))
print(type(100.99))
print(type(-10.99))
print(type(0.99))
print(type(-0.99))

# Complex       معقد

myComplexNumber = 5+6j

print(type(myComplexNumber))

# rel  يعني الرقم الحقيقي اللي هو ٥
print("Real Part Is: {}".format(myComplexNumber.real))
# imag يعني الرقم الخيالي اللي هو ٦
print("Imaginary Part Is: {}".format(myComplexNumber.imag))

# [1] You Can Convert From Int To Float or Complex
# [2] You Can Convert From Float To Int or Complex
# [3] You Cannot Convert Complex To Any Type

print(100)
print(float(100))
print(complex(100))

print(10.50)
print(int(10.50))
print(complex(10.50))

print(10+9j)
print(int(10+9j))
