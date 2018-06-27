from __future__ import print_function
import ply.yacc as yacc
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
    if string[0] != '-':
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

# while True:
#    try:
#        s = raw_input('json > ')
#    except EOFError:
#        break
#    if not s: continue
#    result = parser.parse(s)
#    print(result)

test1 = '''
{
    "a": [
        1,
        {
            "b": 2,
            "c": "asd",
            "d": []
        },
        [
            [3],
            4,
            [
                5,
                6,
                [
                    [7]
                ]
            ]
        ],
        8
    ]
}'''

test2 = '''
{
  "a" :1,
  "c":[1,2,3],
  "b":[3,4,{ "n":[2,3,3,{"o":{"p":"fgh"}}],"m":"a"},3],
  "d": {
    "a": 1,
    "b": "asd"
  }
}
'''

test3 = '''
["asd",0,[],{"a":{},"b":1},[1,2]]
'''

print('JSON:')
print(test3)
print('')
print('YAML:')
result = parser.parse(test3)
print('')
