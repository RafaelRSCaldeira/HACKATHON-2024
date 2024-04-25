import streamlit as st
import pandas as pd
from graphviz import Digraph
import base64
from PIL import Image
import io


@st.cache_data
def load_data(file_path):
    try:
        data = pd.read_csv(file_path, delimiter=';')
        return data
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {str(e)}")
        return None


def process_data(data):
    flows = {}
    for _, row in data.iterrows():
        name = row['Nome']
        origem = row['PastaOrigem']
        destino = row['PastaDestino']
        backup = row['PastaBackup']
        
        origem = str(origem).replace('\\', '/').lower()
        destino = str(destino).replace('\\', '/').lower()
        backup = str(backup).replace('\\', '/').lower()
        
        destino = destino if pd.notna(destino) else " "
        backup = backup if pd.notna(backup) else " "
        
        flows[name] = [origem, destino, backup]
    return flows

def draw_flow_diagram(flows):
    dot = Digraph(format='png')

    for flow_name in flows.keys():
        dot.node(flow_name, flow_name)

    for flow1, paths1 in flows.items():
        origem1, destino1, backup1 = paths1
        for flow2, paths2 in flows.items():
            origem2, destino2, backup2 = paths2
            
            if flow1 != flow2:
                if origem1 == destino2:
                    dot.edge(flow2, flow1)
                if origem1 == backup2:
                    dot.edge(flow2, flow1)

    return dot.pipe()

def main():
    st.set_page_config(page_title="Fluxo de Informação", page_icon=":chart_with_upwards_trend:")

    st.title('Fluxo de Informação entre Pastas')

    file_path = st.file_uploader("Carregar arquivo CSV", type=['csv'])

    if file_path is not None:
        data = load_data(file_path)
        if data is not None:
            st.write("Dados carregados com sucesso!")
            
            st.write("Exemplo dos dados:")
            st.write(data.head())

            with st.spinner("Processando dados..."):
                flows = process_data(data)

            st.write("Desenhando diagrama de fluxo de informações...")
            image = draw_flow_diagram(flows)
            st.image(image, use_column_width=True)

            st.markdown(get_download_links(image), unsafe_allow_html=True)

def get_download_links(img_bytes):
    """Gerar links para download em PDF e PNG."""
    img = Image.open(io.BytesIO(img_bytes))

    
    href_png = f'<a href="data:image/png;base64,{base64.b64encode(img_bytes).decode()}" download="flowchart.png">Download PNG</a>'

    
    pdf_bytes = io.BytesIO()
    img.save(pdf_bytes, format='PDF')
    href_pdf = f'<a href="data:application/pdf;base64,{base64.b64encode(pdf_bytes.getvalue()).decode()}" download="fluxograma.pdf">Download PDF</a>'

    return href_png + " | " + href_pdf

if __name__ == "__main__":
    main()