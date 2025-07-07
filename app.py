import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configura a API do Google Gemini
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("Chave de API do Google Gemini não encontrada. Por favor, verifique seu arquivo .env.")
    st.stop() # Para a execução se a chave não for encontrada

genai.configure(api_key=api_key)

# Configuração do modelo Gemini
model_name = "gemini-1.5-flash-latest" # Mantenha este primeiro

try:
    model = genai.GenerativeModel(model_name)
except Exception as e:
    st.error(f"Erro ao inicializar o modelo '{model_name}': {e}. Verifique se o nome do modelo está correto e se ele está disponível para sua chave de API.")
    st.stop() # Para a execução se o modelo não puder ser inicializado


st.set_page_config(page_title="Chatbot Gemini IA", layout="centered")

st.title("🤖 Chatbot IA com Gemini")
st.write("Pergunte-me qualquer coisa e eu responderei usando a inteligência artificial do Google Gemini!")

# Campo de entrada de texto para o usuário
user_input = st.text_input("Sua pergunta:", key="input_text")

# Botão para enviar a pergunta
if st.button("Enviar Pergunta"):
    if user_input:
        with st.spinner("Pensando..."):
            try:
                # Geração da resposta usando o modelo Gemini
                response = model.generate_content(user_input)
                st.success("Resposta:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Ocorreu um erro ao gerar a resposta: {e}")
    else:
        st.warning("Por favor, digite sua pergunta antes de enviar.")

st.markdown("---")
st.caption("Desenvolvido com Google Gemini e Streamlit")