#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Este estudo foi baseado no maravilhoso trabalho de "Sven", um analista de 
dados da Alemanha.

Executar script
===============
$ pip install streamlit --upgrade
$ streamlit run app.py

Usando poetry:
==============
$ poetry run streamlit run app.py

OBSERVAÇÕES:
============

* Executar novamente quando você usar um theme diferente para o streamlit.
  Link de themes --> https://blog.streamlit.io/introducing-theming/

* O arquivo style.css é usado na parte de CONTATO (abaixo) 

"""
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My Website EddyGiusepe", page_icon="🤗", layout="wide")


# Criamos uma Função para carregar uma Animação:
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_DS = load_lottieurl("https://lottie.host/66e3ee32-a325-4f56-a68b-483b022b89c1/6VDmRz5c9B.json") # https://lottiefiles.com/search?category=animations&utm_source=search&utm_medium=platform&q=data+scientist
img_contact_form = Image.open("./images/eddy_linkedin.png")
img_lottie_animation = Image.open("./images/Artificial-Intelligence-Vs.-Machine-Learning-Vs.-Deep-Learning.jpg")


# Usando style (CSS local):
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("./style/style.css")


# Seção de cabeçalho:

with st.container():
    st.title("Olá, sou Eddy Giusepe")
    st.subheader("Sou Cientista de Dados")
    st.write("Sou apaixonado por transformar Dados (estruturados e não-estruturados) em insights. Como cientista de dados, minha missão é utilizar habilidades analíticas avançadas para extrair significado dos dados e assim ajudar na tomada de decisões estratégicas.")

    st.write("[Meu Linkedin](https://www.linkedin.com/in/eddy-giusepe-chirinos-isidro-85a43a42/)")


# O que eu faço:
with st.container():
    st.write("-----")

    left_column, right_column = st.columns(2)
    with left_column:
        st.header("O que eu faço:")
        st.write("##")
        st.write(
            """
            Como Cientista de Dados tenho usado as seguintes tecnologias/técnicas:

            * Uso os modelos pré-treinados do Hugging Face, da OpenAI, etc.
            * Conheço as técnicas de Machine Learning, Deep Learning e da Inteligência Artificial. 
            """
        )
        st.write("[Meu GitHub](https://github.com/EddyGiusepe)")
        st.write("[Meu Repositório Hugging Face](https://huggingface.co/EddyGiusepe)")

     
    with right_column:
        st_lottie(lottie_DS, height=300, key="Data Scientist", quality="high")



# Projetos:
with st.container():
    st.write("-----") 
    st.header("Meus Projetos")
    st.write("##")
    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(img_contact_form)

    with text_column:
        st.subheader("Construindo um ChatBot com LangChain e OpenAI")
        st.write(
            """
            Profissional em Tecnologia da Informação com experiência na criação e implementação de Assistentes Virtuais (ChatBots) para serviços ao cidadão. Especializado em Inteligência Artificial e Deep Learning, contribuí para o desenvolvimento de um ChatBot utilizando uma variedade de tecnologias, incluindo Python, o framework Langchain, e a API da OpenAI (GPT3.5, Embeddings, entre outros).

            Minhas responsabilidades abrangeram desde a integração de APIs até a análise de sentimentos das consultas dos usuários, utilizando ferramentas como Marvi. Gerenciei aspectos como saudações do bot, empregando o framework RASA, e utilizei Docker e docker-compose para garantir a eficiência e escalabilidade da aplicação.

            Além disso, participei ativamente da extração de entidades utilizando a biblioteca spaCy, contribuindo para a robustez e precisão das respostas do Assistente. Este projeto destacou minha capacidade de colaborar em equipes multidisciplinares, minha experiência em implementações de IA e meu compromisso com a entrega de soluções de alta qualidade que atendam às necessidades do cliente.
            """
        )
        st.markdown("[Ver meu Linkedin](https://www.linkedin.com/in/eddy-giusepe-chirinos-isidro-85a43a42/)")


with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Trabalho com AI, Machine Learning e Deep Learning")
        st.write(
            """
            Adoro trabalhar com NLP, Speech Processing e Visão Computacional. Atualmente, uso Engenharia de Prompt, LLMs,
            etc, para poder recuperar informações de um domínio específico, resumir e finalmente responder ao usuário 
            de forma mais humanizada.
            """
        )
        st.markdown("[Tecnologias que já usei](https://github.com/EddyGiusepe)")



# ---- CONTATO ----
with st.container():
    st.write("----")
    st.header("Entra em contato comigo")
    st.write("##")

    # https://formsubmit.co/
    contact_form = """
                   <form action="https://formsubmit.co/eddychirinos_unac@hotmail.com" method="POST">
                   <input type="text" name="name" placeholder="Seu nome" required>
                   <input type="email" name="email" placeholder="Seu e-mail" required>
                   <textarea name="mensagem" placeholder="Sua mensagem aqui" required></textarea>
                   <button type="submit">Enviar</button>
                   </form>
                   """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()