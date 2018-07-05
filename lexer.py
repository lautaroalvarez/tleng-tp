import ply.lex as lex

tokens = (
   'STRING',
   'NUMBER',
   'TRUE',
   'FALSE',
   'NULL',
   'LCORCHETE',
   'RCORCHETE',
   'LLLAVE',
   'RLLAVE',
   'COMA',
   'DOSPUNTOS',
)

t_STRING  = r'\"([^"\\]+|\\(u[a-fA-F0-9]{4}|[\"\\\/bfnrt]))*\"'
t_NUMBER  = r'\-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?'
t_TRUE  = r'true'
t_FALSE  = r'false'
t_NULL  = r'null'
t_LCORCHETE  = r'\['
t_RCORCHETE  = r'\]'
t_LLLAVE  = r'\{'
t_RLLAVE  = r'\}'
t_COMA  = r'\,'
t_DOSPUNTOS  = r'\:'

t_ignore  = ' \t\n'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    exit(1)

lexer = lex.lex()
