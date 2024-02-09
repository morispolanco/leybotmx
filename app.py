import requests
import json
import streamlit as st

# Replace the API key with your own
api_key = "260cee54-6d54-48ba-92e8-bf641b5f4805"

# Replace the spellId with the unique identifier of the spell you want to run
spell_id = "AMS1u_FAWQea7sxE6Ffu6"

# Replace the spellVersionId with the unique identifier of the spell version you want to run
spell_version_id = "sU33jCqGk0-RJKDxeiWif"

# Replace the inputs with the values you want to input into the spell
inputs = {
   "pregunta": "Example text",
   "estado": "Example text"
}

# Create a form in Streamlit to input the spell parameters
form = st.form("Spell Runner Form")
pregunta = form.text_input("Pregunta", inputs["pregunta"])
estado = form.text_input("Estado", inputs["estado"])

# Add a submit button to the form
form.add_button("Run Spell")

# Make a POST request to the API with the required parameters
response = requests.post(
   "https://api.respell.ai/v1/run",
   headers={
       "Authorization": f"Bearer {api_key}",
       "Accept": "application/json",
       "Content-Type": "application/json"
   },
   data=json.dumps({
       "spellId": spell_id,
       "spellVersionId": spell_version_id,
       "inputs": {
           "pregunta": pregunta,
           "estado": estado
       }
   })
)

# Print the response from the API
print(response.json())
