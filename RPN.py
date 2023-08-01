
import os           
path= os.path.realpath(os.path.join(os.getcwd(),          #getting file path
os.path.dirname('input_RPN_EC.txt')))
file = open(os.path.join(path, 'input_RPN_EC.txt'))       #opening input file
count=1
operators = set(['+', '-', '*', '/', '(', ')','%'])       # set of operators
precedence = {'+':1, '-':1, '*':2, '/':2, '%':2}          # setting up precedence 
def convert(expression):                                  #converting algebraic expression
    items = []                                           
    finalexp = ''                                           
    for i in expression:
        if i not in operators:                            # checking for operands
            finalexp+= i
        elif i=='(':                                     # checking for operators
            items.append('(')
        elif i==')':
            while items and items[-1]!= '(':
                finalexp+=items.pop()
            items.pop()
        else:   
            while items and items[-1]!='(' and precedence[i]<=precedence[items[-1]]:    # checking priority  
                finalexp+=items.pop()                                                   # putting items in finalexp
            items.append(i)
    while items:
        finalexp+=items.pop()
    return finalexp
for i in file:                                            #progressing line-by-line 
  expression = i
  print('(',count,')','Algebraic: ',expression)
  count=count+1
  q=convert(expression)
  print('  ','RPN: ',q)
  arr=list(q)