import ply.lex as lex

# Reserved words
reserved = {
    'null': 'NULL'
}

# Tokens
tokens = [
    '',
] + list(reserved.values())

# Regexs
t_ASSIGN = r'='

# Functions


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t


def t_STRING(t):
    r'["\'].*["\']'
    t.value = t.value.strip('"').strip("'")
    return t


def t_DOUBLE(t):
    r'\d+\.\d+[e?\d+]*'
    t.value = float(t.value)
    return t


def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# New Line


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error token


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Ignore tokens
t_ignore_COMMENT = r'\/\/.*'
t_ignore = ' \t'

# Build lexer
lexer = lex.lex()

"""
lexer.input(f.read())

while True:
  tok = lexer.token()
  if not tok:
    break
  print(tok)
  
"""
