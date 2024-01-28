import ply.lex as lex
import ply.yacc as yacc

dict = {
    'DESCRIBE':'DESCRIBE',
    'DESC':'DESC',
    'desc':'DESC1',
    'describe':'DESCRIBE1',
    'SELECT':'SELECT',
    'select':'SELECT1',
    'ROUND':'ROUND',
    'round':'ROUND1',
    'LENGTH':'LENGTH',
    'length':'LENGTH1',
    'MIN':'MIN',
    'min':'MIN1',
    'MAX':'MAX',
    'max':'MAX1',
    'DROP':'DROP',
    'drop': 'DROP1',
    'DATABASE':'DATABASE',
    'database':'DATABASE1',
    'TABLE':'TABLE',
    'table':'TABLE1'
    
}
tokens = ['ID','NUM','DECIMAL','SEMICOLON','LPAREN','RPAREN','COMMA','DQUOTE','SQUOTE'] + list(dict.values())

# Regular expressions for simple tokens
t_SEMICOLON = r'\;'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_DQUOTE = r'\"'
t_SQUOTE = r'\''
t_DECIMAL = r'.'
t_ignore = ' \t\n'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = dict.get(t.value, 'ID')
    return t

def t_NUM(t):
    r'[0-9][0-9]*'
    t.type = dict.get(t.value, 'NUM')
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()









def p_start(p):
    ' start : declaration '
    print("Valid declaration")


def p_declaration(p):
    '''declaration  : DROP DATABASE ID SEMICOLON
                    | DROP DATABASE1 ID SEMICOLON
                    | DROP1 DATABASE ID SEMICOLON
                    | DROP1 DATABASE1 ID SEMICOLON
                    | DROP TABLE ID SEMICOLON
                    | DROP TABLE1 ID SEMICOLON
                    | DROP1 TABLE ID SEMICOLON
                    | DROP1 TABLE1 ID SEMICOLON
                    | SELECT MAX LPAREN ID RPAREN SEMICOLON
                    | SELECT MAX1 LPAREN ID RPAREN SEMICOLON
                    | SELECT1 MAX LPAREN ID RPAREN SEMICOLON
                    | SELECT1 MAX1 LPAREN ID RPAREN SEMICOLON
                    | SELECT MIN LPAREN ID RPAREN SEMICOLON
                    | SELECT MIN1 LPAREN ID RPAREN SEMICOLON
                    | SELECT1 MIN LPAREN ID RPAREN SEMICOLON
                    | SELECT1 MIN1 LPAREN ID RPAREN SEMICOLON
                    | SELECT LENGTH LPAREN SQUOTE ID SQUOTE RPAREN SEMICOLON
                    | SELECT LENGTH1 LPAREN SQUOTE ID SQUOTE RPAREN SEMICOLON
                    | SELECT1 LENGTH LPAREN SQUOTE ID SQUOTE RPAREN SEMICOLON
                    | SELECT1 LENGTH1 LPAREN SQUOTE ID SQUOTE RPAREN SEMICOLON
                    | SELECT LENGTH LPAREN DQUOTE ID DQUOTE RPAREN SEMICOLON
                    | SELECT LENGTH1 LPAREN DQUOTE ID DQUOTE RPAREN SEMICOLON
                    | SELECT1 LENGTH LPAREN DQUOTE ID DQUOTE RPAREN SEMICOLON
                    | SELECT1 LENGTH1 LPAREN DQUOTE ID DQUOTE RPAREN SEMICOLON
                    | SELECT ROUND LPAREN NUM DECIMAL NUM COMMA NUM RPAREN SEMICOLON
                    | SELECT ROUND1 LPAREN NUM DECIMAL NUM COMMA NUM RPAREN SEMICOLON
                    | SELECT1 ROUND LPAREN NUM DECIMAL NUM COMMA NUM RPAREN SEMICOLON
                    | SELECT1 ROUND1 LPAREN NUM DECIMAL NUM COMMA NUM RPAREN SEMICOLON
                    | DESCRIBE ID SEMICOLON
                    | DESC ID SEMICOLON
                    | DESCRIBE1 ID SEMICOLON
                    | DESC1 ID SEMICOLON
    '''



def p_error(p):
    print("Syntax error")


parser = yacc.yacc()

while True:
    try:
        s = input("Enter: ")
    except EOFError:
        break
    if not s:
        continue
    parser.parse(s) 
