#Task 1 – Print Formatting
print("Hello", "World", "Welcome", "Python")
print("Laptop", "Mouse", "Keyboard", sep=" | ")

#Task 2 – Variables
name = "Ravi"
age = 22
city = "Chennai"

print(name, age, city, sep="-")

#Task 3 – Multiple Assignment
name, age, student = "Meena", 20, True
print(name)
print(age)
print(student)

#Task 4-Indexing
word = "Python"
print(word[0])   
print(word[2])   
print(word[-1])

#Task 5- Arithmetic Operators
print(25 + 10)
print(50 - 20)
print(8 * 5)
print(100 / 10)
print(10 % 3)
print(2 ** 4)
print(20 // 3)

#Task 6- Bodmas Expression
print(3 + 2 * 5 ** 2)

#Task 7-Assigment operator
num = 50
num += 25
print(num) 

num = 100
num /= 10
print(num)

#Task 8- Comparision operator
print(10 > 5)  #True
print(20 < 15) #False
print(5 == 5)  #True
print(10 != 8) #True
print(7 >= 7)  #True
print(6 <= 2)  #False

# TASK 9 - STRING COMPARISON
a = "apple"
b = "Apple"

print(a == b) #false

# TASK 10 - LOGICAL OPERATORS
print(10 > 5 and 5 == 5)
print(5 > 10 or 10 == 10)
print(not(5 > 2))

#Task11 - Membership Operator
numbers = [10,20,30,40,50]

print(20 in numbers)
print(60 in numbers)
print(30 not in numbers)

#Task 12 – Swap Variables
a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)

#Task 13 – Bitwise XOR
a = 6
b = 3

print(a ^ b)
