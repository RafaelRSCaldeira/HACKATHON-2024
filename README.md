# INTRODUÇÃO

Um código em Python foi desenvolvido com o propósito de criar um programa capaz de receber um arquivo em formato CSV e convertê-lo em um fluxograma. Inicialmente, o programa realiza o tratamento dos dados contidos no arquivo, para posteriormente realizar a conversão destes em uma representação visual por meio de uma imagem de fluxograma.


# BILIOTECAS UTILIZADAS

Neste projeto, foram empregadas as seguintes bibliotecas:

    1. Streamlit: Utilizada para a construção de interfaces web de forma simples e intuitiva, o Streamlit facilita a criação de aplicativos interativos em Python.

    2. Pandas: Uma biblioteca de análise de dados amplamente utilizada em Python, o Pandas oferece estruturas de dados poderosas e ferramentas para manipulação e análise eficiente de conjuntos de dados.

    3. Base64: Essa biblioteca é empregada para a codificação e decodificação de dados binários em ASCII, sendo comumente utilizada para representar dados binários de forma segura em formato de texto.

    4. Graphviz: Uma ferramenta utilizada para visualização de grafos e redes, o Graphviz oferece recursos para representação visual de estruturas de dados complexas, como fluxogramas e diagramas.

    5. IO: A biblioteca IO fornece classes e funções para trabalhar com operações de entrada e saída em Python, possibilitando a manipulação de fluxos de dados, arquivos e objetos.

    6. PIL (Python Imaging Library): Também conhecida como Pillow, essa biblioteca é utilizada para o processamento de imagens em Python, oferecendo uma ampla gama de funcionalidades para manipulação e edição de imagens digitais


# CÓDIGO

**BIBLIOTECAS**

	import streamlit as st
	import pandas as pd 
	from graphviz import Digraph 
	import base64 
	from PIL import Image 
	import io 


**FUNÇÃO PARA VERIFICAR SE DA PARA LER O ARQUIVO:**

Essa função tem como propósito realizar uma verificação preliminar para determinar se é possível ler o arquivo especificado.

	@st.cache_data #tratamento de dados
	def load_data(file_path):
	    try:
	        data = pd.read_csv(file_path, delimiter=';')
	        return data
	    except Exception as e:
	        st.error(f"Erro ao carregar o arquivo: {str(e)}")
	        return None


**FUNÇÃO PARA O TRATAMENTO DE DADOS:**

Essa função é responsável por processar e manipular os dados, aplicando as operações necessárias para prepará-los para análise ou visualização.

	def process_data(data): #tratamento de dados
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


**FUNÇÃO PARA ORDEM:**

Essa função é responsável por coordenar a ordem dos elementos, incluindo origens, destinos e backups, implementando uma lógica eficaz para a organização coerente dos fluxos. Após a organização lógica dos fluxos, a função utiliza a biblioteca Graphviz para gerar e plotar o gráfico correspondente, proporcionando uma representação visual clara e compreensível dos fluxos de dados.

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


**FUNÇÃO QUE VAI CHAMAR TODAS AS OUTRAS FUNÇÕES:**

Esta função atua como o ponto central do processo, coordenando e invocando todas as outras funções necessárias para executar as etapas do fluxo de trabalho

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


**FUNÇÃO DE EXPORTAÇÃO DO ARQUIVO:**

Esta função tem como finalidade exportar o arquivo processado, disponibilizando links para download nos formatos PDF e PNG.

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


# ENV
**Criando e Instalando um Ambiente Python usando requirements.txt**

Este README fornece um guia passo a passo sobre como criar e instalar um ambiente Python usando um arquivo requirements.txt. Esse processo garante que as dependências do seu projeto sejam gerenciadas de forma eficiente.

**Pré-requisitos:**
Python instalado no seu sistema (versão 3.x recomendada)
Gerenciador de pacotes pip instalado

**Passos:**

1. Criar um Ambiente Virtual (Opcional, mas Recomendado): É uma boa prática isolar as dependências do seu projeto usando um ambiente virtual. Isso evita conflitos entre diferentes projetos. Para criar um ambiente virtual, abra o seu terminal ou prompt de comando e navegue até o diretório do seu projeto. Em seguida, execute o seguinte comando:

	    py -m venv env
   
	Este comando criará uma pasta chamada env no diretório do seu projeto, contendo um interpretador Python e uma cópia da biblioteca padrão.


3. Ativar o Ambiente Virtual (Pule se Não Estiver Usando um Ambiente Virtual): Ativar o ambiente virtual garantirá que todos os comandos Python e pip subsequentes sejam executados dentro deste ambiente isolado. Para ativar o ambiente virtual, execute o comando apropriado com base no seu sistema operacional:

	Windows:

    	env\Scripts\activate
   
	Unix ou MacOS:

   	 	source env/bin/activate
   

5. Instalar Dependências do requirements.txt:Agora, você usará o gerenciador de pacotes pip para instalar todas as dependências listadas no arquivo requirements.txt. Certifique-se de que o arquivo requirements.txt esteja presente no diretório do seu projeto. Execute o seguinte comando:

	    pip install -r requirements.txt
   
	Este comando lerá o arquivo requirements.txt e instalará cada dependência listada nele, juntamente com suas respectivas versões.


7. Verificar a Instalação:Após o término do processo de instalação, você pode verificar se todas as dependências foram instaladas corretamente executando:

	    pip list
   
	Este comando exibirá uma lista de pacotes instalados juntamente com suas versões. Você deve ver os pacotes listados no seu arquivo requirements.txt entre eles.


9. Desativar o Ambiente Virtual (Se Utilizado):Depois de terminar o trabalho no seu projeto, você pode desativar o ambiente virtual executando:

	    deactivate
	Este comando retornará ao ambiente Python padrão do seu sistema.



