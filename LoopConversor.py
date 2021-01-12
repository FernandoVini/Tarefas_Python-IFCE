def printDecimal(x):
    numdecimal.append(x)

def printBinário(x):
    numbin.append(bin(x))

def printHexadecimal( x):
    numhexa.append(hex(x))

def printOctal(x):
    numoctal.append(oct(x))

def imprimirTabela():
    print("Decimal\tOctal\tHexadecimal\t Binario\n"
          "-------\t------\t-----------\t ------- \t ")
    for c in range(0, 226):
        printDecimal(c)
        printBinário(c)
        printHexadecimal(c)
        printOctal(c)
        print(f'{numdecimal[c]:>3}   {numoctal[c]: >6}    {numhexa[c]: >7}    {numbin[c]: >7}')

numdecimal = []
numbin = []
numhexa = []
numoctal = []

imprimirTabela()
