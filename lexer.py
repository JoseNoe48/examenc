import ply.lex as lex
import difflib

# Lista de palabras reservadas
RESERVED = [
    'using',
    'namespace',
    'class',
    'static',
    'void',
    'program',
    'Main',
    'args',
    'Console',
    'writeline',
    'readline',
    'system'
    
]

# Lista de tokens
tokens = [
    'IDENTIFIER',
    'SYMBOL',
    'RESERVED',
    'BAD_RESERVED'
]

errores = []

# Expresión regular para identificadores y palabras reservadas
def t_RESERVED(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.lower() in RESERVED:
        t.type = 'RESERVED'
    elif difflib.get_close_matches(t.value.lower(), RESERVED, n=1, cutoff=0.7):
        t.type = 'BAD_RESERVED'
    else:
        t.type = 'IDENTIFIER'
    return t

# Expresión regular para símbolos
def t_SYMBOL(t):
    r'[^\s\w]'
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t\n'

# Contador de líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    errores.append(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()
