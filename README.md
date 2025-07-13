# 🤖 Chatbot Multimodal com Google Gemini

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35.0-red.svg)
![Google Gemini](https://img.shields.io/badge/Google_Gemini-API-green.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Este projeto é um chatbot interativo construído com Python, utilizando o poder da API do **Google Gemini** para processamento de linguagem e visão computacional, e o **Streamlit** para criar uma interface web amigável e reativa.

O chatbot é capaz de responder a perguntas baseadas em texto e também analisar imagens enviadas pelo usuário, descrevendo-as ou respondendo a perguntas sobre elas. Ele utiliza o modelo `gemini-1.5-flash`, que é otimizado para respostas rápidas e multimodalidade.

### 📸 Demonstração


<img width="1302" height="974" alt="image" src="https://github.com/user-attachments/assets/d577cf1e-0e57-47d4-83c1-fcf71f85ab56" />

---

## ✨ Funcionalidades

* **Interação via Texto:** Converse com o bot fazendo perguntas ou pedindo informações.
* **Análise de Imagens:** Envie uma imagem (JPG,JPEG,PNG) e peça uma descrição detalhada ou faça perguntas específicas sobre o conteúdo visual.
* **Interface Intuitiva:** Interface web simples e limpa, criada com Streamlit, que permite o upload de arquivos e a entrada de texto de forma fácil.
* **Respostas Rápidas:** Utiliza o modelo `gemini-1.5-flash` para uma interação ágil.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.9+**
* **Streamlit:** Para a criação da interface web.
* **Google Gemini API (`google-generativeai`):** Para acesso aos modelos de IA generativa.
* **Pillow (`PIL`):** Para manipulação e processamento de imagens.
* **Python-dotenv:** Para gerenciamento de variáveis de ambiente em desenvolvimento local.

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para executar o projeto em sua máquina local.

#### 1. Pré-requisitos

* Ter o [Python 3.9](https://www.python.org/downloads/) ou superior instalado.
* Ter o [Git](https://git-scm.com/) instalado para clonar o repositório.
* Uma chave de API do Google Gemini. Você pode obter a sua no [Google AI Studio](https://aistudio.google.com/app/apikey).

#### 2. Clone o Repositório e depois navegue até o diretório
```bash
git clone https://github.com/EnzoMello/Chatbot_Gemini.git
cd Chatbot_Gemini
```

#### 3. Crie um Ambiente Virtual e Instale as Dependências

É uma boa prática usar um ambiente virtual para isolar as dependências do projeto.

```bash
# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# No Windows:
venv\Scripts\activate
```

Antes de instalar, crie um arquivo `requirements.txt` com o seguinte conteúdo:
```txt
streamlit
google-generativeai
python-dotenv
Pillow
```

Agora, instale as bibliotecas:
```bash
pip install -r requirements.txt
```

#### 4. Configure a Chave de API

1.  Crie um arquivo chamado `.env` na raiz do projeto.
2.  Dentro deste arquivo, adicione sua chave de API do Gemini:

    ```
    GOOGLE_API_KEY="SUA_CHAVE_API_AQUI"
    ```

#### 4. Execute o Aplicativo

Com o ambiente virtual ativado e a chave configurada, inicie o servidor do Streamlit:

```bash
streamlit run app.py
```
Seu navegador abrirá automaticamente com o aplicativo em execução!

---

## 💡 Possíveis Melhorias

* [ ] Implementar **histórico de conversa** (`st.session_state`) para que o bot lembre de interações passadas.
* [ ] Adicionar **streaming de respostas** para que o texto do bot apareça palavra por palavra, melhorando a experiência do usuário.
* [ ] Criar uma barra lateral (`st.sidebar`) para opções, como a escolha do modelo Gemini ou o ajuste de parâmetros (temperatura, etc.).

---

## 👨‍💻 Autor

Feito por **Enzo Melo**.

