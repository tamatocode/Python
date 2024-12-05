#Question 1
m =int(input("Enter the starting number (m): "))
n=int(input("Enter the ending number (n): "))
sum = 0
for i in range(m, n+1):
     sum += i

print(f"The sum of numbers between {m} and {n} is: {sum}")


#Question 2
a = int(input("Write 1st number:  "))
b = int(input("Write 2nd number:  "))
if a%b==0 or b%a==0 :
    print(True)
else:
    print(False)

#Question 3
c = int(input("Enter diameter:  "))
radius = c/2
pi = 3.14
print('perimeter of circle ', 2 * pi * radius)
print('Area of circle ', pi * radius*radius)

#Question 4

num = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, num+1):
    factorial *= i

print("the factorial of the number is:",  {factorial})

#Question 5
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()