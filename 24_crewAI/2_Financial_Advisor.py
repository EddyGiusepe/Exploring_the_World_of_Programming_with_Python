#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Install:
=======
python = ">=3.10,<=3.13"
crewai = "0.28.8"
crewai_tools = "0.1.6"
langchain_community = "0.0.29"
duckduckgo-search = "^6.1.7"
"""

# 1. Definindo variávei de Ambiente: 
import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
#openai.api_key  = os.environ['OPENAI_API_KEY']
#Eddy_key_openai  = os.environ['OPENAI_API_KEY']
#from openai import OpenAI
#client = OpenAI(api_key=Eddy_key_openai)

# 2. Criando Tools:
from crewai_tools import FileReadTool, ScrapeWebsiteTool # Web Scraping: tool para ajudar a raspar dados do site de clientes em potencial
from langchain_community.tools import DuckDuckGoSearchRun # Search tools: para buscar conteúdo na internet que possa ser usado para escrever dicas de vendas.
# Criando ferramenta de pesquisa:
search_tool = DuckDuckGoSearchRun()
# Criando ferramenta de web scraping:
scrape_tool = ScrapeWebsiteTool()

# 3. Os Agentes e suas Tarefas:
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
# 3.1 Agente de Pesquisa da Empresa e a sua Tarefa
# Definimos o agente de pesquisa da empresa:
company_research_agent = Agent(
    role="Agente de pesquisa da empresa",
    goal="Reúna informações detalhadas sobre a empresa-alvo, incluindo seus negócios, produtos, serviços e posição no mercado.",
    backstory=(
        "Responsável por coletar dados abrangentes sobre clientes em potencial para informar o discurso de vendas."
    ),
    allow_delegation=True,
    llm=ChatOpenAI(model_name="gpt-3.5-turbo-0125", temperature=0.0),
    verbose=True
)

# Defina a tarefa para o agente de pesquisa da empresa:
company_research_task = Task(
    description=(
        "Colete dados abrangentes sobre {company_name} do site deles ({company_website}) e de outras fontes. "
        "Inclua detalhes sobre seus negócios, produtos, serviços e posição no mercado."
    ),
    expected_output=(
        "Relatório detalhado sobre os negócios, produtos, serviços e posição de mercado da {company_name}."
    ),
    agent=company_research_agent,
    tools=[search_tool, scrape_tool]
)

# 3.2 Agente e tarefa de análise de site (website)
# Definimos o Agente de Análise de Site (website):
website_analysis_agent = Agent(
    role="Agente de análise de sites",
    goal="Analise o site da empresa-alvo em busca de áreas de melhoria, incluindo design, desempenho e experiência do usuário.",
    backstory=(
        "Concentra-se na identificação de problemas específicos e oportunidades de melhoria no site do cliente."
    ),
    allow_delegation=True,
    llm=ChatOpenAI(model_name="gpt-3.5-turbo-0125", temperature=0.0),
    verbose=True
)

# Define the task for Website Analysis Agent
website_analysis_task = Task(
    description=(
        "Analise o site da {company_name} ({company_website}) para identificar áreas de melhoria no design, desempenho e experiência do usuário."
    ),
    expected_output=(
        "Relatório de análise detalhado destacando áreas de melhoria para o site da {company_name}, incluindo design, desempenho e experiência do usuário."
    ),
    agent=website_analysis_agent,
    tools=[scrape_tool, search_tool]
)

# 3.3 Agente de estratégia de conteúdo e tarefa
# Defina o Agente de Estratégia de Conteúdo:
content_strategy_agent = Agent(
    role="Agente de estratégia de conteúdo",
    goal="Desenvolva estratégias de conteúdo e identifique como o conteúdo aprimorado pode gerar engajamento e conversões.",
    backstory=(
        "Especializado na criação de uma narrativa e estratégia convincente para melhorias de conteúdo no site do cliente."
    ),
    allow_delegation=True,
    llm=ChatOpenAI(model_name="gpt-3.5-turbo-0125", temperature=0.0),
    verbose=True
)

# Definir a tarefa do Agente de Estratégia de Conteúdo:
content_strategy_task = Task(
    description=(
        "Desenvolva uma estratégia de conteúdo para o site da {company_name} ({company_website}) para melhorar o envolvimento do usuário e as taxas de conversão."
    ),
    expected_output=(
        "Estratégia de conteúdo abrangente para o site da {company_name}, incluindo recomendações para melhorias de conteúdo."
    ),
    agent=content_strategy_agent,
    tools=[search_tool, scrape_tool]
)

# 3.4 Agente de argumento de venda e tarefa
# Definimos o agente de argumento de venda:
sales_pitch_agent = Agent(
    role="Agente de vendas",
    goal="Crie um discurso de vendas personalizado e persuasivo para convencer a empresa-alvo a ter seu site modificado pelo 'Code With Prince'.",
    backstory=(
        "Combina pesquisa, análise e estratégia de conteúdo para criar um discurso de vendas atraente."
    ),
    allow_delegation=False,
    llm=ChatOpenAI(model_name="gpt-3.5-turbo-0125", temperature=0.0),
    verbose=True
)

# Definir a tarefa do Sales Pitch Agent:
sales_pitch_task = Task(
    description=(
        "Combine pesquisa, análise e estratégia de conteúdo para criar um discurso de vendas personalizado e persuasivo para {company_name}"
        "para convencê-los a ter seu site modificado pelo 'Code With Prince'."
    ),
    expected_output=(
        "Discurso de vendas personalizado para {company_name}, destacando os benefícios de ter seu site modificado pelo 'Code With Prince'."
    ),
    agent=sales_pitch_agent,
    tools=[search_tool, scrape_tool]
)

# 4. Criando o Crew:
# Iniciamos o Crew:
crew = Crew(
    agents=[
        company_research_agent, 
        website_analysis_agent,
        content_strategy_agent,
        sales_pitch_agent
    ],
    tasks=[
        company_research_task, 
        website_analysis_task,
        content_strategy_task,
        sales_pitch_task
    ],
    verbose=2,
    # Adicionamos memory e cache --> Isso ajuda a evitar que a equipe busque material já buscado.
    memory=True,
    cache=True # Armazenaremos em cache as saídas das Tools
)

# 5. Agora executamos:
inputs = {
    "company_name": "CrewAI",
    "company_website": "https://crewai.com"
}

# Executamos o kickoff:
result = crew.kickoff(inputs=inputs)
print("\n\n")
print(result)



# # Visualizando em markdown:
# from IPython.display import Markdown
# Markdown(result)