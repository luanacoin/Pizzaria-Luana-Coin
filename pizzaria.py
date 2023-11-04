from time import sleep
subtotal = 0
print('+++++++++++ Seja bem vindo a Pizzaria Luana Coin ++++++++++++')
while True:
    print('----------------------------Cardápio-------------------------')
    print('| Código  | Descrição  | Pizza Média (M) | Pizza Grande (G) |')
    print('|  21     | Napolitana |   R$ 20,00      |    R$ 26,00      |')
    print('|  22     | Margherita |   R$ 20,00      |    R$ 26,00      |')
    print('|  23     | Calabresa  |   R$ 25,00      |    R$ 32,50      |')
    print('|  24     | Toscana    |   R$ 30,00      |    R$ 39,00      |')
    print('-------------------------------------------------------------')
    sleep(1)
    while True:
        tam = input('Qual será o tamanho de pizza escolhido ? (M/G): ')
        if tam != 'M' and tam != 'G':
            print('Tamanho inválido para o pedido, escolha um da lista!')
        cod = input('Qual o código do sabor escolhido? ')
        if cod == '21':
            sabor = 'Napolitana'
            me = 20
            if tam == 'G':
              gr = 26
        elif cod == '22':
            sabor = 'Margherita'
            me = 20
            if tam == 'G':
              gr = 26
        elif cod == '23':
            sabor = 'Calabresa'
            me = 25
            if tam == 'G':
              gr = 32.5
        elif cod == '24':
            sabor = 'Toscana'
            me = 30
            if tam == 'G':
              gr = 39
        else:
            print('Código inválido para o pedido, escolha um da lista!')
            continue
        res = input('Você escolheu {}. Deseja pedir mais alguma pizza? (S/N): '.format(sabor))
        if tam == 'M':
            subtotal = subtotal + me
        if tam == 'G':
          subtotal = subtotal + gr
        if res == 'S':
            continue
            if res == 'N':
              print('O valor final é: {:.2f}.'.format(subtotal,))
        else:
            print('O valor final é: {:.2f}.'.format(subtotal,))
            break
