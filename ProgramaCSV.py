import csv
import matplotlib.pyplot as plt

while True:
    print(' 1- Criar arquivo\n 2- Ler arquivo\n 3- Mostrar gráfico\n 4- Sair do Programa\n')
    opt = input('escolha uma opção: ')
    if opt not in '1234':
        print('digite uma opção válida!\n')

    if opt == '1':
        x = int(input('digite o número de profissões que você deseja: '))

        f = open('tabela.csv', 'w', newline="")

        try:
            writer = csv.writer(f)
            writer.writerow(('profissao', 'salario'))
            for c in range(0, x):
                prof = input('escreva uma profissão: ')
                sal = float(input('digite o salário desta profissão: '))
                writer.writerow((prof, sal))

        finally:
            f.close()

    elif opt == '2':
        print('\n')
        try:
            print(open('tabela.csv', 'r').read())

        except:
            print('não foi possível encontrar o arquivo!')

    elif opt == '3':
        try:
            profissao = []
            salario = []

            f = open('tabela.csv', 'r')
            rec = csv.DictReader(f)

            for z in rec:
                profissao.append(z['profissao'])
                salario.append(float(z['salario']))
            try:
                plt.figure(figsize=(6, 6))

                plt.plot(profissao, salario)
                plt.show()

                plt.bar(profissao, salario)
                plt.show()

                fig1, ax1 = plt.subplots(figsize=(6, 6))
                ax1.pie(salario, labels=profissao, autopct='%1.1f%%', shadow=True, startangle=90)
                ax1.axis('equal')
                plt.show()

            finally:
                f.close()

        except:
            print('não foi possível encontrar o arquivo!')

    elif opt == '4':
        break

