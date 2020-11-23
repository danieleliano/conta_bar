def conta_bar():
  valor_valido = False
  while not valor_valido:
      consumo = float(input("Informe o valor total do consumo: "))
      if consumo >= 0:
        numero_pessoas_valido = False
        while not numero_pessoas_valido:
          pessoas = int(input("Informe o total de pessoas: "))
          if pessoas >= 0:
            taxa_valida = False
            while not taxa_valida:
              taxa = int(input("Informe o percentual do serviço, entre 0 e 100: "))
              if taxa >= 0 and taxa <= 100:
                valor_total = consumo + (consumo * (taxa * 0.01))
                valor_total_pessoa = (valor_total / pessoas)
                valor_total = str(valor_total)
                valor_total_pessoa = str(valor_total_pessoa)
                print(f"O valor total da conta, com a taxa de serviço, será de R$ {valor_total.replace('.' , ',')}")
                print(f"O valor que cada pessoa deverá pagar é: R$ {valor_total_pessoa.replace('.' , ',')}")
                taxa_valida = True
              else:
                print("Valor inválido")
            numero_pessoas_valido = True
          else:
            print("Número de pessoas errado! Digite novamente.")
        valor_valido = True
      else:
        print("Valor inválido! Digite novamente o consumo da mesa.")

conta_bar()