#Task:1
def create_user(name,age,Role):
    return{"name":name.title(),"age": age,"role": Role}
users = []
users.append(create_user("maha",25,"developer"))
users.append(create_user("balu",28,"manager"))
print("All users:")
for users in users:
    print(users)


#Task 2:  
def calculate_total(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    count = len(numbers)
    if count == 0:
        average = 0
    else:
        average = total / count
    return total, average
result = calculate_total(50, 60, 70, 80)
print("Total:", result[0])
print("Average:", result[1])

#Task 3:
def system_config(**settings):
    print("System Configuration:")
    for key in settings:
        print(key, ":", settings[key])
system_config(mode="debug", version="1.0")

#Task 4:
def factorial(n):
    if n < 0:
        print("Error: Negative numbers not allowed")
        return
    if n == 0:
        return 1
    result = n * factorial(n - 1)
    return result
num1 = 6
print("Factorial of", num1, "is:", factorial(num1))

num2 = -2
print("Factorial of", num2, "is:", factorial(num2))

#Task 5: 

def square_generator(n):

    for i in range(n):
        yield i * i
square_list = []
for i in range(5):
    square_list.append(i * i)
print("List:", square_list)
print("Type of list:", type(square_list))
gen = square_generator(5)
print("Generator values:")
for value in gen:
    print(value)
gen2 = square_generator(5)
print("Type of generator:", type(gen2))

#Task 6: 

try:
    num = int(input("Enter numerator: "))
    den = int(input("Enter denominator: "))
    result = num / den
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Please enter numbers only")

finally:
    print("Program Completed")


#Task 7: 

users = [{"name": "maha", "age": 25, "role": "Developer"},
         {"name": "balu", "age": 30, "role": "Manager"}]

file = open("team_data.txt", "w")
for user in users:
    file.write(user["name"] + ", " + str(user["age"]) + ", " + user["role"] + "\n")
    
file.close()
file = open("team_data.txt", "r")
print("File Content:")
print(file.read())
print("Is file closed?", file.closed)
file.close()
print("Is file closed after closing?", file.closed)
