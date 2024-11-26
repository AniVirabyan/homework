string 
10.
mstr=input()
print(mstr.replace(mstr[0],mstr[-1]))
# 12
mstr=input()
count=[]
tmp=mstr.split()
for el in tmp:
    if el not in count:
        count.append(el)
for el in count:
    print({el:tmp.count(el)})
    
# 27
mstr=input()
tmp= ' '
n=""
for el in mstr:
    if el!=tmp:
        n+=el
print(n)
#18
mstr=input()
if len(mstr)>3:
    print(mstr[0:3])
else:
    print(mstr)
#17
mstr=input()
tmp=mstr[-2:]
print(tmp*4)
#19
mstr=input()
print(mstr.rsplit("-",1)[0])
#29
def line_indentation(mstr, spaces):
    indentation = " " * spaces
    lines = mstr.splitlines()  
    if not lines:
        return ""
    else:
        lines[0] = indentation + lines[0]  
        return "\n".join(lines)  


print(line_indentation(
    mstr="""Это первая строка.
Это вторая строка.
А это третья строка""", 
    spaces=4
))
#42
def count_characters(mstr):
    count=[]
    result=[]
    for i in mstr:
        for el in count:
            if el[0]==i:
                el[1]+=1
                break
        else:
            count.append([i,1])
    for i in count:
        if i[1]==1:
            result.append((i[0],i[1]))
    return result
print(count_characters(mstr="udhshygygytttwdrdaf0l"))
#40
def reverse_words(mstr):
    ml=[]
    for el in mstr.split("\n "):
        line=" ".join(el.split()[::-1])
        ml.append(line)
    return "\n" .join(ml)
print(reverse_words(mstr="hello world yes"))
#47
def lower_n_chars(string,n):
    if n>len(string):
        return string.lower()
    return string[:n].lower()+string[n:]
print(lower_n_chars(string=("HELLO WORLD"),n=3))

#list
#7
ml=[23,45,78,23,45,12,78]
tmp=[]
for el in ml:
    if el not in tmp:
        tmp.append(el)
print(tmp)
#11
ml=[12,33,4,3]
ps=[23,37,3,7]
n=False  
for el in ml:
    if el  in ps:
        n=True
        break
print(n)
#22
num=[43,76,98]
print(num.index(98))
#31
ml=[12,23,45,67,89,100]
n=int(input())
m=int(input())
count=0
for el in ml:
    if n<=el<=m:
        count+=1
print(count)
#37
ml1=['go','ut','er','kl']
ml2=['ht','ut','go','mk']
mk=[]
for el in ml1:
    if el in ml2:
        mk.append(el)
         
        
print(mk)
#38
ml=[3,2,4,3,9,8]
for i in range(0,len(ml)-1,2):
    ml[i],ml[i+1]=ml[i+1],ml[i]

print(ml)
#39
#1-i tarberak
ml=["12","23","34"]
string=''
for el in ml:
    string+=el
print(string)
#2 tarberak
ml=["12","23","34"]
print(''.join(ml))
#23
def fllatten_list(ml):
    tmp=[]
    for el in ml:
        for i in el:
            tmp.append(i)
    return tmp
print(fllatten_list(ml=[[1,2],[43,87,6],[7,8],[8,76]]))
#47
def insert_element(ml,a):
    tmp=[]
    for el in ml:
        tmp.append(a)
        tmp.append(el)
    return tmp
print(insert_element(ml=["hello" , "world" ,"sos"] , a=2))
#46
def odd_digit(ml):
    tmp=[]
    for el in ml:
        if el%2==1:
            tmp.append(el)
    return tmp
print(odd_digit(ml=[12,33,22,45,6,9,78,99,77]))
#45
mstr = [[1, 2], [3, 4], [2, 5], [3, 1]]
tmp=set()
for el in mstr:
    for i in el:
        tmp.add(i)
sort_tmp=sorted(tmp)
print(sort_tmp)
#51
def split_list(lst, n):
    
    result = [lst[i:i+n] for i in range(0, len(lst), n)]
    return result
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
n = 3
result = split_list(my_list, n)
print(result)
#66
num = [[1, 2, 3], [4, 5, 1], [10, 11, 12], [7, 8, 9]]

try:
    
    result = max(num, key=sum)
    print("maximum amount", result)
except ValueError:
   
    print("empty list")
except TypeError:
    
    print("error in the list ")
#64
list1 = [1,2,]
list2 = ['a', 'b', "c"]

for i in range(max(len(list1), len(list2))):
    try:
        print(str(list1[i]) +" " + str(list2[i]))
    except IndexError:
        print("empty list")
#55
dict1=[{"a":2,"b":4},{"c":3,"a":5}]
remove_key=["a"]
for el in dict1:
    for i in remove_key:
        try:
            el.pop(i)
        except KeyError:
            print("Key not found")
print(dict1)
#42
list1=['first','second',23,76]
list2=['first',43,23]
set1=set(list1)
set2=set(list2)
diff1=set1-set2
diff2=set2-set2

print(diff1)
print(diff2)

dict
3
dict1={2:30,3:30}
dict2={'br':34,'gr':56}
b=dict1.keys()
c=dict2.keys()
b.extend(c)
print(b)
11
dict1={'df':23,'er':34}
b=sum(dict1.values())
print(b)
#7
d1={}
for i in range(1,16):
    d1[i]=i**2
print(d1)
#10
d1={"bi":34,"py":12}
ssum=sum(d1.values())
print(ssum)
#17
my_dict={
    'id1': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id2': {
        'name': ['David'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id3': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id4': {
        'name': ['Surya'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    }
}
result={}
for k,v in my_dict.items():
    if v not in  result.values():
        result[k]=v
print(result)
#15
def min_max_digit(dict1):
    max_digit=max(dict1.values())
    min_digit=min(dict1.values())
    return min_digit,max_digit
print(min_max_digit(dict1={"pu":97,"sos":54,"br":66}))
#18
def  dict_empty(dict1):
    
    return len(dict1) == 0


s_dict = {"boy":45}

if dict_empty(s_dict):
    print("The dictionary is empty.")
else:
    print("The dictionary is not empty.")
#23
def combine_values(dict1):
    dict2={}
    for el in dict1:
        for k,v in el.items():
            if v not in dict1:
                dict2[k]=[]
                dict2[k].append(v)
    return dict2
print(combine_values(dict1=[{"b":22,"a":32},{"c":87,"d":3}]))
#24
ml="goodapple233"
dictt={}
for el in ml:
    if el in dictt:
        dictt[el]+=1
    else:
        dictt[el]=1
print(dictt)
#32
dict={"Ara":{"class":"b"},"Bob":{"class":"c"}}
for el in dict:
    print(el)
    for i in dict[el]:
        print(i,":",dict[el][i])