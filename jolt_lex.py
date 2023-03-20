# ------------------------------------------------------------
# Jolt Programming Language
#Jada Bailey & Garcian Mairs
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required

reserved = {
   'ef' : 'IF',
   'den' : 'THEN',
   'none' : 'ELSE',
   'efnot' : 'ELSEIF',
}

tokens = [
    #Literals
   'NUMBA',
   'DECI',
   'WUD',
   'LETTA',
   'WHICHEVA',

    #Arithmetic Operators
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'MODULUS',
   'INCREMENT',
   'DECREMENT',

    #Logical Operators
   'AND',
   'OR',
   'NOT',

   #Comparative/Conditional Operators
   'EQUAL',
   'NOT_EQUAL',
   'GREATER_THAN',
   'LESS_THAN',
   'GREATER_EQUAL',
   'LESS_EQUAL',

   #Symbols
   'ASSIGNMENT',
   'END_LINE',
   'COMMENT',
   'COLON',
   'OPENBRACE',
   'CLOSEBRACE',
   'DOUBLE_LESS',
   'DOUBLE_GREATER',
] + list(reserved.values())

#Regular Expressions for Tokens - Simple
t_INCREMENT  = r'\+\+'
t_DECREMENT  = r'\-\-'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_MODULUS  = r'%'


t_AND  = r'\@'
t_OR  = r'\|'
t_NOT  = r'\?'

t_EQUAL    = r'\=\='
t_NOT_EQUAL   = r'\?\='
t_GREATER_THAN  = r'\>'
t_LESS_THAN  = r'<'
t_GREATER_EQUAL  = r'\>='
t_LESS_EQUAL  = r'\<='

t_ASSIGNMENT    = r'\='
t_END_LINE   = r'\.'
t_COLON  = r':'
#t_COMMENT  = r'~.~*'  #'~.*~'  r'~.*~'
t_DOUBLE_LESS  = r'\<<'
t_DOUBLE_GREATER  = r'\>>'
t_OPENBRACE  = r'\('
t_CLOSEBRACE  = r'\)'

#Regular Expressions for Tokens - Functions
def t_DECI(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUMBA(t):
    r'([0-9]+)' 
    t.value = int(t.value)  
    return t

def t_LETTA(t):
    r'"([a-zA-Z]?)"'
    t.value = t.value
    return t

def t_WUD(t):
    #Starts & ends with a double quote
    # [^"\\] matches any character that is not a double quote or a backslash.
    # | is the alternation operator, which means "or".
    # \\. matches an escaped character (e.g., \" or \\).
    r'"([^"\\]|\\.)*"'
    t.value = t.value
    return t

def t_WHICHEVA(t):
    r'False' #Need to fix
    t.value = bool(t.value)
    return t

def t_COMMENT(t):
    r'~.*~'
    t.value = t.value
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

data = ''' False'''

#'''3.1'''
#check for 3 + 4 * 10 + - 20
#epr + term
#term + term
#factor + term
#factor + term
#factor + term * factor
#factor + factor * factor
#num + num+ num = syntax correct

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    #print(tok) #-prints token type, value, position
    print(tok.type,':', tok.value)


