print("\033[1:32m  Este projeto, visa mostrar uma 'Calculadora' com operações envolvendo 2(dois) números de cada vez, \nhavendo a possibilidade de realizar operações matemáticas como: Adição, Subtração, Multiplicação, e \nDivisão, direcionada para números inteiros!\033[1:38m")
resultado = 0
continuar = 'Ss'
number3 = 0
cont = 0
number3 = 0
numero1 = int(input("Número: "))
operação = str(input("Operação: "))
numero2 = int(input("Número: "))
if operação in "+":
 resultado = numero1 + numero2
elif operação in "-":
 resultado = numero1 - numero2
elif operação in "*":
 resultado = numero1 * numero2
elif operação in "/":
 resultado = numero1 / numero2
print(f'{numero1} {operação} {numero2} = {resultado}.')
continuar = str(input("Deseja continuar? "))
while continuar in 'Ss':
     operação = str(input("Operação: "))
     numero3 = int(input("Número: "))
     number3 = number3 + numero3
     if operação in '+':
         cont = resultado + numero3
     elif operação in'-':
         cont = resultado - numero3
     elif operação in '*':
         cont = resultado * numero3
     elif operação in '/':
         cont = resultado / numero3
     print("{} {} {} = {}.".format(resultado, operação, numero3, cont))
     resultado = cont
     number3 = 0
     continuar = str(input("Deseja continuar? "))

