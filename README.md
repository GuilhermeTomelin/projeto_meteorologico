
# Monitoramento Meteorológico

Aplicação Python que consulta dados meteorológicos simulados
de Jaraguá do Sul - SC e apresenta os resultados no Streamlit.

## Tecnologias
- Python
- Requests
- Streamlit
- API REST local

## Arquivos
- consumidor_api.py: consulta a API.
- frontend.py: apresenta as informações.
- requirements.txt: dependências.
- .gitignore: arquivos ignorados pelo Git.

## Preparação

A API utilizada está disponível em:
https://github.com/jpsvalentim/api-meteorologica-offline

Siga as instruções do repositório para instalar e iniciar a API.

A API deve estar funcionando em:
http://127.0.0.1:8000

## Executar o projeto

Criar o ambiente virtual:

python -m venv .venv

Ativar no PowerShell:

.\.venv\Scripts\Activate.ps1

Instalar as dependências:

python -m pip install -r requirements.txt

Iniciar a interface:

python -m streamlit run frontend.py

## Testes

Verificar a API:
http://127.0.0.1:8000/health

Testar pelo Postman:
GET http://127.0.0.1:8000/v1/forecast

Parâmetros:
latitude = -26.4851
longitude = -49.0713