#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Enum on Python
==============
Imagine que você está desenvolvendo um sistema que lida com pedidos e que o status
de um pedido pode ser "pendente", "em processo", ou "completo". Você pode usar 
um Enum para representar esses estados de forma mais clara.
"""
# Exemplo 1:
from enum import Enum

class OrderStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    COMPLETED = 3

# Exemplo de uso:
def check_order_status(status):
    if status == OrderStatus.PENDING:
        return "O pedido está pendente."
    elif status == OrderStatus.PROCESSING:
        return "O pedido está em processamento."
    elif status == OrderStatus.COMPLETED:
        return "O pedido foi concluído."

# Testando a função
print(check_order_status(OrderStatus.PROCESSING))

print("\n")
# Exemplo 2:
from enum import Enum

class SectionType(str, Enum):
    HEADER = "header"
    FAILURES = "failures"
    SPECTRUM = "spectrum"
    AMPLITUDE = "amplitude"
    INSPECTION = "inspection"

# Exemplo de uso:
section = SectionType.HEADER

# Pode ser tratado como uma string:
print(section)            # Saída: header
print(section.upper())    # Saída: HEADER

# Também pode ser comparado como um enum:
if section == SectionType.HEADER:
    print("Seção é um HEADER")


print("\n")
# Exemplo 3:
from enum import Enum

class StatusCode(int, Enum):
    SUCCESS = 200
    NOT_FOUND = 404
    SERVER_ERROR = 500

# Exemplo de uso:
code = StatusCode.SUCCESS

# Pode ser tratado como um inteiro:
print(code)             # Saída: 200
print(code + 100)       # Saída: 300

# Comparação como enum:
if code == StatusCode.SUCCESS:
    print("Código indica sucesso")


print("\n")
# Exemplo 4:
from enum import Enum

class Measurement(float, Enum):
    LOW = 0.5
    MEDIUM = 1.0
    HIGH = 2.5

# Exemplo de uso:
measurement = Measurement.HIGH

# Pode ser tratado como um float:
print(measurement)             # Saída: 2.5
print(measurement * 2)         # Saída: 5.0

# Comparação como enum:
if measurement == Measurement.HIGH:
    print("Medição é alta")
