import json
input= '{"Name":"Ram", "Class":"IV", "Age":9 }'
print(type(input))
a=json.loads(input)
print(a)
print(type(a))

