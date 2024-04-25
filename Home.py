import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed", page_title="Fluxo de Aplicações", page_icon=":chart_with_upwards_trend:")

with open("style.css") as file:
    st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

footer = '''
<footer class=footer>
    <p>Feito com ❤️ por Hippocampus</p>
</footer>
'''
st.markdown(footer, unsafe_allow_html=True)

buttons = st.columns(3, gap="medium")
with buttons[0]:
    if st.button("Pagina Inicial", type="primary"):
        st.switch_page("Home.py")
with buttons[1]:
    if st.button("Produto", type="primary"):
        st.switch_page("pages/Product.py")
with buttons[2]:
    if st.button("Sobre Nós", type="primary"):
        st.switch_page("pages/Contact.py")

st.markdown("<div class='introductionBG'></div>", unsafe_allow_html=True)


col1, col2 = st.columns(2)
with col1:
    st.markdown('''
    <img class="bannerImage" src="https://www.mackenzie.br/fileadmin/ARQUIVOS/Public/1-mackenzie/universidade/unidades-academicas/EE/2024/hackathon/banner/HIPER.png">
    ''', unsafe_allow_html=True)
with col2:
    st.markdown('''
    <p class="titleBanner"> Desafio HACKATHON</br>:hiperstream</p>
    <p class="descriptionBanner">DESENHO DE FLUXO DE APLICAÇÕES</p>
    ''', unsafe_allow_html=True)


