
n=int(input())
l=[]
def get_key_with_highest_value(dictionary):
    max_key = None
    max_value = None
    
    for key, value in dictionary.items():
        if max_value is None or value > max_value:
            max_key = key
            max_value = value
    
    return max_key
for i in range(n):
    a=input()
    l.append(a)
for i in l:
    d={}
    for j in i:
        if j!=" ":
            if j not in d.keys():
                d[j]=1
            else:
                d[j]+=1
    result = get_key_with_highest_value(d)
    if result!='i':
        print(result.upper(),end="\n")
    else:
        print(chr(ord(result.upper())-2),end="")

