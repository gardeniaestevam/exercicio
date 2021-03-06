import random
from time import sleep

def pegar_tentativa(palavra, prox_letra):
    """

    Aqui testamos a tentiva do jogador, vemos se a letra está na palavra sorteada.
    """
    if prox_letra in palavra:
        print('{} está na palavra! '.format(prox_letra), flush=True)
        sleep(0.5)
        return True
    else:
        print('{} não está na palavra! '.format(prox_letra), flush=True)
        sleep(0.5)
        return False

def pegar_palavra_4_letras():
    arquivo = 'palavras4Letras.txt'
    with open(arquivo, 'r') as file:
        palavras = arquivo.readlines()
        p = random.choice(palavras)
    print(p)
    return p

def pegar_palavra_5_letras():
    pass

def pegar_palavra_6_letras():
    pass

def pegar_palavra_7_letras():
    pass

def pegar_palavra_8_letras():
    pass

def pegar_palavra_9_letras():
    pass

def pegar_palavra_10_letras():
    pass

def mostrar_palavra(palavra, acertos):
    """
    Printa a palavra mostrando apenas os caracteres que já foram adivinhados.
    """
    tam = len(palavra)
    x = '*' * tam
    for i in range(tam):
        if palavra[i] in acertos:
            print(f'{palavra[i]}', end = '')
        else:
            print(f'*', end = '')
    print('\n')

def pegar_prox_letra(tent):
    """
    Verifica se o que o usuário digitou é realmente uma letra e
    se está realmente na palavra
    """
    while True:
        try:
            prox_letra = input('Escolha a próxima letra: ')
        except (ValueError, TypeError):
            print('Tivemos um problema com o tipo de dado que você digitou. Por favor, digite um número!')
        except KeyboardInterrupt:
            print('Nenhum dado foi informado.')
        else:
            if prox_letra in tent:
                print('{} já foi escolhido antes, escolha outra letra!'.format(prox_letra))
            else:
                print('Verificando se {} está na palavra...'.format(prox_letra), flush=True)
                sleep(0.5)
                return prox_letra

def pegar_random_palavra(tam):
    """
    No início do jogo, essa função seleciona uma palavra aleatória
    a partir do arquivo com algumas palavras.
    Vai selecionando uma nova palavra até que ela seja do tamanho
    que o usuário deseja, assim que encontra uma palavra do tamanho
    desejado, retorna.

    entrada: tam - variável com o tamanho
    retoran: palavra
    """
    print(tam)
    if tam == 4:
        palavra = pegar_palavra_4_letras()
    if tam == 5:
        palavra = 'sagaz'
    if tam == 6:
        palavra = 'exceto'
    if tam == 7:
        palavra = 'empatia'
    if tam == 8:
        palavra = 'inerente'
    if tam == 9:
        palavra = 'perspicaz'
    if tam == 10:
        palavra = 'prescindir'
    return palavra

print(30 * '-', flush=True)
sleep(0.5)
print('Vamos brincar de forca!', flush=True)
sleep(0.5)
print(30 * '-', flush=True)
sleep(0.5)

while True:
    try:
        tentativas = int(input('Quantas tentativas você deseja ter? [1-25] ')) #número de tentativas que o jogador vai ter
    except (ValueError, TypeError):
        print('Tivemos um problema com o tipo de dado que você digitou. Por favor, digite um número!')
    except KeyboardInterrupt:
        print('Nenhum dado foi informado.')
    else:
        if tentativas < 1 or tentativas > 25:
            print('Por favor, insira um número dentro do intervalo desejado! ')
            continue
        else:
            break

while True:
    try:
        tam = int(input('Qual o tamanho mínimo da palavra? [4-10] ')) #tamanho mínimo da palavra
    except (ValueError, TypeError):
        print('Tivemos um problema com o tipo de dado que você digitou. Por favor, digite um número!')
    except KeyboardInterrupt:
        print('Nenhum dado foi informado.')
    else:
        if tam < 4 or tam > 10:
            print('Por favor, insira um número dentro do intervalo desejado! ')
            continue
        else:
            break

print(30 * '-', flush=True)
sleep(0.5)
print('Escolhendo uma palavra...', flush=True)
sleep(0.5)
palavra = pegar_random_palavra(tam)
print(30 * '-', flush=True)
sleep(0.5)

tent = []
acertos = []
round = 0
while (tentativas != 0):
    mostrar_palavra(palavra, acertos)
    print('Tentativas que restam: {}'. format(tentativas))
    if round == 0:
        print('Nenhuma tentativa precedente!')
    else:
        print('Tentativa precedente: {}'.format(tent[round - 1]))
    prox_letra = pegar_prox_letra(tent)
    tent.append(prox_letra)
    if pegar_tentativa(palavra, prox_letra) == True:
        acertos.append(prox_letra)
    if len(acertos) == len(palavra):
        print(palavra)
        print('Parabéns, você adivinhou a palavra!', flush=True)
        sleep(0.5)
        print(30 * '-')
        print('Fim de jogo!', flush=True)
        sleep(0.5)
        print(30 * '-')
        break
    tentativas = tentativas - 1
    round = round + 1
    if tentativas == 0:
        print('Você perdeu! ', flush=True)
        sleep(0.5)
        print(30 * '-')
        print('A palavra era {}'.format(palavra))
        print('Fim de jogo!', flush=True)
        sleep(0.5)
        print(30 * '-')
        break

