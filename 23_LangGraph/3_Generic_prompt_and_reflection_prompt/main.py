#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Resumo nas mãos do Usuário 
==========================
Neste Script uso FastAPI para mostrar a customização 
de PROMPTs e seguidamente o RESUMO do documento fornecido 
pelo Usuário.


Executar o script:
==================
$ uvicorn main:app --host 0.0.0.0 --port 8000
"""
from fastapi import FastAPI, UploadFile, File
import asyncio
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langgraph.graph import END, MessageGraph
from typing import List, Sequence
from langchain_community.document_loaders import UnstructuredFileLoader

# Transformar o PDF em texto com UnstructuredFileLoader:
def extract_text_with_langchain_pdf(pdf_file):
    loader = UnstructuredFileLoader(pdf_file)
    documents = loader.load()
    pdf_pages_content = '\n'.join(doc.page_content for doc in documents)
    return pdf_pages_content

# Modelo para os prompts:
from pydantic import BaseModel
class PromptUpdate(BaseModel):
    system_prompt: str


app = FastAPI(title='🤗 Usando FastAPI para SUMARIZAR documentos 🤗',
              version='1.0',
              description="""Data Scientist.: PhD. Eddy Giusepe Chirinos Isidro\n
              Projeto end-to-end para SUMARIZAÇÃO""")


# Inicializar prompts com valores Default:
default_prompt = """
Forneça um resumo do documento fornecido, evitando opiniões pessoais. \
O resumo deve cobrir os principais aspectos do documento original.
"""

default_reflection_prompt = """
Analise o resumo fornecido e faça as sugestões ou críticas para torná-lo mais claro, factual e informativo, mantendo-o conciso.
"""

current_prompt = default_prompt
current_reflection_prompt = default_reflection_prompt


"""Aqui começamos a usar o FastAPI:"""

# Endpoint para atualizar o prompt generate:
@app.post("/update-generate-prompt/")
async def update_generate_prompt(prompt_update: PromptUpdate):
    global current_prompt
    current_prompt = prompt_update.system_prompt
    return {"message": "Prompt generate atualizado com sucesso."}

# Endpoint para atualizar o prompt reflection:
@app.post("/update-reflection-prompt/")
async def update_reflection_prompt(prompt_update: PromptUpdate):
    global current_reflection_prompt
    current_reflection_prompt = prompt_update.system_prompt
    return {"message": "Prompt reflection atualizado com sucesso."}

# Endpoint para processar o PDF em formato Binário:
@app.post("/PDF-document-summary/")
async def process_pdf(file: UploadFile = File(...)):
    file_location = f"/tmp/{file.filename}" # Geramos um arquivo temporário para salvar o PDF
    with open(file_location, "wb") as f:
        f.write(file.file.read())

    text = extract_text_with_langchain_pdf(file_location)

    # Usamos os PROMPTs Atualizados:
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", current_prompt),
            MessagesPlaceholder(variable_name="text"),
        ]
    )

    reflection_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", current_reflection_prompt),
            MessagesPlaceholder(variable_name="text"),
        ]
    )

    # Instanciar o modelo LLM:
    llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0, streaming=True) # "gpt-4o"   ou    "gpt-3.5-turbo-0125"

    # Crio o objeto de geração:
    generate = prompt | llm
    # Crio o objeto de Refletir:
    reflect = reflection_prompt | llm
    
    # Criar a função de geração de nós:
    async def generation_node(state: Sequence[BaseMessage]):
        return await generate.ainvoke({"text": state})

    # Criar a função de reflexão:
    async def reflection_node(messages: Sequence[BaseMessage]) -> List[BaseMessage]:
        # Outras mensagens que precisamos ajustar:
        cls_map = {"ai": HumanMessage, "human": AIMessage}

        # A primeira mensagem é a solicitação original do usuário. Mantemos o mesmo para todos os nós:
        translated = [messages[0]] + [
            cls_map[msg.type](content=msg.content) for msg in messages[1:]
        ]
        res = await reflect.ainvoke({"text": translated})

        # Isso será tratado como um feedback para o gerador:
        return HumanMessage(content=res.content)

    # Criar o grafo de mensagens:
    builder = MessageGraph()
    builder.add_node("generate", generation_node)
    builder.add_node("reflect", reflection_node)
    builder.set_entry_point("generate")

    # Definir a condição para parar a geração:
    def should_continue(state: List[BaseMessage]):
        if len(state) > 3:
            return END
        return "reflect"

    # Adicionar as condições de parada:
    builder.add_conditional_edges("generate", should_continue)
    builder.add_edge("reflect", "generate")

    # Compilar o grafo:
    graph = builder.compile()

    # Função para gerar respostas:
    async def stream_responses():
        # last_content = None
        async for event in graph.astream([HumanMessage(content=text)]):
            if 'generate' in event:
                last_content = event['generate'].content # Armazena o 'content' da mensagem 'generate'
        return last_content

    result = await stream_responses()
    return {"Resumo do Documento": result}




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
