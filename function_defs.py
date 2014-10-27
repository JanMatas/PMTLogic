import itertools
def sees (ch1,ch2,array):
    for i in range(0,len(array)):
        for j in range(0,len(array[i])):
            if array[i][j]==ch1:
                for k in range(0,len(array)):
                
                   if array[k][j]==ch2:
                        return True
                for l in range(0,len(array[i])):
                    if array[i][l]==ch2:
                        return True
def nextto (ch1,ch2,array):
  for i in range(0,len(array)):
            for j in range(0,len(array[i])):
                if array[i][j]==ch1:
                  if i>0:
                    if array[i-1][j]==ch2:
                        return True

		  if i<2:
                    if array[i+1][j]==ch2:
                        return True

                  if j<2:
                    if array[i][j+1]==ch2:
                        return True
                  if j>0:
                    if array[i][j-1]==ch2:
                        return True

  return False


def left (ch1,ch2,array):
    for i in range(0,len(array)):
        for j in range(0,len(array[i])):
            if array[i][j]==ch1:
              try:
                for m in range(0,j):
                    
                    for k in range(0,len(array)):
                        
                        if array[k][m]==ch2:
                            return True
              except:    
                raise
                return False
    return False
    
                        
def above (ch1,ch2,array):
    for i in range(0,len(array)):
        for j in range(0,len(array[i])):
            if array[i][j]==ch1:
              try:
                for m in range(0,i):
                    
                    for k in range(0,len(array[m])):
                        
                        if array[m][k]==ch2:
                            return True
              except:
                raise
                return False
    return False

def check(matrix):
    if not(sees("A","B",matrix) == (sees("B","C",matrix))):
      if not(nextto("B","D",matrix) or nextto ("B","E",matrix)):
        if  (left("F","A",matrix) and  above("A","F",matrix)):
            if not( (not(left ("D","E",matrix))) or (not(nextto("D","C",matrix))) or (not(sees("A","E",matrix)))):
                if not (not(sees("E","D",matrix) or sees("F","E",matrix)) or  not(above("E","B",matrix) == nextto("B","C",matrix))):
                    return True
      return False      

def generate():
    a = list(itertools.permutations("ABCDEF   ", 9))
    arrays= []
    for i in a:
        array=[]
        A,B,C,D,E,F,G,H,I = i
        row1 = [A,B,C]
        row2 = [D,E,F]
        row3 = [G,H,I]
        array.append(row1)
        array.append(row2)
        array.append(row3)
        arrays.append(array)
    return arrays
