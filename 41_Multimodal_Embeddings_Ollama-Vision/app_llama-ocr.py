#!/usr/bin/env python3
"""
Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

llama-ocr
=========
Aqui vamos a criar um aplicativo para OCR usando o modelo "llama3.2-vision:11b" e
usando streamlit.
"""
import streamlit as st
import ollama
from PIL import Image
import io # É um módulo da biblioteca padrão do Python para lidar com streams de entrada/saída

# Página de configuração:
st.set_page_config(page_title="llama-ocr",
                   page_icon="🦙",
                   layout="wide",
                   initial_sidebar_state="expanded"
                  )

# Título e descrição na área principal:
st.title("🦙 llama3.2-vision:11b OCR 🦙")

# Adicionar botão limpar no canto superior direito:
col1, col2 = st.columns([6, 1])
with col2:
    if st.button("Limpar 🧹"):
        if 'ocr_result' in st.session_state:
            del st.session_state['ocr_result']
        st.rerun()

st.markdown('<p style="margin-top: -20px;">Extraia texto estruturado de imagens usando o llama3.2-vision:11b!</p>', unsafe_allow_html=True)
st.markdown("---")

# Mover os controles de upload para a barra lateral:
with st.sidebar:
    st.header("Upload de Imagem")
    uploaded_file = st.file_uploader("Escolha uma imagem...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Exibir a imagem carregada:
        image = Image.open(uploaded_file)
        st.image(image, caption="Imagem carregada")

        if st.button("Extrair Texto 📄", type="primary"):
            with st.spinner("Processando imagem..."):
                try:
                    response = ollama.chat(
                        model="llama3.2-vision:11b",
                        messages=[{'role': 'system',
                                   'content': """Você é um experto em Análise de Vibração, Manutenção preditiva
                                                e monitoramento de ativos industriais. Você analisa imagens de motores
                                                elétricos e extrai o texto legível. 
                                              """
                                  },
                                  {'role': 'user',
                                   'content': """Qual é a marca do motor e o peso?
                                              """,
                                  'images': [uploaded_file.getvalue()]    
                                  }]
                    )
                    st.session_state['ocr_result'] = response['message']['content']
                except Exception as e:
                    st.error(f"Erro ao processar a imagem: {str(e)}")

# Área de conteúdo principal para resultados:
if 'ocr_result' in st.session_state:
    st.markdown(st.session_state['ocr_result'])
else: 
    st.info("Carregue uma imagem e clique em 'Extrair texto' para ver os resultados aqui.")

# Feedback:
if 'ocr_result' in st.session_state:
    st.write("O resultado foi útil?")
    col1, col2, col3 = st.columns([1,1,4])
    with col1:
        if st.button("👍"):
            st.success("Obrigado pelo feedback positivo!")
    with col2:
        if st.button("👎"):
            st.text_area("Como podemos melhorar?")
            if st.button("Enviar Feedback"):
                st.success("Obrigado por nos ajudar a melhorar!")

# Baixar os resultados:
if 'ocr_result' in st.session_state:
    resultado = st.session_state['ocr_result']
    st.download_button(
        label="Download Resultados 📥",
        data=resultado,
        file_name="resultado_ocr.txt",
        mime="text/plain"
    )

# Rodapé:
st.markdown("---")
st.markdown("Desenvolvido com ❤️ pelo [Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro](https://www.linkedin.com/in/eddy-giusepe-chirinos-isidro-phd-85a43a42/)")
