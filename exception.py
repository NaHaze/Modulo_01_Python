try:
    number = int(input("Digite o número a ser dividido: "))
    result = 10/number
except ValueError as e:
    print(f"Erro de value error: {e}")
    raise ValueError ("Tipo de variável incopatível com divisão!")
except Exception as e:
    print(f"Erro: {e}")
else:
    print(f"Resultado: {result}")
finally:
    print("Operação Finalizada")
