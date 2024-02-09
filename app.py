import streamlit as st
import requests
import json

# Set the title of the app
st.title("Respell AI App")

# Create a form to get the inputs
with st.form("my_form"):
    pregunta = st.text_input("Pregunta")
    estado = st.text_input("Estado")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        # Make the API call
        response = requests.post(
            "https://api.respell.ai/v1/run",
            headers={
                "Authorization": "Bearer 260cee54-6d54-48ba-92e8-bf641b5f4805",
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "spellId": "AMS1u_FAWQea7sxE6Ffu6",
                "spellVersionId": "sU33jCqGk0-RJKDxeiWif",
                "inputs": {
                    "pregunta": pregunta,
                    "estado": estado,
                }
            }),
        )

        # Print the response
        st.write("Response:")
        st.markdown(f"```json\n{json.dumps(response.json(), indent=4)}\n```")
