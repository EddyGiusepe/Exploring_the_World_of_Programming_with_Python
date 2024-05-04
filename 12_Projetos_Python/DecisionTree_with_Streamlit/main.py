#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Este estudo foi baseado no maravilhoso trabalho de "shamiraty"
Executar script
===============
$ pip install streamlit --upgrade
$ streamlit run main.py
"""
import streamlit as st
import pandas as pd 
import streamlit.components.v1 as stc
import plotly.express as px
import time
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
#from query import * 

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
#pip install -U scikit-learn

import warnings
warnings.filterwarnings("ignore") # Suprimindo todos os avisos.

st.set_page_config(page_title="Análise Descritiva", page_icon="📈", layout="wide")
st.markdown("<h2 style='text-align: center;'><font color='rainbow'>💰 Previsão de empréstimo</font></h2>", unsafe_allow_html=True)
#st.subheader("💰 Previsão de empréstimo", align='center', divider='rainbow')
st.write("Escolha que tipo de negócio você pretende fazer, escolha o local e o estado em que mora e depois verifique a probabilidade de conseguir um empréstimo")
st.markdown("##")
 
 
#for database use these two commented lines
#result = view_all_data()
#df = pd.DataFrame(result,columns=["Policy","Expiry","Location","State","Region","Investment","Construction","BusinessType","Earthquake","Flood","Rating","id"])

#for excel use this line
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
#print(df.head())


#st.sidebar.image("data/logo1.png",caption="Online Analytical")

# 2. Interruptor
st.sidebar.header("Filtre aqui:")
state= st.sidebar.selectbox(
    "Selecione o estado :",
    options=df["State"].unique(),
    help="Onde os negócios são alocados",   
)
region = st.sidebar.selectbox(
    "Selecione a zona :",
    options=df["Region"].unique(),
    help="Segmentar dentro de uma região"  
)
location = st.sidebar.radio(
    "Selecione a localização :",
    options=df["Location"].unique(),
    help="Áreas Urbanas ou Rurais"
     
)
construction = st.sidebar.radio(
    "Selecione a instalação :",
    options=df["Construction"].unique(),
    help="Bens ou serviços"
)


df_selection = df.query(
    "State == @state & Location ==@location & Region==@region & Construction==@construction"
 )

   

 
 
# Gráfico de barras simples:
investment_by_business_type=(
        df_selection.groupby(by=["BusinessType"]).count()[["State"]].sort_values(by="State")
    )
fig_investment=px.bar(
       investment_by_business_type,
       x="State",
       y=investment_by_business_type.index,
       orientation="h",
       title="Investimento por tipo de negócio",
       color_discrete_sequence=["#0083B8"]*len(investment_by_business_type),
       template="plotly_white",
    )


fig_investment.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
     )
 



try:
 with st.expander("Tabular"):
  #st.dataframe(df_selection,use_container_width=True)
  shwdata = st.multiselect('Filter :', df_selection.columns, default=["Location", "State", "Region", "Investment", "Construction", "BusinessType"])
  st.dataframe(df_selection[shwdata], use_container_width=True
  )
 
 df_selection['State'].replace(['Dodoma','Kigoma','Iringa','Mwanza','Dar es Salaam','Kilimanjaro','Arusha'],[1,2,3,4,5,6,7], inplace=True)
 df_selection['Location'].replace(['Urban','Rural'],[1,2],inplace=True)
 df_selection['Region'].replace(['East','Midwest','Northeast','Central'],[1,2,3,4],inplace=True)
 df_selection['Construction'].replace(['Frame','Fire Resist','Masonry','Metal Clad'],[1,2,3,4],inplace=True)

 X=df_selection.drop(columns=['BusinessType'])
 y=df_selection.drop(columns=['Location',  'State',  'Region',  'Investment',  'Construction'])
 X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, shuffle=True)
 clf = DecisionTreeClassifier() # Instância do classificador de árvore de decisão
 clf.fit(X_train, y_train) # Treinando
 test = clf.predict(X_test) # Previsões usando o método predict()
 from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
 accuracy = accuracy_score(y_test, test)

 
 col1, col2=st.columns(2)

 with col1:
  st.dataframe(df_selection["BusinessType"].unique(), use_container_width=True)

 with col2:
  st.write("Probabilidade de empréstimo:", round(accuracy, 2))
  st.title(f"{round(accuracy*100,1)} %")
  st.markdown("""---""")
  new_user=clf.predict([[df_selection["State"].unique(),df_selection["Location"].unique(),df_selection["Region"].unique(),0,df_selection["Construction"].unique()]]) 
  st.write("Instalação recomendada")
  st.info(",".join(new_user))
 st.plotly_chart(fig_investment, use_container_width=False, theme="streamlit") 

except:
     st.info("Uma das seleções é obrigatória")

# ---- OCULTAR ESTILO DE STREAMLIT ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
 