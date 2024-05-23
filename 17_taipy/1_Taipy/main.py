#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

* https://docs.taipy.io/en/latest/gallery/

* https://docs.taipy.io/en/latest/getting_started/

Taipy
=====
Aqui começamos usando a biblioteca Taipy.
Aqui criaremos um aplicativo que inclui um controle deslizante para ajustar um parâmetro, que
por sua vez afeta um gráfico de visualização de dados. Este exemplo demonstra como o Taipy 
pode ser usado para criar aplicativos web interativos e dinâmicos.

NOTA:
=====
As páginas Taipy podem ser definidas de várias maneiras: Markdown, Html ou Python. A página 
é criada por meio da API do Page Builder.

Executar o Script
=================
$ python main.py
"""
from taipy.gui import Gui 
import taipy.gui.builder as tgb
from math import cos, exp

value = 10

def compute_data(decay:int)->list:
    return [cos(i/6) * exp(-i*decay/600) for i in range(100)]

def on_slider(state):
    state.data = compute_data(state.value)

with tgb.Page() as page:
    tgb.text(value="# Meu primeiro gráfico com Taipy", mode="md")
    tgb.text(value="##### Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro", mode="md")
    tgb.text(value="Valor: {value}")
    tgb.slider(value="{value}", on_change=on_slider)
    tgb.chart(data="{data}") 
    

data = compute_data(value)



if __name__ == "__main__":
    Gui(page=page).run(title="Gráfico dinâmico")