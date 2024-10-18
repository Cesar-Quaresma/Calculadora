print("\033[0:36m  Digite um número que corresponde com alguma Tabuada de sua preferência: ")


resp = ' '
while resp not in 'Nn':
    n = int(input("\033[0:33m Qual a Tabuada que você quer? "))
    for c in range(1, 11):
        print(f'\033[1:39m{n} \033[0:39mX \033[1:32m{c} \033[1:39m= \033[1:33m{n * c}')
    resp = str(input("\033[4:33mDeseja continuar?\033[0:39m ")).upper()