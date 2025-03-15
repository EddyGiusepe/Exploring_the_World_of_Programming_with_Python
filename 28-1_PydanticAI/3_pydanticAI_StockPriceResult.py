#! /usr/bin/env python3
"""
Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Agente de busca de preço de ações
=================================
pip install pydantic-ai yfinance gradio
"""
from pydantic_ai import Agent
from pydantic import BaseModel
import yfinance as yf


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
                  """,
)

"""
Símbolos de ações
=================
AAPL: Apple Inc.
MSFT: Microsoft Corporation
GOOGL: Alphabet Inc. (Google)
AMZN: Amazon.com Inc.
PETR4: Petrobras (ação preferencial na B3, bolsa brasileira)
VALE3: Vale S.A. (ação ordinária na B3)
"""


@stock_agent.tool_plain
def get_stock_price(symbol: str) -> dict:
    ticker = yf.Ticker(symbol)
    price = ticker.fast_info.last_price
    return {"price": round(price, 2), "currency": "USD"}


result = stock_agent.run_sync(
    "Qual o preço atual da ação da Google?"
)  # O Modelo de AI entende que deve procurar o símbolo GOOGL.
print(f"Preço da Ação: ${result.data.price:.2f} {result.data.currency}")
print(f"Mensagem: {result.data.message}")
