#Projeto de Algebra Linear, nele faremos a pergunta do tipo de sistema(1x1, 2x2 ou 3x3) e faremos a
#solução por meio de determinantes(Regra de Cramer).

def tipo_sistema(sistema_tipo): #Função para determinar o tipo de sistema:
    if (sistema_tipo == 1):
        print('\t***Sistema 1x1***')
        print(f'aX = R')
        det1_1()

    elif (sistema_tipo == 2):
        print('\t***Sistema 2x2***')
        print(f'a[0]X b[0]Y = R[0]\na[1]X b[1]Y = R[1]')
        det2_2()

    elif (sistema_tipo == 3):
        print('\t***Sistema 3x3***')
        print(f'a[0]X b[0]Y c[0]Z = R[0]\na[1]X b[1]Y c[1]Z = R[1]\na[2]X b[2]Y c[2]Z = R[2]')
        det3_3()


def det1_1(): #Função Determinante 1x1:
    a = []
    R = []
    # Recebendo os números usados nos coeficientes da equação:
    aux = int(input(f'digite um número para x:'))
    a.append(aux)
    aux = int(input(f'digite um número para R:'))
    R.append(aux)
    print(f'{a[0]}X = {R[0]}')

    # Fazendo as operações:
    DetD = a[0]
    DetX = R[0]
    if (DetD != 0):
        x = DetX / DetD

        #Resultado:
        print(f'x = {x}')

    else:
        print('O determinante é igual a zero, ou seja, o sistema é indeterminado ou impossível!')

    input('')
    print('\n')

def det2_2(): #Função Determinante 2x2:
    a = []
    b = []
    R = []
    # Recebendo os números usados nos coeficientes da equação:
    for i in range(0, 2):
        aux = int(input(f'digite um número para x[{i+1}]:'))
        a.append(aux)
    for i in range(0, 2):
        aux = int(input(f'digite um número para y[{i+1}]:'))
        b.append(aux)
    for i in range(0, 2):
        aux = int(input(f'digite um número para o R[{i+1}]:'))
        R.append(aux)
    for i in range(0, 2):
       print(f'{a[i]}X  {b[i]}Y = {R[i]}')

    #Fazendo os Determinantes:
    DetD = (a[0] * b[1]) - (a[1] * b[0])
    if(DetD != 0):
        DetX = (R[0] * b[1]) - (R[1] * b[0])
        DetY = (a[0] * R[1]) - (a[1] * R[0])

        x = DetX / DetD
        y = DetY / DetD

        # Resultado:
        print(f'x = {x}')
        print(f'y = {y}')


    else:
        print('O determinante é igual a zero, ou seja, o sistema é indeterminado ou impossível!')

    input('')
    print('\n')

def det3_3(): #Função Determinante 3x3:
    a = []
    b = []
    c = []
    R = []
    # Recebendo os números usados nos coeficientes da equação:
    for i in range(0, 3):
        aux = int(input(f'digite um número para x[{i + 1}]:'))
        a.append(aux)
    for i in range(0, 3):
        aux = int(input(f'digite um número para y[{i + 1}]:'))
        b.append(aux)
    for i in range(0, 3):
        aux = int(input(f'digite um número para z[{i + 1}]:'))
        c.append(aux)
    for i in range(0, 3):
        aux = int(input(f'digite um número para o R[{i + 1}]:'))
        R.append(aux)
    for i in range(0, 3):
        print(f'{a[i]}X  {b[i]}Y {c[i]}Z = {R[i]}')

    # Fazendo os Determinantes:
    DetD = ((a[0] * b[1] * c[2]) + (b[0] * c[1] * a[2]) + (c[0] * a[1] * b[2])) - ((b[0] * a[1] * c[2]) + (a[0] * c[1] * b[2]) + (c[0] * b[1] * a[2]))
    if (DetD != 0):
        DetX = ((R[0] * b[1] * c[2]) + (b[0] * c[1] * R[2]) + (c[0] * R[1] * b[2])) - ((b[0] * R[1] * c[2]) + (R[0] * c[1] * b[2]) + (c[0] * b[1] * R[2]))
        DetY = ((a[0] * R[1] * c[2]) + (R[0] * c[1] * a[2]) + (c[0] * a[1] * R[2])) - ((R[0] * a[1] * c[2]) + (a[0] * c[1] * R[2]) + (c[0] * R[1] * a[2]))
        DetZ = ((a[0] * b[1] * R[2]) + (b[0] * R[1] * a[2]) + (R[0] * a[1] * b[2])) - ((b[0] * a[1] * R[2]) + (a[0] * R[1] * b[2]) + (R[0] * b[1] * a[2]))
        x = DetX / DetD
        y = DetY / DetD
        z = DetZ / DetD

        # Resultado:
        print(f'x = {x}')
        print(f'y = {y}')
        print(f'z = {z}')

    else:
        print('O determinante é igual a zero, ou seja, o sistema é indeterminado ou impossível!')

    input('')
    print('\n')

while True: #Loop para manter o programa rodando até desejar que ele pare:
    print('''*Tipos de Resolução de Sistema:*
    1 - Sistema por Determinante 1x1
    2 - Sistema por Determinante 2x2
    3 - Sistema por Determinante 3x3
    4 - Sair do Programa
    ''')
    sistema = input('Digite a opção que você deseja:')
    while sistema not in '1234':
        sistema = input('Digite a opção que você deseja:')

    if sistema == '4':
        print('\033[1;31mEncerrando...') #encerra o programa:
        break
    else:
        tipo_sistema(int(sistema)) #Chama a função para escolher o tipo de sistema: