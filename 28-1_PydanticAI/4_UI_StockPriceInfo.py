#! /usr/bin/env python3
"""
Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Agente de busca de preço de ações
=================================
Aqui é criado uma interface gráfica para o usuário perguntar
sobre o preço de qualquer ação.

Intall
------
pip install pydantic-ai yfinance gradio

Run
---
uv run 4_UI_StockPriceInfo.py
"""
from pydantic_ai import Agent
from pydantic import BaseModel
import yfinance as yf
import gradio as gr

class StockPriceResult(BaseModel):
    symbol: str
    price: float
    currency: str = "USD"
    message: str

stock_agent = Agent(
    "groq:llama3-70b-8192",
    result_type=StockPriceResult,
    system_prompt="""Você é um assistente financeiro que pode buscar preços de ações.
                     Use a ferramenta get_stock_price para buscar dados atuais.
                  """
)

@stock_agent.tool_plain
def get_stock_price(symbol: str) -> dict:
    ticker = yf.Ticker(symbol)
    price = ticker.fast_info.last_price
    return {
        "price": round(price, 2),
        "currency": "USD"
    }

def get_stock_info(query):
    try:
        result = stock_agent.run_sync(query)
        response = f"Ação: {result.data.symbol}\n"
        response += f" Preço: ${result.data.price:.2f} {result.data.currency}\n"
        response += f"\n{result.data.message}"
        return response
    except Exception as e:
        return f"Erro: {str(e)}"

demo = gr.Interface(
    fn=get_stock_info,
    inputs=gr.Textbox(label="Pergunte sobre o preço de qualquer ação", placeholder="Qual o preço atual da ação da Apple?"),
    outputs=gr.Textbox(label="Informações da Ação"),
    title="Assistente de Preço de Ações",
    description="Pergunte sobre o preço de qualquer ação e eu buscarei as informações mais recentes para você!"
)

if __name__ == "__main__":
    demo.launch(share=True, debug=True)
