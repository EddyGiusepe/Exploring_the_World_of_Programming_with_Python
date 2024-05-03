#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Executar script
===============
$ pip install streamlit --upgrade
$ streamlit run main.py
"""
import streamlit as st
import pandas as pd 
import time

# Comportamento da página:
st.set_page_config(page_title="Análise Descritiva", page_icon="🤗", layout="wide")

# Remover tema padrão:
theme_plotly = None # None or streamlit

# Style CSS:
with open("./style.css") as f:
    st.markdown(f"<style>{f.read}</style>", unsafe_allow_html=True)

# Carregar Data:
df = pd.read_csv("./data.csv")

# Interruptor:
st.sidebar.header("Por favor, filtre aqui:")
region = st.sidebar.multiselect(
    "Selecione a região:",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)
location = st.sidebar.multiselect(
    "Selecione a localização:",
    options=df["Location"].unique(),
    default=df["Location"].unique()
)
construction = st.sidebar.multiselect(
    "Selecione a Construção:",
    options=df["Construction"].unique(),
    default=df["Construction"].unique()
)


df_selection = df.query(
    "Region == @region & Location == @location & Construction == @construction"
)

# Método/função:

def HomePage():
    # 1. Printamos o DataFrame:
    with st.expander("🎲 Minha base de dados"):
        #st.dataframe(df_selection, use_container_width=True)
        shwdata = st.multiselect('Filtro:', df_selection.columns, default=["Location", "State", "Region", "Investment", "Construction", "BusinessType", "Earthquake"])
        st.dataframe(df_selection[shwdata], use_container_width=True)


    # 2. Calcule as principais análises:
    total_investment = float(df_selection['Investment'].sum())
    investment_mode = float(df_selection['Investment'].mode())
    investment_mean = float(df_selection['Investment'].mean())
    investment_median= float(df_selection['Investment'].median()) 
    rating = float(df_selection['Rating'].sum())

    print(total_investment)
    # 3. Colunas:
    total1, total2, total3, total4 = st.columns(4, gap='large')
    with total1:

        st.info('Investimento total', icon="🔍")
        st.metric(label = 'Soma TZS', value=f"{total_investment:,.0f}")
        
    with total2:
        st.info('Mais frequente', icon="🔍")
        st.metric(label='Mode TZS', value=f"{investment_mode:,.0f}")

    with total3:
        st.info('Média de investimento', icon="🔍")
        st.metric(label= 'Mean TZS',value=f"{investment_mean:,.0f}")

    with total4:
        st.info('Margem de Investimento', icon="🔍")
        st.metric(label='Median TZS',value=f"{investment_median:,.0f}")

    st.markdown("""---""")


# Gráficos:

def Graphs():
 total_investments = int(df_selection["Investment"].sum())
 average_rating = round(df_selection["Rating"].mean(), 1)
 star_rating = ":star:" * int(round(average_rating, 0))
 average_investment = round(df_selection["Investment"].mean(), 2)


# -----BARRA DE PROGRESSO-----

def ProgressBar():
  st.markdown("""<style>.stProgress > div > div > div > div { background-image: linear-gradient(to right, #99ff99 , #FFFF00)}</style>""", unsafe_allow_html=True,)
  target=3000000000
  current=df_selection['Investment'].sum()
  percent=round((current/target*100))
  my_bar = st.progress(0)

  if percent>100:
    st.subheader("Meta 100 concluída")
  else:
   st.write("Você tem ", percent, " % " ," de ", (format(target, ',d')), " TZS")
   for percent_complete in range(percent):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1, text="Porcentagem desejada")


# -----BARRA LATERAL-----

HomePage()
Graphs()
ProgressBar()

# footer="""<style>
 

# a:hover,  a:active {
# color: red;
# background-color: transparent;
# text-decoration: underline;
# }

# .footer {
# position: fixed;
# left: 0;
# height:10%;
# bottom: 0;
# width: 100%;
# background-color: #D0D0D0;
# color: white;
# text-align: center;
# }
# </style>
# <div class="footer">
# <p>Developed with  ❤ by samir <a style='display: block; text-align: center;' href="https://www.heflin.dev/" target="_blank">Samir.s.s</a></p>
# </div>
# """
# st.markdown(footer, unsafe_allow_html=True)