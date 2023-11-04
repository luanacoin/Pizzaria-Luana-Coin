from datetime import datetime
def titulo(t):
    print(f'-' * (len(t) + 2))
    print(f'|{t:^{len(t)}}|')
    print(f'-' * (len(t) + 2))

def volumeFeijoada():
    while True:
        try:
            print('|-------MENU VOLUME DA FEIJOADA (ML)-------|\n>>')
            quant = int(input('Qual a quantidade que o pedido possui (ml)?: '))
            if quant < 300 and quant > 5000:
                print('Não aceitamos quantidades menores que 300 ml ou maiores que 5l. Tente Novamente')
                return 0.00
            elif (quant >= 300) and (quant <= 5000):
                print('O volume do seu pedido é de: {}'.format(quant))
                return 0.08
            else:
                print('Não aceitamos quantidades menores que 300 ml ou maiores que 5l. Tente Novamente!')
                continue
        except ValueError:
            print('Digite uma quantidade númerica aceitavel, tente novamente!')
            continue


def opcaoFeijoada():
    while True:
        op = input('\n|--------Escolha a sua Feijoada--------|\nB - BÁSICA (Feijão + paiol + costelinha)\nP - PREMIUM (Feijão + paiol + costelinha + partes de porco)\nS - SUPREMA (Feijão + paiol + costelinha + partes de porco + charque + calabresa + bacon)\n>>')
        if op == 'B':
            print('FEIJOADA BÁSICA - adicinado a seu pedido.')
            return 1.00
        elif op == 'P':
            print('FEIJOADA PREMIUM - adicinado a seu pedido.')
            return 1.25
        elif op == 'S':
            print('FEIJOADA SUPREMA - adicinado a seu pedido.')
            return 1.50
        else:
            print('Pedido inválido, escolha entre B, P ou  S')
            continue


def acompanhamentoFeijoada():
    while True:
        af = input('''\n|--------Qual acompanhamento para a feijoada?-------|\n|Código|----Opções de Acompanhamentos-----|  valor |
|  0   |-Não Desejo Mais Acompanhamentos--|R$  0,00|
|  1   |----------200G De Arroz-----------|R$  5,00|
|  2   |-----150G De Farora Especial------|R$  6,00|
|  3   |--------100G De Couve Flor--------|R$  7,00|
|  4   |----1(Uma) Laranja Descascada-----|R$  3,00|\n''')
        if af == '0':
            break
        elif af == '1':
            print('200g de arroz - adicinado a seu pedido.')
            return 5.00
        elif af == '2':
            print('150g de farofa especial - adicinado a seu pedido.')
            return 6.00
        elif af == '3':
            print('100g de couve cozida - adicinado a seu pedido.')
            return 7.00
        elif af == '4':
            print('laranja descascada - adicinado a seu pedido.')
            return 3.00
        else:
            print('Digite apenas o que consta na lista')
            continue



# Programa Inicial
print('++++Bem vindo ao Restaurante Luana Coin++++')
vol = volumeFeijoada()
ped = opcaoFeijoada()
acom = acompanhamentoFeijoada()
totValor = (vol * ped) + acom
pedidoFinal = []
valor = 0

while True:
    continuar = input('\nDeseja pedir mais alguma coisa (S/N) ?\n ')
    if continuar == 'N':
        print('Finalizando o seu pedido...\n')
        break
    elif continuar == 'S':
        adic = input('Deseja outra Feijoada ou Acompanhamento: \n')
        if adic == 'ACOMPANHAMENTO':
            print(acompanhamentoFeijoada())
        elif adic == 'FEIJOADA':
            print(opcaoFeijoada())
            continue
    else:
        print('Opção não encontrada,tente novamente')
        break

titulo(f'{"PEDIDO FINALIZADO":^50}')
titulo(f'TOTAL: R$ {totValor:.2f}')
titulo(f'DATA DO PEDIDO: {datetime.today().date().day}/{datetime.today().date().month}/{datetime.today().date().year}')
