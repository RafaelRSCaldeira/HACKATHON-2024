import pandas as pd
import streamlit as st


st.set_page_config(initial_sidebar_state="collapsed", page_title="Sobre Nós", page_icon="🧑")

with open("style.css") as file:
    st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

footer = '''
<footer class=footer>
    <p>Feito com ❤️ por Hippocampus</p>
</footer>
'''
st.markdown(footer, unsafe_allow_html=True)

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

columns = st.columns(2)
with columns[0]:
    st.markdown("<div class='leftColumn'></div>", unsafe_allow_html=True)
    st.markdown('''
                <p class="aboutUsTitleLeft">Alice</p>
                <p class="aboutUsDescriptionLeft" id="Alice">Como estudante de engenharia da computação no terceiro semestre da Universidade Presbiteriana Mackenzie, sou uma entusiasta apaixonada pela programação desde os meus primeiros passos na internet na infância. Minha jornada começou com uma simples curiosidade, que rapidamente se transformou em uma paixão duradoura pela arte de codificar. Explorar os intricados meandros da ciência da computação é mais do que uma atividade acadêmica para mim; é uma busca incessante pela compreensão e maestria das linguagens e algoritmos que impulsionam o mundo digital. Sempre em busca de desafios e novos conhecimentos, encontro na engenharia da computação não apenas uma carreira potencial, mas uma verdadeira vocação que alimenta minha curiosidade e criatividade.</p>
                <p class="aboutUsTitleLeft">Fábio</p></br>
                <p class="aboutUsDescriptionLeft" id"Fabio">Como estudante de engenharia de produção na Universidade Presbiteriana Mackenzie, encontro uma fusão única entre a análise sistemática e a criatividade inovadora. Minha paixão pela eficiência e otimização é complementada pelo meu papel como programador freelancer nas horas vagas, onde aplico minhas habilidades técnicas para resolver problemas e criar soluções sob medida. Esta dualidade de habilidades me permite abordar os desafios tanto do mundo acadêmico quanto do mercado de trabalho de forma holística, buscando constantemente maneiras de integrar a tecnologia à engenharia de produção para alcançar resultados excepcionais.</p>
                <p class="aboutUsTitleLeft">Mariane</p></br>
                <p class="aboutUsDescriptionLeft" id"Mariane">Como estudante de engenharia elétrica no Mackenzie, trilhei um caminho de descoberta e autodescoberta ao ingressar inicialmente no curso de engenharia mecânica e, posteriormente, migrar para elétrica no quarto semestre. Essa transição não só reflete minha busca por alinhamento entre meus interesses e habilidades, mas também evidencia minha vontade de explorar novos horizontes. Com um amor pela programação que permeia minha jornada acadêmica, enxergo na engenharia elétrica não apenas uma disciplina técnica, mas um campo de possibilidades infinitas onde posso unir minha paixão pela tecnologia com meu desejo de criar soluções inovadoras e impactantes.</p>
                ''', unsafe_allow_html=True)

with columns[1]:
    st.markdown("<div class='rightColumn'></div>", unsafe_allow_html=True)
    st.markdown('''
                <p class="aboutUsTitleRight">Rafael</p>
                <p class="aboutUsDescriptionRight" id="Rafael">Como estudante de engenharia da computação no Mackenzie, minha trajetória é marcada por uma afinidade intrínseca tanto pela programação quanto pela matemática, elementos que considero essenciais para desbravar os desafios e as nuances da era digital. Optei por este curso por reconhecer nele a interseção ideal entre meus interesses, onde posso explorar profundamente a lógica computacional enquanto mergulho nas complexidades dos números e algoritmos. Para mim, a computação é mais do que uma disciplina acadêmica; é uma paixão que impulsiona minha curiosidade incessante e minha busca por soluções inovadoras. Neste ambiente dinâmico e desafiador, vejo oportunidades infinitas de crescimento e contribuição para o mundo tecnológico em constante evolução.</p>
                <p class="aboutUsTitleRight">Sophia</p></br>
                <p class="aboutUsDescriptionRight" id"Sophia">Como estudante de engenharia elétrica no Mackenzie, minha jornada é guiada não apenas pelo desejo de aprender, mas também pelo compromisso inabalável de compartilhar conhecimento e capacitar os outros. Minha paixão por ajudar se manifesta não apenas dentro dos limites da universidade, mas além deles, onde busco democratizar o acesso ao aprendizado, ensinando e orientando aqueles que estão fora dos muros acadêmicos. Acredito firmemente que o conhecimento é uma ferramenta poderosa que deve ser acessível a todos, e é com esse princípio em mente que me dedico a inspirar e capacitar outros a alcançarem seu pleno potencial, não apenas como estudantes, mas como agentes de mudança em suas próprias comunidades.</p>
                ''', unsafe_allow_html=True)


