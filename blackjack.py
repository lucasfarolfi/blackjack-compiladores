import ply.lex as lex
import ply.yacc as yacc
import random as random

# --- TOKENS --- #
tokens = [
    'INT', 'ID', 'PLUS', 'MINUS', 'DIVIDE', 'MULTIPLY', 'EQUALS'
]

# --- OPERAÇÕES --- # 
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\='

# --- CARACTERES IGNORADOS --- #
t_ignore = r''

# --- VALIDAÇÕES COM REGEX --- #
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t): # Variáveis
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = 'ID'
    return t

def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)

lexer = lex.lex() # Recebe o analisador lexico responsável por ler os tokens

# Remove os warnings de shift/reduce conflicts do terminal
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE')
)

# Recebe dados na entrada do analisador lexico
# lexer.input("1+2")
# lexer.input("abc=123")

# --- Funções de Parser --- #
# Obs: Precisa escrever expression, empty corretamente, senão gera um erro no yacc
def p_calc(p):
    '''
    calc : E
         | empty
    '''
    print(run(p[1])) # Função que roda a expressão

def p_E(p):
    '''
    E : R EQUALS S
    '''
    
    # print('---------------')
    # print(f'E: {p[3]}')
    # print('---------------')
    p[0] = ('=', p[1], p[3])

def p_R(p):
    '''
    R : ID
    '''
    p[0] = p[1]

def p_S(p):
    '''
    S : L MINUS F
    '''
    # p2 = Operador
    # p1 = Primeira expressao
    # p3 = Segunda expressão

    # print('---------------')
    # print(f'S: {p[1]}, {p[2]}, {p[3]}')
    # print('---------------')
    p[0] = (p[2], p[1], p[3])

# --------
def p_F(p):
    '''
    F : F PLUS L
    '''
    p[0] = (p[2], p[1], p[3])

def p_F_L(p):
    '''
    F : L
    '''
    p[0] = p[1]

def p_L(p):
    '''
    L : INT
    '''
    p[0] = p[1]

# Quando caracteres inválidos são digitados
def p_error(p):
    print('Syntax error found!')

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

# Converte as expressões
parser = yacc.yacc()

env = {} # Guarda as variáveis

# Função que roda a expressão
def run(p):
    global env

    if type(p) == tuple: # Se for uma tupla, então é uma expressão

        #print(f'RUN: {p[1]} {p[0]} {p[2]}')
        if p[0] == '+':
            return run(p[1]) + run(p[2])
        elif p[0] == '-':
            return run(p[1]) - run(p[2])
        elif p[0] == '=':
            env[p[1]] = run(p[2]) # env['nome_variavel_p[1]'] = numero
            #print(env)
    else: # Se não for uma tupla de uma expressão, retorne apenas o valor existente
        return p

# Le todos os tokens
def main():
    buying_cards = True
    dealer_cards = []
    player_cards = []

    while sum(dealer_cards) < 17:
        dealer_cards.append(random.randint(2, 11))

    print("Cartas do Dealer: ", dealer_cards)       

    d_expression = 'dealer=21-'
    for i in range(len(dealer_cards)):
        if i == 0:
            d_expression += f'{dealer_cards[i]}'
        else:
            d_expression += f'+{dealer_cards[i]}'

    parser.parse(d_expression)

    player_cards.append(random.randint(2, 11))

    while buying_cards:
        print("\nSuas cartas: ", player_cards) 
        option = input('Deseja comprar mais cartas? (s/n): ')

        if option == 's':
            player_cards.append(random.randint(2, 11))
        elif option == 'n':
            buying_cards = False
            
            p_expression = 'player=21-'
            for i in range(len(player_cards)):
                if i == 0:
                    p_expression += f'{player_cards[i]}'
                    #print(f'p_expression: {p_expression}')
                else:
                    p_expression += f'+{player_cards[i]}'
                    #print(f'p_expression: {p_expression}')

            parser.parse(p_expression) # Vai chamar as funçoes de parser passando este input

            #print(f'ENV: {env}')
            print('\n------------------------------------------')
            print('Resultado:\n')

            if env['dealer'] < 0 and env['player'] < 0:
                print('A pontuação de ambos foi maior que 21. Ocorreu um empate!!!')
            elif env['dealer'] < 0 and env['player'] >= 0:
                print('A pontuação do Dealer foi maior que 21. Você ganhou!!!')
            elif env['dealer'] >= 0 and env['player'] < 0:
                print('A sua pontuação foi maior que 21. Você perdeu!!!')
            
            elif env['dealer'] < env['player']:
                print('A pontuação do dealer foi maior. Você perdeu!!!')
            elif env['dealer'] > env['player']:
                print('Sua pontuação foi maior que a do Dealer. Você ganhou!!!')
            elif env['dealer'] == env['player']:
                print('A pontuação de ambos é igual. Ocorreu um empate!!!')

            print('------------------------------------------')
            print('Total de cartas:\n')
            print(f'Pontuação do Dealer: {sum(dealer_cards)}')
            print(f'Sua pontuação: {sum(player_cards)}')
            print('------------------------------------------')
        else:
            print('Erro: Digite uma opção válida')

main()