#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
class TemperatureConverter:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperatura abaixo do zero absoluto não é possível.")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @property
    def kelvin(self):
        return self._celsius + 273.15

# Uso da classe:
converter = TemperatureConverter(25)
print(f"Temperatura em Celsius: {converter.celsius}°C")
print(f"Temperatura em Fahrenheit: {converter.fahrenheit}°F")
print(f"Temperatura em Kelvin: {converter.kelvin}K")

# Mudando a temperatura
converter.celsius = 30
print(f"\nNova temperatura em Celsius: {converter.celsius}°C")
print(f"Nova temperatura em Fahrenheit: {converter.fahrenheit}°F")
print(f"Nova temperatura em Kelvin: {converter.kelvin}K")

# Tentando definir uma temperatura inválida
try:
    converter.celsius = -300
except ValueError as e:
    print(f"\nErro: {e}")