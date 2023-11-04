listProdutos = []


def cadastrarProduto(produto):
    print('Bem vindo ao Cadastro de produto\n')
    print(f'O código do seu produto é: 0{produto}\n')
    nome = input('Qual o nome do produto? \n')
    fabricante = input('Qual o nome do Fabricante do produto ?\n')
    valor = float(input('Qual o valor do produto?\n'))
    dicionarioProd = {'produto' : produto,
                      'nome' : nome,
                      'fabricante' : fabricante,
                      'valor' : valor}
    listProdutos.append(dicionarioProd.copy())

def consultarProduto():
    while True:
        try:
            consulta = int(input('Quais das opções de consulta você deseja?:\n1- Consultar todos os produtos\n2- Consultar produto por código\n3- Consultar produto por Fabricante\n4- Retornar\n'))
            if consulta == 1:
                print('Bem Vindo ao consultar todos os produtos')
                for produto in listProdutos:
                    for key,value in produto.items():
                        print(f'{key} : {value}')
            elif consulta == 2:
                print('Bem Vindo ao consultar por código')
                codigo = int(input('Digite o código do seu produto\n'))
                for produto in listProdutos:
                    if(produto['produto'] == codigo):
                        for key,value in produto.items():
                            print(f'{key} : {value}')
            elif consulta == 3:
                print('Bem Vindo ao consultar os produtos pelo Fabricante')
                entrada = input('Qual o nome do fabricante?\n')
                for produto in listProdutos:
                    if(produto['fabricante'] == entrada):
                        for key, value in produto.items():
                            print(f'{key} : {value}')
            elif consulta == 4:
                return
            else:
                print('Digite apenas o que deseja consultar')
                continue
        except ValueError:
            print('Pare de digitar Errado!')

def removerProduto():
    print('Bem Vindo ao Remover Produto')
    codigo = int(input('Digite o código do seu produto\n'))
    for produto in listProdutos:
        if (produto['produto'] == codigo):
            listProdutos.remove(produto)
            for key, value in produto.items():
                print(f'{key} : {value}')
            print('Foi removido!')




#programa inicial
print('Bem Vindo ao controle de estoque mercearia Luana Coin')
registroProduto = 0
while True:
    try:
        menu = int(input('Digite a opção desejada:\n1- Cadastrar produtos\n2- Consultar produto(s)\n3- Remover produto\n4- Sair\n'))
        if menu == 1:
            registroProduto += 1
            cadastrarProduto(registroProduto)
        elif menu == 2:
            consultarProduto()
        elif menu == 3:
            removerProduto()
        elif menu == 4:
            print('Programa finalizado!')
            break
        else:
            print('Digite apenas os número que consta no menu')
            continue
    except ValueError:
        print('Pare de digitar Errado!')
