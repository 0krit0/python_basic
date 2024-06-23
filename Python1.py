# This is a comment
# v = s/t
# V = ความเร็ว (m/s)
# S = ระยะทาง (m)
# t = ระยะทาง (s)

print("Hello world 1")
"""
# This is a comment
# v = s/t
# V = ความเร็ว (m/s)
# S = ระยะทาง (m)
# t = ระยะทาง (s)
"""
print("Hello world 2")

"""
#
# Part: Python Variables
#
"""
x = 5
y = "Hey Bro"
print(x, y)

x = str(3)
y = int(3)
z = float(3)
print(type(x), type(y), type(z))

"""
#
# Part: Variables Names
#
"""
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
MY_VAR = "John"
myvar2 = "John"

# camel Case
myVariableName = "John" 
# Pascal Case
MyVariableName = "John"
# Snake Case 
my_variable_name = "John"


x = "Hey Bro"
print(x)

y = """1 Hey Bro
2 Hey Bro
3 Hey Bro
4 Hey Bro
5 Hey Bro"""
print(y)

x = "Hey Bro"
print(x[4])
print(len(x))

print("Hey" in x)
print("What sup" not in x)
print(x.upper())
print(x.lower())
print(x.replace("Bro", "Sis"))
print(x.split(" "))

a = "Apple"
b = "Banana"
print(a + " " + b)

price = 20
word = f"Peice: {price:.2f}"
print(word)