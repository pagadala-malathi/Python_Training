#Bitwise Operator Tasks (1–8)
a = 10
b = 6
print(a & b)

x = 12
y = 5
print(x | y)

num = 8
print(~num)

a = 15
b = 9
print(a ^ b)

num = 7
print(num << 2)

num = 20
print(num >> 1) 

a = int(input())
b = int(input())
print(a & b)

a = int(input())
b = int(input())
print(a ^ b)


#String Tasks (9–14)
a ="hi"
print(a*4)

s = "python"
print(s*3)

a = "super"
b = "man"
print(a + b)

a = "hello"
b = " "
c = "world"
print(a + b + c)

name = input()
print(name * 5)

a = input()
b = input()
print(a + b)

#Input & Type Casting Tasks (15–20)
name = input()
print(type(name))

age = input()
age = int(age)
print(age)

a = int(input())
b = int(input())
print(a + b)

m1 = int(input())
m2 = int(input())
print((m1 + m2) / 2)

a = int(input())
b = int(input())
print(3 * a * 2 + b - 2)

num = input()
print(type(num))
num = int(num)
print(type(num))

#Unit Digit Tasks (21–25)

num = input()
print(num[-1])

num = int(input())
print(num % 10)

num = int(input())
print(num // 10)

num = int(input())
print((num // 10) % 10)

num = int(input())
print(num % 10)

# If-Else Tasks (31–34)

num = int(input())
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

marks = int(input())
if marks >= 35:
    print("Pass")
else:
    print("Fail")

num = int(input())
if num > 0:
    print("Positive")
else:
    print("Negative")

num = int(input())
if num > 10:
    print("Greater than 10")
else:
    print("Not greater than 10")  

#Nested If Tasks (35–37) 
age = int(input())
height = int(input())
weight = int(input())

if age >= 18 and height >= 160 and weight >= 60:
    print("Selected")
else:
    print("Rejected")


marks = int(input())
age = int(input())

if marks >= 60 and age >= 17:
    print("Admission Granted")
else:
    print("Admission Denied") 

age = int(input())
height = int(input())
weight = int(input())

if age >= 16 and height >= 150 and weight >= 50:
    print("Selected")
else:
    print("Not Selected")   


#Match Statement Tasks (38–40)             
num = int(input())

match num:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("sunday")
    case _:
        print("Invalid input")


num = int(input())

match num:
    case 1:
        print("Red")
    case 2:
        print("Blue")
    case 3:
        print("Green")
    case _:
        print("Invalid input") 

num = int(input())

match num:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")
    case _:
        print("Invalid input")               

        



