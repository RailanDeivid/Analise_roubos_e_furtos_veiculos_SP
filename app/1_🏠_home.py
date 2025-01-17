import pandas as pd
import os
import streamlit as st


# Função para carregar os dados
if "data" not in st.session_state:
    # Caminho dos arquivos
    path = os.path.dirname(__file__)
    my_data = path+'/data/VeiculosSubtraidos.parquet'
    df = pd.read_parquet(my_data)
    st.session_state["data"] = df



# Define o layout da pagina
st.set_page_config(
    page_title="Home",
    page_icon="🏠", 
    initial_sidebar_state="expanded",
    layout="wide"
    )


# # setando titulo
# st.markdown("""
#     <style>
#         .rounded-title {
#             text-align: center; 
#             font-size: 40px;
#         }
#     </style>
#     """, unsafe_allow_html=True)

# st.markdown("<h1 class='rounded-title'>Análise de Dados Públicos de Furtos e Roubos no municipio de Guarulhos-SP.</h1>", unsafe_allow_html=True)
st.header('Análise de Dados Públicos de Furtos e Roubos no municipio de Guarulhos-SP', divider='rainbow')

# setando informações
st.markdown(
"""<p style='font-size: 16px;'>Este projeto faz parte de uma atividade extensiva dedicada à análise e disseminação de dados públicos sobre furtos e roubos em Guarulhos-SP. 
A iniciativa visa não apenas compreender as tendências de crimes na região, mas também proporcionar insights valiosos para a comunidade.
Através da aplicação de técnicas avançadas de ciência de dados, meu objetivo é:</p>""", unsafe_allow_html=True)

st.markdown("""
- **<h3 style='font-size: 20px;'>Objetivos do Projeto:</h3>**
    - **Análise Profunda de Dados:**
        - Utilizando técnicas avançadas de ciência de dados, o projeto visa realizar uma análise abrangente dos registros de furtos e roubos em Guarulhos. Isso inclui a identificação de padrões temporais, locais e tipos de crime mais prevalentes.
    - **Desenvolvimento de Ferramentas Interativas:**
        - Serão desenvolvidas ferramentas interativas e visualizações dinâmicas para facilitar o entendimento e a exploração dos dados por parte dos usuários. Essas ferramentas permitirão a análise espacial dos crimes, comparações ao longo do tempo e insights detalhados sobre áreas de maior incidência.
    - **Engajamento Comunitário:**
        - Além da análise técnica, o projeto busca promover o engajamento comunitário através da divulgação dos resultados. Isso inclui a conscientização sobre questões de segurança, a promoção de práticas preventivas e a participação ativa dos cidadãos na promoção de um ambiente mais seguro.
""", unsafe_allow_html=True)

st.markdown("""
- **<h3 style='font-size: 20px;'>Informações dos Dados:</h3>**
Os dados usados para o desenvolvimento desse projeto são dados abertos da [Secretaria de Segurança Publica de São paulo (SSP)](https://www.ssp.sp.gov.br/estatistica/consultas)
        
    - São Paulo é pioneiro na divulgação mensal dos dados estatísticos por Estado, área, município e unidade policial. Os índices também são divulgados trimestralmente. Conteúdo ajuda a monitorar a evolução das tendências criminais e o planejamento do Estado e das polícias.
    - As estatísticas criminais são utilizadas para retratar a situação da segurança pública e permitir o planejamento de ações policiais e de investimentos no setor. Em São Paulo, 
            a compilação dos dados é feita pela Secretaria da Segurança Pública, por intermédio da Coordenadoria de Análise e Planejamento (CAP) - responsável pela análise dos dados de interesse policial e pela realização de estudos para prevenir e reprimir a criminalidade.
            
    - No site das SSP, você pode encontrar:
        - Dados criminais
        - Dados de Produtividade
        - Morte Decorrente de Intervenção Policial
        - Celulares subtraídos
        - Veículos subtraídos
        - Objetos subtraídos
    
""", unsafe_allow_html=True)


