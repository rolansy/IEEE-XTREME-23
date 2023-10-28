n=int(input())
def ccipher(t, s):
    r = ""

    for c in t:
        if c.isalpha():
            cup = c.isupper()
            c = c.lower()
            n = ord(c) + s - ord('a')
            n %= 26
            nc= chr(n + ord('a'))
            if cup:
                nc = nc.upper()
            r += nc
        else:
            r += c

    return  r
l=[]
for i in range(2):
    x=int(input())
    s=input()
    if "the" in s.split(" "):
        x*=-1
    l.append(ccipher(s,x))
for i in range(len(l)):
    print(l[i])