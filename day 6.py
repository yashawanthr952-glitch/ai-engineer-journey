#Frequency Counter – Most Frequent Element
nums = [4, 1,2,1,1, 2, 2, 3, 4, 4, 5, 2, 4, 3]
freq={}
for i in nums:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

most=max(freq,key=freq.get)
max_feq=[x for x,v in freq.items() if v == most]

print(min(max_feq))

#Word Frequency Counter (Text Processing)
text = "AI is the future and AI is powerful and AI is everywhere ai"
words=''
for i in text:
    if i.isalpha() or i == " " :
        words += i
word = words.lower().split()
print(word)
w={}
for i in word:
    if i in w:
        w[i]+=1
    else:
        w[i]=1
n=2
top2=[]
sorted_dict = sorted(w.items(), key=lambda x: x[1], reverse=True)
print(sorted_dict)
for word, count in sorted_dict[:2]:
    print(word, count)


#Sorting Logic – Custom Sort by Second Value
students = [
    ("Rahul", 85),
    ("Ankit", 92),
    ("Priya", 78),
    ("Vikas", 92),
]

s=sorted(students,key=lambda x: (x[1],x[0]),reverse=True)
print(s)

#Nested List Processing – Matrix Flatten
matrix = [
    [[1,2], [3,4]],
    [[5,6], [7,8]]
]

Flattend=[]
for i in matrix:
    if isinstance(i,list):
        for s in i:
            if isinstance(s,list):
                for j in s:
                    Flattend.append(j)
            else:
                Flattend.append(s)
    else:
        Flattend.append(i)

print(f'Flattend={Flattend}')
print(f'Sum={sum(Flattend)}')
p=len(Flattend)
print (p)
avg=sum(Flattend)/p
print(avg)


#Dictionary Aggregation – Total Salary Per Department
employees = [
    {"name": "Aman", "dept": "AI", "salary": 50000},
    {"name": "Riya", "dept": "ML", "salary": 60000},
    {"name": "Karan", "dept": "AI", "salary": 70000},
    {"name": "Meena", "dept": "ML", "salary": 65000},
]

sorted_employees = sorted(employees, key=lambda x: (x["dept"]), reverse=True)
print(sorted_employees)
dept_salary={}
for i in employees:
    dept=i["dept"]
    salary=i["salary"]
    if dept in dept_salary:
        dept_salary[dept]+=salary
    else:
        dept_salary[dept]=salary

print(dept_salary)

#Dictionary of Lists – Group Words by First Letter
fruits= ["apple", "banana", "avocado", "blueberry", "apricot"]
grouped={}
print(fruits)

for i in fruits:
    first_letter= i[0]

    if first_letter not in grouped:
        grouped[first_letter]=[]
    grouped[first_letter].append(i)

print(grouped)



#Final Boss Question (Combined Everything)
data = [
    ("AI", "Aman", 50000),
    ("ML", "Riya", 60000),
    ("AI", "Karan", 70000),
    ("ML", "Meena", 65000),
    ("AI", "Rahul", 55000)
]


sorted_data = sorted(data, key=lambda x: (x[0]))
print(sorted_data)
groupe={}

for i in sorted_data:
    first_letter= i[0]

    if first_letter not in groupe:
        groupe[first_letter]=[]
    groupe[first_letter].append(i)

print(groupe)

