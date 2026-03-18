# Section 1: Loop Basics (1–10)
#numbers from 1 to 50 using for loop
for i in range(1, 51):
    print(i)

#even numbers from 1 to 100
for i in range(1, 101):
    if i % 2 == 0:
        print(i)

# odd numbers from 1 to 100
for i in range(1, 101):
    if i % 2 != 0:
        print(i)      

#multiplication table of 7
for i in range(1, 11):
    print("7 x", i, "=", 7 * i)

#sum of numbers from 1 to 100   
total = 0
for i in range(1, 101):
    total = total + i
print("Sum =", total)

#numbers in reverse from 50 to 1
for i in range(50, 0, -1):
    print(i)

#numbers divisible by 3 (1–100)
count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count += 1
print("Count =", count)

#squares of numbers from 1 to 10
for i in range(1, 11):
    print(i * i)

#cubes of first 10 numbers  
for i in range(1, 11):
    print(i ** 3)

#input n and print numbers from 1 to n    
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i)

#Section 2: While Loop (11–15) 
#numbers from 1 to 20 using while
i = 1
while i <= 20:
    print(i)
    i += 1

#factorial of a number using while
n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i += 1
print("Factorial =", fact)    

#Reverse a number using while0
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print("Reversed number =", rev)

#Count digits in a number
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num = num // 10
    count += 1
print("Number of digits =", count)

#Keep asking input until user enters "stop"
text = ""
while text != "stop":
    text = input("Enter something (type 'stop' to end): ")


#Section 3: Nested Loop (16–20)
#Print pattern:
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()


for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()    

#Multiplication tables (1 to 5)    
for i in range(1, 6):
    print("Table of", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print()


for i in range(3):
    for j in range(3):
        print(chr(65 + j), end=" ")
    print()    

num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()    

#Section 4: String Basics (21–25)
#Count total characters in a string    
text = input("Enter a string: ")
count = 0
for ch in text:
    count += 1
print("Total characters =", count)

#Count vowels in a string
text = input("Enter a string: ")
count = 0
for ch in text:
    if ch.lower() in "aeiou":
        count += 1
print("Vowels =", count)

#Count consonants in a string
text = input("Enter a string: ")
count = 0
for ch in text:
    if ch.isalpha() and ch.lower() not in "aeiou":
        count += 1
print("Consonants =", count)

#Reverse a string using loop
text = input("Enter a string: ")
rev = ""
for ch in text:
    rev = ch + rev
print("Reversed string =", rev)

#Check if string is palindrome
text = input("Enter a string: ")
rev = ""
for ch in text:
    rev = ch + rev

if text == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


#Section 5: String Slicing (26–30)    
#first 5 characters of a string
text = input("Enter a string: ")
print(text[:5])

#Print last 3 characters
text = input("Enter a string: ")
print(text[-3:])

#string in reverse using slicing
text = input("Enter a string: ")
print(text[::-1])

#Print every 2nd character
text = input("Enter a string: ")
print(text[::2])

#Remove first and last character from string
text = input("Enter a string: ")
print(text[1:-1])

#Section 6: List Basics (31–35)

#Create a list of 5 numbers and print sum
nums = [10, 20, 30, 40, 50]
total = 0
for n in nums:
    total += n
print("Sum =", total)

#Find maximum value in list
nums = [10, 25, 5, 60, 15]
max_val = nums[0]
for n in nums:
    if n > max_val:
        max_val = n
print("Maximum =", max_val)

#Find minimum value in list
nums = [10, 25, 5, 60, 15]
min_val = nums[0]
for n in nums:
    if n < min_val:
        min_val = n
print("Minimum =", min_val)

#Count total elements in list
nums = [10, 20, 30, 40, 50]
count = 0
for n in nums:
    count += 1
print("Total elements =", count)

#Check if element exists in list
nums = [10, 20, 30, 40, 50]
x = int(input("Enter number to search: "))
found = False

for n in nums:
    if n == x:
        found = True
        break

if found:
    print("Element found")
else:
    print("Element not found")

#List Operations (36–40)  
#Add 3 elements using append()   
nums = [10, 20, 30]
nums.append(40)
nums.append(50)
nums.append(60)
print(nums)

#Insert element at specific index
nums = [10, 20, 30, 40]
nums.insert(2, 25)   
print(nums)

#Remove element using remove()
nums = [10, 20, 30, 40, 50]
nums.remove(30)   
print(nums)

#Reverse list without using .reverse()
nums = [10, 20, 30, 40, 50]
rev = []

for i in range(len(nums) - 1, -1, -1):
    rev.append(nums[i])

print("Reversed list =", rev)

#Sort list without using .sort()
nums = [50, 20, 40, 10, 30]

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

print("Sorted list =", nums)
