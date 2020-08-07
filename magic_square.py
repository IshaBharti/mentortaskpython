Iss list ko dekhein:

# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65, 76],
#     [95, 45, 78, 52, 49]
# ]

# Yeh kisi student ke peechle teen saal ke marks hai. Aap ko teeno saalo, ke sab subjects ke marks ka total calculate karna hai.

# Jaise uppar di hui nested list ka sum - 1142 aayega.


marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
    ]
sum = 0
i = 0
while i < len(marks):
    j = 0
    while j < len(marks[i]):
        sum = sum+marks[i][j]
        j = j+1
    i = i +1
print(sum)




	
	
	

