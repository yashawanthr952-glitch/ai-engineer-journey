#Write a function to check if a number is even.
def oddeven(a):
    if a %2 ==0:
        return "even"
    else:
        return "odd"

a=int(input("enter a number="))
value=oddeven(a)
print(value)

#Write a function to find factorial.
def fac(n):
    i=1
    factorical=1
    while i <=n:
        factorical *= i
        i += 1
    return factorical
    
facto=fac(5)
print(facto)


#Write a function to reverse a string.
def rev(a):
    return a[::-1]

reverse=rev("yashawnth")
print(reverse)


#Write a function that counts vowels in a string. 
def vowel(a):
    v=0
    for i in a:
        if i in ['A','E','I','O','U','a',"e",'i','o','u']:
            v +=1
    return v

vo=vowel('education')
print(vo)


#Write a function to check palindrome.

def pan(a):
    b=a[::-1]
    if a ==b:
        print("its a panlindrome")
    else:
        print("its a not panlindrome")

pan("12321")

#Write a function to find maximum from a list.
def maximum(a):
    return max (a)

m=maximum([54,45,95,8])
print(m)

#Write a function that returns second largest number.

def maxtwo(a):
    first= max (a)
    second =max([x for x in a if x !=first])
    return second

m2=maxtwo([54,45,95,8])
print(m2)


#Write a function that removes duplicates from list.
def dup(a):
    return list(set(a))

dupli=dup([54,45,8,95,8])
print(dupli)

#Write a function that takes list and returns dictionary of frequency.

#Write a function that checks if two strings are anagrams


#list
#Reverse list without using reverse().
def rev(a):
    return a[::-1]

lst=input("enter the list").split()
reverse=rev(lst)
print(reverse)

#Find common elements in two lists.

lst1= ["apple","banana","oranges","watermelon"]
lst2= ["chair","apple","fan","table"]
common=[x for x in lst1 if x in lst2]
print(common)

data = [10, [20, 30], [40, [50, 60]], 70]

flat=[]

for i in data:
    if isinstance(i,list):
        for sub in i:
            if isinstance(sub,list):
                for s in sub:
                    flat.append(s)
            else:
                flat.append(sub)
    else:
        flat.append(i)

print(flat)


#Rotate list by k positions.

#Find missing number from list 1–100.



