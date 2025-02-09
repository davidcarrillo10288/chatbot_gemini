# ZERBERUS CHATBOT

Zerberus es un chatbot interactivo desarrollado con Streamlit y la API de Gemini (Google Generative AI). Su principal característica es la capacidad de mantener memoria y contexto en la conversación, permitiendo una experiencia más fluida e intuitiva para el usuario.

## CARACTERÍSTICAS PRINCIPALES:

✅ Memoria de la conversación: Guarda el historial de mensajes en la sesión de Streamlit, lo que permite que el chatbot recuerde el contexto y mantenga coherencia en las respuestas.

✅ Integración con Google Gemini: Utiliza el modelo Gemini-1.5-Pro para generar respuestas inteligentes y en español.

✅ Interfaz amigable con Streamlit: Ofrece una interfaz limpia y sencilla, con la opción de reiniciar el chat cuando sea necesario.

✅ Gestión dinámica del historial: Almacena y recupera los mensajes del usuario para una experiencia de conversación continua.

Este proyecto es ideal para implementar asistentes virtuales que requieran seguimiento del contexto en tiempo real, mejorando la interacción con el usuario. 🚀

## INSTALACIÓN: 

Para ejecutar este proyecto en tu máquina local, sigue estos pasos:

 * Clona el repositorio:
  ```bash
  git clone https://github.com/davidcarrillo10288/chatbot_gemini.git
  ```
 * Accede al directorio del proyecto:
  ```bash
  cd chatbot_gemini
  ```
 * Crea un entorno virtual (Recomendado):
  ```bash
  python -m venv venv  
  source venv/bin/activate  # En macOS/Linux  
  venv\Scripts\activate  # En Windows  
  ```
 * Instala las dependencias necesarias:
  ```bash
  pip install -r requirements.txt
  ```
 * Configura las credenciales de Google Gemini:
  ```bash
  echo "GOOGLE_API_KEY=tu_clave_aquí" > .env  
  ```
 * Ejecuta la aplicación:
  ```bash
  streamlit run app.py
  ```

* Si no tienes una clave API de Google, obtén una en: https://aistudio.google.com/apikey
