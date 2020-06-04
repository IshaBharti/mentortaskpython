mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
replacementStr = "on"





x =["the quick brown fox jumped over the lazy dog. the dog slept over the verandah."]
n = 0
for i in x:
    x[n] = i.replace('over',' on')
    n += 1
    print (x)
