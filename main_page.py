from enviorment import Enviorment
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)


amount = st.sidebar.slider('amount of nodes', 30, 100)


env = Enviorment(amount_of_nodes=amount)
env.generate_network()
env.select_random_cluster_heades()
env.draw_network()

st.pyplot(env.draw_network())

