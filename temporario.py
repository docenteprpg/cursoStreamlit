import streamlit as st
st.header("Cabeçalho")

st.multiselect(
     'Quais são suas cores favoritas?',
     ['Verde', 'Amarelo', 'Vermelho', 'Azul'],
     ['Amarelo', 'Vermelho'])

st.toggle("Toggle")
st.text_area("Enter text")
st.text_input("")
st.selectbox(
  'Qual a sua cor favorita?',
  ('Azul', 'Vermelho', 'Verde'))

st.checkbox('Sorvete')
st.checkbox('Café')
st.checkbox('Refrigerante')

options = ["North", "East", "South", "West"]
selection = st.pills("Directions", options, selection_mode="multi")

st.button("Botão Salvar")
