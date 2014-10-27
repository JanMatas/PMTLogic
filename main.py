import sys
from function_defs import *

result=[]
for i in generate():
        if check (i):
            result.append(i)


result.sort()
result =list(result for result,_ in itertools.groupby(result))
for i in range(0,len(result)):
  
  print i
  print result[i][0][0]+" "+result[i][0][1]+" "+result[i][0][2]
  print result[i][1][0]+" "+result[i][1][1]+" "+result[i][1][2]
  print result[i][2][0]+" "+result[i][2][1]+" "+result[i][2][2]
  print "---"    
print len(result)


