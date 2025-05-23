# Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")

# Python If-Else
n = int(input())
a = 0
if 1 <= n <= 150:
    for i in range(1,n+1):
        if i < 10:
            a = a * 10 + i 
        elif i < 100:
            a = a * 100 + i 
        else:
            a = a * 1000 + i 
    print (a)
        
# Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if 1 <= a <=10**10 and 1<= b <= 10**10:
        print(a+b)
        print(a-b)
        print(a*b)

# Loops
if __name__ == '__main__':
    n = int(input())
    if 1 <= n <= 20:
        for i in range(n):
            print(i**2)

# Write a function
def is_leap(year):
    leap = False
    if 1900 <= year <= 10**5:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap = True
        else:
            leap = False   
           
    return leap

year = int(input())
print(is_leap(year))