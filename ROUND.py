import ply.lex as lex
import ply.yacc as yacc
# import mysql.connector 
# mydb = mysql.connector.connect(host="localhost", user= "root", password= "admin@123", database= "akku")

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
    'database':'DATABASE1'
    
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
    '''declaration  : SELECT ROUND LPAREN NUM DECIMAL NUM COMMA NUM RPAREN SEMICOLON
                    | SELECT ROUND1 LPAREN NUM DECIMAL NUM COMMA NUM RPAREN SEMICOLON
                    | SELECT1 ROUND LPAREN NUM DECIMAL NUM COMMA NUM RPAREN SEMICOLON
                    | SELECT1 ROUND1 LPAREN NUM DECIMAL NUM COMMA NUM RPAREN SEMICOLON
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
    # cur = mydb.cursor() 
    # cur.execute(s) 
    # data=cur.fetchall()
    # print(data)
    # mydb.close()