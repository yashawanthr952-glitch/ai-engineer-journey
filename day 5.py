#Count Frequency of Elements in a List
lst=[1,3,2,3,4,2,2,2,2,3,4,5,4,3,2,3]
freq={}

for i in lst :
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

print (freq)


#Find Second Largest Number
first=max(lst)
second = max(x for x in lst if x !=first )
print(second)

#Remove Duplicates from List

uni=[]

for i in lst :
    if i not in uni:
        uni.append(i)
    

print (uni)

#Merge Two Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict1.update(dict2)
print(dict1)

#Word Frequency Counter from Sentence
a ="help help help i need help"
freq1={"help":0,"i":0,"need":0}
for i in a.split() :
    if i == "help":
        freq1["help"]+=1
    elif i == "i":
        freq1["i"]+=1
    else:
        freq1['need']+=1

print(freq1)

#Find Common Elements Between Two Lists

c = [1, 2, 3, 4]
b = [3, 4, 5, 6]

def comelement(a,b):
    com=[]
    for  i in a:
            if i in b and i not in com:
                com.append(i)
    return com

common=comelement(b,c)
print(common)

#Pattern Printing
n=5
x=""
for i in range(n):
    x +="xox"
    print(x)

#Reverse Each Word in a Sentence
ab="I love python"
rab=ab[::-1]
print(rab)

#Check if Two Strings are Anagrams
a="caft"
b="fact"

if sorted(a)==sorted(b):
    print("its is an anagram")
else:
    print("its not an anagram")

#Find First Non-Repeating Character
word="aabbce"
for i in word:
    if word.count(i)==1:
        print(i)
        break

#Print Multiplication Table (Nested Loops)
for i in range(1,11):
    for j in range(1,11):
        print(i*j,end="\t")
    print()

#Search Element in 2D Matrix

#Two Sum (Without Using Built-in Magic)
#Given a list and a target, return indices of two numbers that add up to target.
Input= [2, 7, 11, 15]
target = 9  

for i in range(len(Input)):
    for j in range(1+i,len(Input)):
        if Input[i]+Input[j]==target:
           print(i,j) 

#Move All Zeros to End
put = [0, 0, 0, 1]

for i in put:
    if i == 0:
        put.remove(i)
        put.append(i)
    else:
        continue

print(put)
#Longest Word in a Sentence


Word="AI engineering is powerful and transformative."
length=''
for i in Word:
    if i.isalpha() or i == ' ' :
        length += i

words=length.split()
longest=''
for i in words:
    if len(i) >len(longest):
        longest=i

print(longest)

#Find Missing Number
Inp= [1,2,4,5]
n=5 
ch=[]
for i in range(1,n+1):
    if i not in Inp:
            ch.append(i)

print(ch)

#Rotate List by k Steps
In=[1,2,3,4,5]
k=2

for i in range(k):
    In.remove(i)
    In.append(i)
    




