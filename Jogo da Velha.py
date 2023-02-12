#Criando o tabuleiro usando a função de listas:
linha1 = ['-', '-', '-']
linha2 = ['-', '-', '-']
linha3 = ['-', '-', '-']

#Definindo como o tabuleiro será mostrado:
def tabuleiro():
    print('')
    print(linha1)
    print(linha2)
    print(linha3)





#Definindo a função que verifica se o P1 venceu:
def check_win1():
    if linha1 == ['X', 'X', 'X']:
        print('P1 Venceu!!!')
        quit()
    if linha2 == ['X', 'X', 'X']:
        print('P1 Venceu!!!')
        quit()
    if linha3 == ['X', 'X', 'X']:
        print('P1 Venceu!!!')
        quit()
    if linha1[0] == 'X' and linha2[1] == 'X' and linha3[2] == 'X':
        print('P1 Venceu!!!')
        quit()
    if linha1[0] == 'X' and linha2[0] == 'X' and linha3[0] == 'X':
        print('P1 Venceu!!!')
        quit()
    if linha1[1] == 'X' and linha2[1] == 'X' and linha3[1] == 'X':
        print('P1 Venceu!!!')
        quit()
    if linha1[2] == 'X' and linha2[2] == 'X' and linha3[2] == 'X':
        print('P1 Venceu!!!')
        quit()
    if linha1[2] == 'X' and linha2[1] == 'X' and linha3[0] == 'X':
        print('P1 Venceu!!!')
        quit()
    if linha1[2] == 'X' and linha2[1] == 'X' and linha3[0] == 'X':
        print('P1 Venceu!!!')
        quit()
    
#Definindo a função que verifica se o P2 venceu:
def check_win2():
    if linha1 == ['O', 'O', 'O']:
        print('P2 Venceu!!!')
        quit()
    if linha2 == ['O', 'O', 'O']:
        print('P2 Venceu!!!')
        quit()
    if linha3 == ['O', 'O', 'O']:
        print('P2 Venceu!!!')
        quit()
    if linha1[0] == 'O' and linha2[1] == 'O' and linha3[2] == 'O':
        print('P2 Venceu!!!')
        quit()
    if linha1[0] == 'O' and linha2[0] == 'O' and linha3[0] == 'O':
        print('P2 Venceu!!!')
        quit()
    if linha1[1] == 'O' and linha2[1] == 'O' and linha3[1] == 'O':
        print('P2 Venceu!!!')
        quit()
    if linha1[2] == 'O' and linha2[2] == 'O' and linha3[2] == 'O':
        print('P2 Venceu!!!')
        quit()
    if linha1[2] == 'O' and linha2[1] == 'O' and linha3[0] == 'O':
        print('P2 Venceu!!!')
        quit()
    if linha1[2] == 'O' and linha2[1] == 'O' and linha3[0] == 'O':
        print('P2 Venceu!!!')
        quit()

#Definindo a função de movimentos do P1: 
def move1():
    def func1(x):
      del linha1[x-7]
      linha1.insert(x-7, 'X')
    def func2(x):
      del linha2[x-4]
      linha2.insert(x-4, 'X')
    def func3(x):
      del linha3[x-1]
      linha3.insert(x-1, 'X')
    if x >= 7 and x <=9:
      func1(x)
    if x >= 4 and x <=6:
      func2(x)
    if x >= 1 and x <=3:
      func3(x)
    if x < 1 or x > 9:
      quit('error')

#Definindo a função de movimentos do P2: 
def move2():
    def func1(y):
      del linha1[y-7]
      linha1.insert(y-7, 'O')
    def func2(y):
      del linha2[y-4]
      linha2.insert(y-4, 'O')
    def func3(y):
      del linha3[y-1]
      linha3.insert(y-1, 'O')
    if y >= 7 and y <=9:
      func1(y)
    if y >= 4 and y <=6:
      func2(y)
    if y >= 1 and y <=3:
      func3(y)
    if y < 1 or y > 9:
      quit('error')
    

#Anexando a jogada com o display do tabuleiro e checagem de vitória:
def movement1():
    move1()
    tabuleiro()
    check_win1()
    
def movement2():
    move2()
    tabuleiro()
    check_win2()

#Criando a ordem de jogadas:
tabuleiro()
x = int(input('P1\n\n>'))
movement1()
y = int(input('P2\n\n>'))
movement2()
x = int(input('P1\n\n>'))
movement1()
y = int(input('P2\n\n>'))
movement2()
x = int(input('P1\n\n>'))
movement1()
y = int(input('P2\n\n>'))
movement2()
x = int(input('P1\n\n>'))
movement1()
y = int(input('P2\n\n>'))
movement2()
x = int(input('P1\n\n>'))


#Checando as posições caso esgotem os espaços:
if not linha1 == ['-', '-', '-'] or linha2 == ['-', '-', '-'] or linha3 == ['-', '-', '-']:
    print('Deu velha!')
    exit()



