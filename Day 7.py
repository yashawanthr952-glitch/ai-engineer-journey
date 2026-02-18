#Frequency Counter with Ranking
nums = [4, 1, 2, 2, 3, 4, 4, 5, 1, 2, 3, 3, 3]
freq={}
for i in nums:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

print(freq)

s=sorted(freq.items(),key=lambda x: (-x[1],x[0]))
print(s)

#Smart Dictionary Merge
d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"b": 5, "c": 15, "d": 40}
merged={}
for k,v in d1.items():
    merged[k]=v

print(merged)
for k,v in d2.items():
    if k in merged:
        merged[k]+=v
    else:
        merged[k]=v

sorted_data = sorted(merged.items(), key=lambda x: -x[1])
result=dict(sorted_data)
print(result)


#Group Words Like Anagrams
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams={}
for i in words:
    key = "".join(sorted(i))

    if key not in anagrams:
        anagrams[key] = []
    
    anagrams[key].append(i)

result = list(anagrams.values())
result.sort(key=lambda x: -len(x))

print(result)


#Nested List Traversal (Deep Flatten)
data = [1, [2, 3], [4, [5, 6], 7], 8, [[9, 10], 11]]
Flattend=[]
for i in data:
    if isinstance(i,list):
        for j in i:
            if isinstance(j,list):
                for k in j:
                    Flattend.append(k)
            else:
                Flattend.append(j)
    else:
        Flattend.append(i)


print(Flattend)


#Remove Duplicates But Preserve Order
numss = [4, 5, 4, 6, 5, 7, 8, 7, 9]
nodup=[]

for i in numss:
    if i not in nodup:
        nodup.append(i)

print(nodup)
#First Non-Repeating Character
se = "aabbccddeffg"
for i in se:
    if se.count(i)==1:
        print(i)
        break


#Longest Subarray with Sum = K
nus = [1, 2, 3, -2, 5, -3, 1, 2]
k = 6


for i  in nus:
    i+=i
    if i ==k:
        break
    


#Custom Sorting by Frequency
ok=[5, 3, 5, 2, 2, 2, 4, 3,4,4]

freq2={}

for i in ok:
    if i in freq2:
        freq2[i]+=1
    else:
        freq2[i]=1

print(freq2)

lowest=sorted(freq2.items(),key=lambda x: (x[1],-x[0]) )
print(lowest)
result=[]
for num, count in lowest:
    result.extend([num] * count)

print(result)