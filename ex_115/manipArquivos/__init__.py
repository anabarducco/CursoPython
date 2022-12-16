def cadastrar():
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    arquivo = open('pessoas.txt', 'a')
    arquivo.write(f'Nome: {nome}\n')
    arquivo.write(f'Idade: {idade}\n')
    arquivo.close()


def listar():
    try:
        arquivo = open('pessoas.txt', 'r')
    except Exception as e:
        print(f'Não foi possível listar as pessoas cadasrtadas.\nErro encontrado: {e.__cause__}.')
    else:
        for linha in arquivo:
            print(linha)
        arquivo.close()
