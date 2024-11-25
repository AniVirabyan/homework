#string 
#10.
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