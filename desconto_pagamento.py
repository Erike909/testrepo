# Exercícios

# Desconto e Pagamento

while True:
    print('Desconto e pagamento!')
    comando = input("Digite sim para iniciar e não para encerrar: ")
    if comando == 'não':
        print("Encerrado!")
        break
    if comando == 'sim':
        print("Iniciar programa!")
        valor_compra = float(input('Digite o valor de compra R$: '))
        if 0< valor_compra < 21:
            desconto = valor_compra * 0.05
            total_pago = valor_compra * (1 - 0.05)
            print('Desconto de %5.2f\nTotal pago pelo cliente: %5.2f' %
                  (desconto, total_pago))
        elif 20 < valor_compra < 51:
            desconto = valor_compra * 0.10
            total_pago = valor_compra * (1 - 0.10)
            print('Desconto de %5.2f\nTotal pago pelo cliente: %5.2f' %
                  (desconto, total_pago))
        elif 50 < valor_compra < 101:
            desconto = valor_compra * 0.15
            total_pago = valor_compra * (1 - 0.15)
            print('Desconto de %5.2f\nTotal pago pelo cliente: %5.2f' %
                  (desconto, total_pago))
        elif 100 < valor_compra < 1001:
            desconto = valor_compra * 0.20
            total_pago = valor_compra * (1 - 0.20)
            print('Desconto de %5.2f\nTotal pago pelo cliente: %5.2f' %
                  (desconto, total_pago))
        elif 1000 < valor_compra:
            desconto = valor_compra * 0.30
            total_pago = valor_compra * (1 - 0.30)
            print('Desconto de %5.2f\nTotal pago pelo cliente: %5.2f' %
                  (desconto, total_pago))
            

# Soma de pares e ímpares

while True:
    print("@@@@@@Soma de pares e Soma de ímpares@@@@@")
    comando = input("Digite sim para iniciar e não para encerrar: ")
    if comando == 'não':
        print("Encerrado!")
        break
    if comando == 'sim':
        numero = int(input('Digite o número de vendas: '))
        lista = range(1, numero + 1)
        lista_par = [ ]
        lista_impa = [ ]
        for elemento in lista:
            if elemento % 2 == 0:
                lista_par.append(elemento)
            else:
                lista_impa.append(elemento)
        soma_par = 0
        soma_impar = 0
        for par in lista_par:
            soma_par = soma_par + par
        for impa in lista_impa:
            soma_impar = soma_impar + impa
        print("Soma dos pares (SP): %d\nSoma dos ímpares (SI): %d" %
              (soma_par, soma_impar))


# Financiamento de um automóvel

# s = ((70-0)/7*1) + ((70-1)/2*7) + ((70-2)/3*7) + ... + ((70 - n + 1)/7*n

while True:
    print("Financiamento de um automóvel!")
    comando = input("Digite sim para iniciar e não para encerrar: ")
    if comando == 'não':
        print("Encerrado!")
        break
    if comando == 'sim':
        soma = 0
        n = int(input('Digite o valor do termo n: '))
        lista = range(1, n + 1)
        for i in lista:
            soma += ((70 - i + 1)/7*i)
        print("Financiamento para n = %d\nSoma: %5.2f" % (n, soma))
        
        
# Contagem e soma de pares e ímpares

while True:
    print("Contagem e soma de pares e ímpares!")
    comando = input("Digite sim para iniciar e não para encerrar: ")
    if comando == 'não':
        print("Encerrado!")
        break
    if comando == 'sim':
        lista = [ ]
        while True:
            numero = int(input("Digite um número ou 0 (zero) para encerrar: "))
            lista.append(numero)
            if numero == 0:
                break
        lista_par = [ ]
        lista_impar = [ ]
        for elemento in lista:
            if elemento % 2 == 0:
                lista_par.append(elemento)
            else:
                lista_impar.append(elemento)
        contagem_par = len(lista_par)
        contagem_impar = len(lista_impar)
        soma_par = 0
        soma_impar = 0
        for par in lista_par:
            soma_par += par
        for impar in lista_impar:
            soma_impar += impar
        print('Número de números pares: %d\nSoma de pares: %d\nNúmero de ímpares: %d\nSoma de ímpares: %d' %
              (contagem_par, soma_par, contagem_impar, soma_impar))
        

     
        

    
              

    




































            
        
