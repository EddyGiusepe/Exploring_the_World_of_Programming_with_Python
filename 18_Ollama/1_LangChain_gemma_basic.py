#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


llm = Ollama(model="gemma",
             callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
             temperature=0
            )

llm.invoke("Fale-me sobre a cultura Peruana.")
