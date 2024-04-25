import pandas as pd
import streamlit as st


st.set_page_config(initial_sidebar_state="collapsed", page_title="Fluxo de Informação", page_icon=":chart_with_upwards_trend:")

with open("style.css") as file:
    st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

footer = '''
<footer class=footer>
    <p>Feito com ❤️ por Hippocampus</p>
</footer>
'''
st.markdown(footer, unsafe_allow_html=True)

columns = st.columns(2)
with columns[0]:
    st.markdown("<div class='leftColumn'></div>", unsafe_allow_html=True)
    st.markdown("<p class='leftDescription'>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sit amet justo egestas, rutrum tortor ac, varius erat. Morbi sed ligula placerat, laoreet nisi vitae, feugiat odio.</br>Nam nec mi dui. Maecenas sodales turpis sed lectus aliquet tristique. Ut euismod sed urna sit amet accumsan. Pellentesque ligula mauris, vulputate eu nunc vitae, vulputate cursus nibh. Pellentesque sed facilisis massa, eu laoreet nunc. Curabitur finibus lacus at odio cursus, id mattis diam pretium. </br></br></br>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sit amet justo egestas, rutrum tortor ac, varius erat. Morbi sed ligula placerat, laoreet nisi vitae, feugiat odio.</br>Nam nec mi dui. Maecenas sodales turpis sed lectus aliquet tristique. Ut euismod sed urna sit amet accumsan. Pellentesque ligula mauris, vulputate eu nunc vitae, vulputate cursus nibh. Pellentesque sed facilisis massa, eu laoreet nunc. Curabitur finibus lacus at odio cursus, id mattis diam pretium. </br></br></br>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sit amet justo egestas, rutrum tortor ac, varius erat. Morbi sed ligula placerat, laoreet nisi vitae, feugiat odio.</br>Nam nec mi dui. Maecenas sodales turpis sed lectus aliquet tristique. Ut euismod sed urna sit amet accumsan. Pellentesque ligula mauris, vulputate eu nunc vitae, vulputate cursus nibh. Pellentesque sed facilisis massa, eu laoreet nunc. Curabitur finibus lacus at odio cursus, id mattis diam pretium.</p>", unsafe_allow_html=True)

with columns[1]:
    st.markdown("<div class='rightColumn'></div>", unsafe_allow_html=True)
    st.markdown("<p class='rightDescription'>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sit amet justo egestas, rutrum tortor ac, varius erat. Morbi sed ligula placerat, laoreet nisi vitae, feugiat odio.</br>Nam nec mi dui. Maecenas sodales turpis sed lectus aliquet tristique. Ut euismod sed urna sit amet accumsan. Pellentesque ligula mauris, vulputate eu nunc vitae, vulputate cursus nibh. Pellentesque sed facilisis massa, eu laoreet nunc. Curabitur finibus lacus at odio cursus, id mattis diam pretium. </br></br></br>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sit amet justo egestas, rutrum tortor ac, varius erat. Morbi sed ligula placerat, laoreet nisi vitae, feugiat odio.</br>Nam nec mi dui. Maecenas sodales turpis sed lectus aliquet tristique. Ut euismod sed urna sit amet accumsan. Pellentesque ligula mauris, vulputate eu nunc vitae, vulputate cursus nibh. Pellentesque sed facilisis massa, eu laoreet nunc. Curabitur finibus lacus at odio cursus, id mattis diam pretium.</p>", unsafe_allow_html=True)


buttons = st.columns(3)
with buttons[0]:
    if st.button("Pagina Inicial", type="primary"):
        st.switch_page("Home.py")
with buttons[1]:
    if st.button("Produto", type="primary"):
        st.switch_page("pages/Product.py")
with buttons[2]:
    if st.button("Sobre Nós", type="primary"):
        st.switch_page("pages/Contact.py")
