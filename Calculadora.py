print("\033[1:32m Este projeto, visa mostrar o funcionamento de uma 'Calculadora' com operações envolvendo 2(dois)números \nem cada vez, podendo-se realizar operações aritméticas como: Adição, Subtração, Multiplicação, e Divisão.\033[1:38m")
resultado = 0
continuar = 'Ss'
number3 = 0
cont = 0
number3 = 0
numero1 = float(input("Número: "))
operação = str(input("Operação: "))
numero2 = float(input("Número: "))
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
     numero3 = float(input("Número: "))
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

