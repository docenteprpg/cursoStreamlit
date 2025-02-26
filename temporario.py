import streamlit as st
import pandas as pd

st.header("Cabeçalho")

st.multiselect(
     'Quais são suas cores favoritas?',
     ['Verde', 'Amarelo', 'Vermelho', 'Azul'],
     ['Amarelo', 'Vermelho'])

st.color_picker("Pick A Color", "#00f900")
st.feedback("stars")

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

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)















