
##########################################################################################################
##########################################################################################################
##########################################################################################################

import google.generativeai as genai
import os
from dotenv import load_dotenv
import streamlit as st

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configura el modelo de Google Generative AI
modelo = genai.GenerativeModel("gemini-1.5-pro")

# Configuración de la página de Streamlit
st.set_page_config(page_title="Chatbot Zerberus", page_icon="🤖")
st.title("Chat con Zerberus 🤖")

# Si no existe 'messages' en el estado de sesión, inicialízalo con el mensaje de bienvenida
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "user", "parts": ["Hola"]},
        {"role": "assistant", "parts": ["Hola como estás, ¿Cómo puedo ayudarte?"]},
    ]


# Mostrar todos los mensajes previos en el chat
for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["parts"][0])

# Si el usuario ingresa un nuevo mensaje
if prompt := st.chat_input():
    # Agregar el mensaje del usuario al historial
    st.session_state.messages.append({"role": "user", "parts": [prompt]})
    st.chat_message("user").write(prompt)

    # Crear la sesión de chat con el historial actualizado
    chat = modelo.start_chat(history=st.session_state.messages)

    # Obtener la respuesta del modelo
    response = chat.send_message(f"Responde en español: {prompt}")

    # Obtener el texto de la respuesta y agregarlo al historial
    msg = response.text
    st.session_state.messages.append({"role": "assistant", "parts": [msg]})
    st.chat_message("assistant").write(msg)

# Función para reiniciar el chat
def reset_chat():
    st.session_state["messages"] = [
        {"role": "assistant", "parts": ["¿Cómo puedo ayudarte?"]}
    ]

# Botón para limpiar el historial del chat
if st.button("Limpiar chat"):
    reset_chat()  # Reinicia el historial de mensajes
