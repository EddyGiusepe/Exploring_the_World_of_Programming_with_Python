#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

=================================
Agente RAG e pesquisa na Internet
=================================

Tutorial baseado no GitHub ---> https://github.com/Shubhamsaboo/awesome-llm-apps?utm_source=www.theunwindai.com&utm_medium=referral&utm_campaign=build-an-ai-rag-agent-with-web-access-using-gpt-4o

Install
=======
$ pip install phidata   ---> Phidata é uma estrutura para construção de sistemas de agentes.
$ pip install lancedb
"""
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.embedder.openai import OpenAIEmbedder
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.lancedb import LanceDb, SearchType
from phi.playground import Playground, serve_playground_app
from phi.tools.duckduckgo import DuckDuckGo


import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
#openai.api_key  = os.environ['OPENAI_API_KEY']
#Eddy_key_openai  = os.environ['OPENAI_API_KEY']
#from openai import OpenAI
#client = OpenAI(api_key=Eddy_key_openai)

db_uri = "tmp/lancedb"

# Crie uma base de conhecimento a partir de um PDF:
knowledge_base = PDFUrlKnowledgeBase(urls=["https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf"], #"https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"
                                     # Use LanceDB como banco de dados vetorial:
                                     vector_db=LanceDb(table_name="paper-of-Attention",
                                                       uri=db_uri,
                                                       search_type=SearchType.vector,
                                                       distance="cosine",
                                                       embedder=OpenAIEmbedder(model="text-embedding-3-small")
                                                      ),
                                    )

# Carregar a base de conhecimento: Comente após a primeira execução:
knowledge_base.load(upsert=True)

rag_agent = Agent(
    model=OpenAIChat(id="gpt-4o-2024-08-06"),
    agent_id="eddy-rag-search-agent",
    knowledge=knowledge_base, # Adicione a base de conhecimento ao agente
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
)

app = Playground(agents=[rag_agent]).get_app()



if __name__ == "__main__":
    serve_playground_app("rag_agent:app", reload=True)
    