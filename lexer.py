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

t_STRING  = r'\"\"|\"[A-Za-z0-9]*\"' # Falta sacar los casos raros
t_NUMBER  = r'\d+' # Falta revisar casos raros
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
