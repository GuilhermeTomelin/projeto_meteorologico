
# Explicação técnica

## Consumidor da API

O arquivo consumidor_api.py utiliza a biblioteca Requests
para se comunicar com a API local.

A função obter_dados_meteorologicos envia uma requisição
GET com a latitude e a longitude de Jaraguá do Sul.

O comando raise_for_status verifica se ocorreu algum erro
HTTP. Depois, json() interpreta os dados recebidos.

As informações meteorológicas são retiradas do grupo
"current" e organizadas em um dicionário Python.

Caso aconteça algum erro na consulta ou na leitura dos
dados, o programa informa que houve uma falha.

## Interface

O arquivo frontend.py utiliza a biblioteca Streamlit.

Ele importa a função do consumidor e recebe os dados
meteorológicos.

O comando st.metric apresenta os indicadores com seus
valores e unidades de medida.

O comando st.write apresenta o horário da API.

Se a consulta falhar, st.error apresenta a mensagem
na interface.

## Fluxo de integração

API local -> Requests -> JSON -> Dicionário Python
-> Streamlit -> Indicadores na tela.