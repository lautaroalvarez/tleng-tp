import ply.yacc as yacc
from lexer import tokens

indentation = 0

def p_initial(p):
    'initial : value'
    p[0]=p[1]
        

def p_value_lasttype(p):
    '''value : STRING
             | NUMBER
             | TRUE
             | FALSE
             | NULL
    '''
    print(p[1])
    p[0] = p[1]

def p_value_object(p):
    'value : object'
    p[0] = p[1]
    
def p_value_array(p):
    'value : array'
    p[0] = p[1]

def p_object_empty(p):
    'object : LLLAVE RLLAVE'
    print('{}')
    p[0] = "objeto vacio"

def p_object_members(p):
    'object : LLLAVE  members  RLLAVE'
    p[0] = p[2]    

def p_members_one(p):
    'members : pair'
    p[0] = p[1]

def p_members_multiple(p):
    'members : pair COMA members'
    p[0] = p[1]

def p_pair(p):
    'pair : STRING printString DOSPUNTOS value'
    p[0] = p[4]

def p_array_empty(p):
    'array : LCORCHETE RCORCHETE'
    print('[]')
    p[0] = "lista vacia"

def p_array_elements(p):
    'array : LCORCHETE indentationP elements RCORCHETE indentationM'
    p[0] = p[3]

def p_elements_one(p):
    'elements : printV value'
    p[0] = p[1]

def p_elements_multiple(p):
    'elements : printV value COMA elements'
    p[0] = p[1]


def p_printString(p):
    'printString :'
    string =p[-1]
    if string[0]!="-": 
        string = string.replace('"', '')     
    print(string+":",end='')

def p_indentation(p):
    'indentation :'
    
def p_indentationP(p):
    'indentationP :'
    global indentation
    indentation = indentation +1
    print()

def p_indentationM(p):
    'indentationM :'
    global indentation
    indentation = indentation -1

def p_printV(p):
    'printV :'
    for i in range(indentation*2):
        print(" ",end='')

def p_error(p):
    print("Error de sintaxis!")
    exit(1)



parser = yacc.yacc()

# while True:
#    try:
#        s = raw_input('json > ')
#    except EOFError:
#        break
#    if not s: continue
#    result = parser.parse(s)
#    print(result)
s = '{"a" :1,"c":[1,2,3],"b":[3,4,{ "n":[2,3,3]},3]}'
result = parser.parse(s)
print(result)
