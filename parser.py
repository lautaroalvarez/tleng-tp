import ply.yacc as yacc
from lexer import tokens

def p_initial(p):
    'initial : value'
    p[1] = {
        "identacion": ''
    }

def p_value_lasttype(p):
    '''value : STRING
             | NUMBER
             | TRUE
             | FALSE
             | NULL
    '''
    print p[1]

def p_value_object(p):
    'value : object'
    p[1] = {
        "identacion": p[0].identacion
    }

def p_value_array(p):
    'value : array'
    p[1] = {
        "identacion": p[0].identacion
    }

def p_object_empty(p):
    'object : LLLAVE RLLAVE'
    print '{}'

def p_object_members(p):
    'object : LLLAVE members RLLAVE'
    p[1] = {
        "identacion": p[0].identacion
    }

def p_members_one(p):
    'members : pair'

def p_members_multiple(p):
    'members : pair COMA members'

def p_pair(p):
    'pair : STRING DOSPUNTOS value'
    print p[1] + ' : '

def p_array_empty(p):
    'array : LCORCHETE RCORCHETE'

def p_array_elements(p):
    'array : LCORCHETE elements RCORCHETE'

def p_elements_one(p):
    'elements : value'

def p_elements_multiple(p):
    'elements : value COMA elements'

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
