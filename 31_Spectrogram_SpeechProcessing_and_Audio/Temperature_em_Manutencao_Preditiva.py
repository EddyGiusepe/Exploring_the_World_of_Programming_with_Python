import random
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Simulação de leituras de temperatura ao longo do tempo
def gerar_dados_temperatura(dias, temp_inicial, taxa_aumento):
    tempo = np.arange(dias)
    temperatura = temp_inicial + taxa_aumento * tempo + np.random.normal(0, 2, dias)
    return tempo, temperatura

# Parâmetros
dias_simulacao = 30
temperatura_inicial = 25
taxa_aumento_diaria = 0.5

# Gerar dados
tempo, temperatura = gerar_dados_temperatura(dias_simulacao, temperatura_inicial, taxa_aumento_diaria)

# Criar e treinar o modelo
modelo = LinearRegression()
modelo.fit(tempo.reshape(-1, 1), temperatura)

# Fazer previsões
dias_futuros = np.arange(dias_simulacao, dias_simulacao + 10)
previsoes = modelo.predict(dias_futuros.reshape(-1, 1))

# Definir limite de temperatura
limite_temperatura = 40

# Encontrar o dia previsto para ultrapassar o limite
dia_manutencao = next((dia for dia, temp in zip(dias_futuros, previsoes) if temp > limite_temperatura), None)

# Visualização
plt.figure(figsize=(10, 6))
plt.scatter(tempo, temperatura, label='Dados reais')
plt.plot(dias_futuros, previsoes, color='red', label='Previsão')
plt.axhline(y=limite_temperatura, color='green', linestyle='--', label='Limite de temperatura')
plt.xlabel('Dias')
plt.ylabel('Temperatura (°C)')
plt.title('Previsão de Manutenção Baseada na Temperatura')
plt.legend()

if dia_manutencao:
    plt.annotate(f'Manutenção necessária no dia {dia_manutencao}', 
                 xy=(dia_manutencao, limite_temperatura),
                 xytext=(dia_manutencao-5, limite_temperatura+5),
                 arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()

print(f"Manutenção prevista para o dia {dia_manutencao}" if dia_manutencao else "Não há necessidade de manutenção nos próximos 10 dias.")
