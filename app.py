import streamlit as st
import requests
import json

def run_respell_api(api_key, question, state):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    data = json.dumps({
        "spellId": "AMS1u_FAWQea7sxE6Ffu6",
        "inputs": {
            "pregunta": question,
            "estado": state
        }
    })

    response = requests.post(
        "https://api.respell.ai/v1/run",
        headers=headers,
        data=data
    )

    if response.status_code == 200:
        return json.load(response.content)["output"]
    else:
        return "Error: " + str(response.status_code)

def main():
    st.title("Respell AI Streamlit App")

    api_key = st.text_input("API Key")
    question = st.text_input("Question")
    state = st.text_input("State")

    if st.button("Run Respell API"):
        result = run_respell_api(api_key, question, state)
        st.write("Result:", result)

if __name__ == "__main__":
    main()
