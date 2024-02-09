import streamlit as st
import requests
import json

# Titular la ventana principal de la app
st.title("Ejemplo de app de Streamlit")

# Crear un campo de texto para que el usuario pueda ingresar la pregunta
pregunta = st.text_input("Ingrese la pregunta:", "")

# Crear un campo de texto para que el usuario pueda ingresar el estado de la spell
estado = st.text_input("Ingrese el estado:", "")

# Utilizar las funciones requests y json para enviar la solicitud HTTP a la API de Respell AI
response = requests.post("https://api.respell.ai/v1/run", headers={
    "Authorization": "Bearer YOUR_API_KEY",
    "Accept": "application/json",
    "Content-Type": "application/json"
}, data=json.dumps({
    "spellId": "AMS1u_FAWQea7sxE6Ffu6",
    "spellVersionId": "sU33jCqGk0-RJKDxeiWif",
    "inputs": {
        "pregunta": pregunta,
        "estado": estado
    }
}))

# Procesar la respuesta de la API
if response.status_code == 200:
    # Extraer la respuesta del modelo de la API
    respuesta_modelo = json.loads(response.text)["output"]["completion"]
    
    # Mostrar la respuesta del modelo en la ventana principal de la app
    st.write(respuesta_modelo)
else:
    st.write("Error running spell:", response.text)
