# All even numbers from 1 to 100
for i in range(2,101,2):
     print(i)

# 2. Sum of all odd numbers between 1 and 50
sum = 0 
for i in range(1,51,2):
    sum = sum + i 
print(sum)

# 3. Write a function that takes 2 numbers and returns their sum
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum = a + b
print("Sum:",sum)

# 4. Write a function that checks if a number is prime
c = int(input("Enter a number:"))
for i in range(2,c):
    if c%i == 0:
        print("Not prime")
        break
    else:
        print("Prime")
        break

