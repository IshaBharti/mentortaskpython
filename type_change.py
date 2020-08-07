import types
k = 5.6
if(type(k)==types.IntType):
   print "int"
elif (type(k)==types.FloatType):
   print "float"
elif(type(k)==types.StringType):
   print "string"
else:
   print "complex"

