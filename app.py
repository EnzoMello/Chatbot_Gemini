# Importa framework para criar interface web simples
import streamlit as st
#importa biblioteca do google para interagir com API do Gemini
import google.generativeai as genai
# Importa a biblioteca que lê chave da api no arquivo .env
from dotenv import load_dotenv
import os
# Importa biblioteca para manipulação de imagens
from PIL import Image

load_dotenv()

# Tenta carregar a chave do Streamlit Cloud Secrets e se não encontrar (porque estamos rodando localmente), ele tenta carregar do arquivo .env
api_key = os.getenv("GOOGLE_API_KEY")


load_dotenv()
if not api_key:
    st.error("Chave de API do Google Gemini não encontrada. Por favor, verifique seu arquivo .env.")
    st.stop()

genai.configure(api_key=api_key)
model_name = "gemini-1.5-flash" # Define modelo do gemini que usaremos

# Tenta criar uma instância do modelo para gerar conteúdo
try:
    model = genai.GenerativeModel(model_name)
except Exception as e:
    st.error(f"Erro ao inicializar o modelo '{model_name}': {e}.")
    st.stop()

# Interface do Streamlit
st.set_page_config(page_title="Chatbot Gemini Flexível", layout="centered")

st.title("🤖 Chatbot com Gemini")
st.write("Faça uma pergunta ou envie uma imagem para análise. Ou os dois!")

# Componente de upload de arquivo
uploaded_file = st.file_uploader("Quer analisar uma imagem? Envie aqui (opcional):", type=["jpg", "jpeg", "png"])

# Mostra a imagem na tela se ela for enviada
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagem enviada. Faça uma pergunta sobre ela ou peça uma descrição.", use_container_width=True)

# Campo de texto genérico para prompt
user_prompt = st.text_input("Sua pergunta:", key="prompt_text")

if st.button("Enviar"):
    # Verifica se não há nenhum input
    if not user_prompt and not uploaded_file:
        st.warning("Por favor, digite uma pergunta ou envie uma imagem.")
        st.stop() # Para a execução se não houver nada a fazer

    with st.spinner("Gemini pensando..."):
        try:
           #  Decide se a chamada é com imagem ou apenas texto
            if uploaded_file is not None:
                # Cenário MULTIMODAL (com imagem)
                image = Image.open(uploaded_file)
                prompt = user_prompt if user_prompt else "Descreva esta imagem em detalhes."
                
                # Envia uma lista com texto e imagem
                contents = [prompt, image]
                response = model.generate_content(contents)
            else:                
                response = model.generate_content(user_prompt)

            # Exibe a resposta
            st.success("Resposta do Gemini:")
            st.markdown(response.text)

        except Exception as e:
            st.error(f"Ocorreu um erro ao comunicar com a API: {e}")

st.markdown("---")
