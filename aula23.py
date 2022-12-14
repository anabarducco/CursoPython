''' Tratamento de Erros e Exceções em Python
print(x) -> sem inicializar a variável, ocorre um erro/ uma exceção
no terminal aparece a exceção NameError
n = int(input('Digite um valor: ')) -> se for digitado um tipo diferente de int, ocorre a exceção de ValueError
ao dividir um número por 0, ocorre a exceção ZeroDivisionError, porque a matemática isso não pode acontecer
ao colocar um número entre '' numa expressão matemática, ocorre a exceção TypeError
ao tentar printar um elemento de uma lista num índice inexistente, ocorre a exceção IndexError
ao tentar importar um módulo e ele não for encontrado, ocorre a exceção ModuleNotFoundError

python exception list: lista de exceções python
todas as exceções tem 'Exception' como "pai"
para tratar uma exceção, utiliza-se o comando try-except

try:
    operação que pode dar problema
except:
    operação que acontece caso dê problema
else:
    operação que acontece caso a operação do try não dê problema
finally:
    operação que acontece independentemente de falhas

é possível ter blocos diferentes de except com diferentes tipos de falhas, e cada bloco fará uma operação diferente.
'''

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por 0.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}.')
else:
    print(f'O resultado da divisão {a}/{b} foi {r}.')
finally:
    print('Volte sempre! Muito obrigado!')