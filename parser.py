import ply.yacc as yacc
from lexer import tokens

def p_value_lasttype(p):
    '''value : STRING
             | NUMBER
             | TRUE
             | FALSE
             | NULL
    '''
    p[0] = "tipo basico"

def p_value_object(p):
    'value : object'
    p[0] = p[1]

def p_value_array(p):
    'value : array'
    p[0] = p[1]

def p_object_empty(p):
    'object : LLLAVE RLLAVE'
    p[0] = 'arreglo'

def p_object_members(p):
    'object : LLLAVE members RLLAVE'
    p[0] = p[2]

def p_members_one(p):
    'members : pair'
    p[0] = p[1]

def p_members_multiple(p):
    'members : pair COMA members'
    p[0] = p[1]

def p_pair(p):
    'pair : STRING DOSPUNTOS value'
    p[0] = p[3]

def p_array_empty(p):
    'array : LCORCHETE RCORCHETE'
    p[0] = 'arreglo vacio'

def p_array_elements(p):
    'array : LCORCHETE elements RCORCHETE'
    p[0] = p[2]

def p_elements_one(p):
    'elements : value'
    p[0] = p[1]

def p_elements_multiple(p):
    'elements : value COMA elements'
    p[0] = p[1]

def p_error(p):
    print("Error de sintaxis!")
    exit(1)

parser = yacc.yacc()

while True:
   try:
       s = raw_input('json > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
