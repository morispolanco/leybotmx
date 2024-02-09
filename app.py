import streamlit as st
import requests
import json

def call_respell_api(pregunta, estado):
    api_key = "260cee54-6d54-48ba-92e8-bf641b5f4805"
    spell_id = "AMS1u_FAWQea7sxE6Ffu6"
    # spell_version_id = "sU33jCqGk0-RJKDxeiWif"  # Uncomment this line if you want to use a specific version

    data = {
        "spellId": spell_id,
        "inputs": {
            "pregunta": pregunta,
            "estado": estado,
        }
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    response = requests.post(
        "https://api.respell.ai/v1/run",
        headers=headers,
        data=json.dumps(data),
    )

    if response.status_code == 200:
        result = json.loads(response.content)
        return result["output"]
    else:
        st.write(f"Error: {response.status_code}")
        return None

st.title("Respell API Streamlit App")

pregunta = st.text_input("Pregunta:")
estado = st.text_input("Estado:")

if st.button("Predicción"):
    result = call_respell_api(pregunta, estado)
    if result is not None:
        st.write(f"Resultado: {result}")
