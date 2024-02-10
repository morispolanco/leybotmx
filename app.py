import streamlit as st
import requests
import json

def main():
    st.title("Chatbot con Respell.ai")

    # Obtiene la entrada del usuario
    pregunta = st.text_input("Ingrese su pregunta:")

    if st.button("Enviar"):
        # Llama a la API de Respell.ai
        response = llamar_api(pregunta)
        
        # Muestra la respuesta de la API
        if response.status_code == 200:
            data = response.json()
            st.success("Respuesta del Chatbot: {}".format(data['response']))
        else:
            st.error("Error al llamar a la API. Código de estado: {}".format(response.status_code))

def llamar_api(pregunta):
    # Llamada a la API de Respell.ai
    url = "https://api.respell.ai/v1/run"
    headers = {
        "Authorization": "Bearer 260cee54-6d54-48ba-92e8-bf641b5f4805",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = {
        "spellId": "1th5Ic7ZnMmZXBtZCfR7-",
        "inputs": {
            "pregunta": pregunta
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    return response

if __name__ == "__main__":
    main()
