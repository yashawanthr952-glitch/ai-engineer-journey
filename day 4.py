#Find Second Largest Number in List
def seclarge(a):
    first=max(a)
    second=max(x for x in a if x != first)
    return second


m2=seclarge([54,45,95,8])
print(m2)

#Merge Two Dictionaries
d1 = {'a':1, 'b':2}
d2 = {'b':3, 'c':4}
d1.update(d2)

#Count Frequency of Elements in a List
l=[1,2,2,3,3,3]
d={"1":0,"2":0,"3":0}
l1=0
l2=0
l3=0
for i in l:
    if i == 1:
        l1+=1
    elif i == 2:
        l2+=1
    else:
        l3+=1

print(l1,l2,l3)

for i in l:
    if i == 1:
        d["1"]+=1
    elif i == 2:
        d["2"]+=1
    else:
        d["3"]+=1

print(d)



#Word Frequency in a Sentence
c="I love python python"
did={"I":0,"love":0,"python":0}
for i in c.split():
    if i == "I":
        did["I"]+=1
    elif i == "love":
        did["love"]+=1
    else:
        did["python"]+=1

print(did)



#Check if two strings are anagrams
a="caft"
b="fact"

if sorted(a)==sorted(b):
    print("its an anagram")
else:
    print("its not an anagram")

#Find missing number in list 1–n
lis=[1,23,24,411,442,5155,565,41,548,121,95]
lis_1=[1,23,24,442]
lis_n=[]
for i in lis:
    if i not in lis_1:
        lis_n.append(i)
        
print(lis_n)

#Rotate list by k positions


#Check if list is palindrome

def pan(a):
    b=a[::-1]
    if a ==b:
        print("its a panlindrome")
    else:
        print("its a not panlindrome")

pan("12321")

