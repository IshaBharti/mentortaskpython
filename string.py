m='The quick brown fox jump over the lazy dog'
rep='over'
rep1='on'
j=" "
a=m.split()
i=0
while i<len(a):
    if a[i]=="over":
        j=j+"on"+" "
    else:
        j=j+m+" "
    i=i+1
print(j)
        
