
import streamlit as st
from consumidor_api import obter_dados_meteorologicos

st.set_page_config(page_title="Meteorologia")

st.title("🌦️ Monitoramento Meteorológico")
st.write("Jaraguá do Sul - SC")
st.caption("Dados simulados da API local")

try:
    # Busca os dados pelo consumidor
    dados = obter_dados_meteorologicos()

    col1, col2, col3 = st.columns(3)

    col1.metric("Temperatura", f"{dados['temperatura']} °C")
    col2.metric("Umidade", f"{dados['umidade']} %")
    col3.metric("Sensação térmica", f"{dados['sensacao']} °C")

    col4, col5 = st.columns(2)

    col4.metric("Precipitação", f"{dados['precipitacao']} mm")
    col5.metric("Velocidade do vento", f"{dados['vento']} km/h")

    st.write("Horário da API:", dados["horario"].replace("T", " "))

except RuntimeError as erro:
    st.error(str(erro))
