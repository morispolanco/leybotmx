import streamlit as st
import requests

import requests
import json

response = requests.post(
  "https://api.respell.ai/v1/run",
  headers={
    # This is your API key
    "Authorization": "Bearer 260cee54-6d54-48ba-92e8-bf641b5f4805",
    "Accept": "application/json",
    "Content-Type": "application/json"
  },
  data=json.dumps({
    "spellId": "AMS1u_FAWQea7sxE6Ffu6",
    # This field can be omitted to run the latest published version
    "spellVersionId": "sU33jCqGk0-RJKDxeiWif",
    # Fill in values for each of your 2 dynamic input blocks
    "inputs": {
      "pregunta": "Example text",
      "estado": "Example text",
    }
  }),
)

# Display the UI of the app
print(response.text)
