def count_char(s1):
    count={}
    for ch in s1:
        if ch in count:
            count[ch]+=1
        else:
            count[ch]=1
    for k,v in count.items():
        print('{} : {}'.format(k,v))
vowels = ['a', 'e', 'i', 'o', 'u']
s1=input()
for c in s1:
    if c in vowels:
        s1 = s1.replace(c, "")
count_char(s1)
