from __future__ import print_function
import ply.yacc as yacc
import os
import sys
from lexer import tokens

status = {
    'indentation': 0,
    'type': '',
    'parentType': '',
    'first': False,
    'initial': True
}

def p_initial(p):
    'initial : value'

def p_value_lasttype(p):
    '''value : STRING
             | NUMBER
             | TRUE
             | FALSE
             | NULL
    '''
    global status
    if status['type'] == 'array':
        if not status['first']:
            printIndentation()
        print("- ",end='')
    print(p[1])

def p_value_object(p):
    'value : saveStatusBeforeObject object'
    global status
    status = p[1]

def p_value_array(p):
    'value : saveStatusBeforeArray array'
    global status
    status = p[1]

def p_object_empty(p):
    'object : LLLAVE RLLAVE'
    print('{}')

def p_object_members(p):
    'object : LLLAVE printBeforeObjectNotEmpty members RLLAVE'

def p_members_one(p):
    'members : pair'

def p_members_multiple(p):
    'members : pair COMA members'

def p_pair(p):
    'pair : STRING printString DOSPUNTOS value'

def p_array_empty(p):
    'array : LCORCHETE RCORCHETE'
    print('[]')

def p_array_elements(p):
    'array : LCORCHETE printBeforeArrayNotEmpty elements RCORCHETE'

def p_elements_one(p):
    'elements : value'

def p_elements_multiple(p):
    'elements : value COMA setNotFirst elements'


def p_printString(p):
    'printString :'
    global status
    string = p[-1]
    stringAux = string.replace(' ', '')
    if stringAux[1] != '-':
        string = string.replace('"', '')
    if not status['first']:
        printIndentation()
    print(string+": ",end='')
    status['first'] = False

def p_saveStatusBeforeObject(p):
    'saveStatusBeforeObject :'
    global status
    p[0] = {
        'indentation': status['indentation'],
        'type': status['type'],
        'parentType': status['parentType'],
        'first': status['first'],
        'initial': status['initial']
    }
    if not status['initial'] and not status['type'] == 'array':
        status['indentation'] += 1
    if status['type'] == 'array':
        printIndentation()
        print('- ', end='')
    status['first'] = True
    status['parentType'] = status['type']
    status['type'] = 'object'
    status['initial'] = False

def p_printBeforeObjectNotEmpty(p):
    'printBeforeObjectNotEmpty :'
    if status['parentType'] != 'array':
        print('')
        printIndentation()

def p_saveStatusBeforeArray(p):
    'saveStatusBeforeArray :'
    global status
    p[0] = {
        'indentation': status['indentation'],
        'type': status['type'],
        'parentType': status['parentType'],
        'first': status['first'],
        'initial': status['initial']
    }
    if status['type'] == 'array':
        if not status['first']:
            printIndentation()
        print('- ', end='')
    status['parentType'] = status['type']
    status['type'] = 'array'
    status['initial'] = False

def p_printBeforeArrayNotEmpty(p):
    'printBeforeArrayNotEmpty :'
    if status['parentType'] != 'array':
        print('')
        status['first'] = False
    else:
        status['first'] = True
    status['indentation'] += 1

def p_setNotFirst(p):
    'setNotFirst :'
    global status
    status['first'] = False

def p_error(p):
    print("Error de sintaxis!")
    exit(1)

def printIndentation():
    global status
    indentation = status['indentation']
    if status['type'] == 'array':
        indentation -= 1
    for i in range(indentation * 2):
        print(" ",end='')


parser = yacc.yacc()

arguments = len(sys.argv)
if(arguments == 3 and sys.argv[1]=="-f"):
    fileR = open(sys.argv[2],"r")
    orig_stdout = sys.stdout
    fileW = open("output.txt","w")
    sys.stdout = fileW
    s = fileR.read()
    result = parser.parse(s)
    sys.stdout = orig_stdout
    fileR.close()
    fileW.close()
elif(arguments == 1):
    try:
       s = input('json > ')
    except EOFError:
        print("Error in call")
    if s:
        result = parser.parse(s)

else:
    print("Error in call")
