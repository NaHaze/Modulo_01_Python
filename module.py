# Criação de um módulo personalizado
#import my_module --> quando importo assim, preciso passar junto com as fç. ex: message = my.module.salutation
from my_module import salutation, double

message = salutation("Nati")
double_result = double(5)
print(message)
print(f"O dobro de 5 é {double_result}")