import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Teste do Streamlit", page_icon="✅")

st.title("✅ Streamlit está funcionando!")
st.write("Se você está vendo esta página, a instalação deu certo.")

# Interação básica
nome = st.text_input("Qual é o seu nome?")
if nome:
    st.success(f"Olá, {nome}! 👋")

# Widget com estado
valor = st.slider("Escolha um número de pontos", min_value=10, max_value=200, value=50)

# Gráfico com dados aleatórios
dados = pd.DataFrame(
    np.random.randn(valor, 3),
    columns=["A", "B", "C"],
)
st.line_chart(dados)

# Tabela
with st.expander("Ver tabela de dados"):
    st.dataframe(dados)

# Botão
if st.button("Clique aqui"):
    st.balloons()