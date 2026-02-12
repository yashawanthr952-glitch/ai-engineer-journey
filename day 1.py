#Store your name in a variable and print it.
a="yashwanth"
print(a)

#Take two numbers (hardcode them) and print their sum.
b=12
c=13
print(b+c)

#Cheaking the type
print(type(a))
print(type (b))

#Swap two variables without using a third variable.
c,b=b,c

print(b,c)

#Take length and breadth. Print area.
length=32
breadth=41
area=length*breadth
print(area)

#Check if a number is even or odd.

number=int(input("what is the number"))

if number%2==0:
    print('it is even')
else :
    print('its is odd')

#Print the greater number.

A=int(input('enter a numbers='))
B=int(input('enter a numbers='))
if A>B:
    print(A,'is greater')
else :
    print(B,'is greater')

#Print Numbers 1 to 10 using dor loop
r=0
for r in range(10):
    r=r+1
    print(r) 


#Print Even Numbers 1 to 20
r=0
for r in range(20):
    r=r+1
    if r%2 ==0:
        print(r)

#Multiplication Table
r=0
for r in range(10):
    r=r+1
    t=5*r
    print("5 x",r,"=",t) 


#Sum of First N Numbers
i=0
n=5
total=0
while i <= n:
    total+= i
    i += 1

print(total)


#Factorial of a Number

i=1
n=5
fac=1
while i <= n:
    fac *= i
    i += 1

print(fac)

#Reverse a String
s="python"
print(s[::-1])



#Count Vowels in a String
v="education"
vowel=0
for i in v:
    if i in ['A','E','I','O','U','a',"e",'i','o','u']:
        vowel +=1

print(vowel)


#Check Prime Number

p=int(input('enter a number='))

if p<=1:
    print('not prime')
else:
    is_prime = True
    
    for i in range(2, p):
        if p % i == 0:
            is_prime = False
            break
    if is_prime:
        print('prime')
    else:
        print("not prime")


#Create a Function to Add Two Numbers
def add(a,b):
    addition=a+b
    print(addition)
    
    
add(13,32)


#Function to Find Square
def square(a):
    sq=a*a
    print(sq)

square(5)
    
#Function to Check Even/Odd
def oddeven(a):
    if a%2 ==0:
        print('its even')
    else:
        print("its oddd")

oddeven(3)


#Function to Find Maximum of Three Numbers
def minmax(a):
    print(max(a))
    print(min(a))

numm=[3,32 ,233]
minmax(numm)


#Calculator Function
def calculator(a,b,operation):
    if operation=="add":
        ad=a+b
        print(ad)
    elif operation == 'sub':
        s=a-b
        print(s)
    elif operation == 'mul':
        m=a*b
        print(m)
    elif operation == "div":
        d = a / b
        print(d)
    else:
        print('no operation')

calculator(2,3,"add")