import React from 'react';
import { useState } from 'react-redux';
import { fetch } from 'vercel';

const App = () => {
  const [state, setState] = useState({
    spellId: 'ams1u_FAWQea7sxE6Ffu6',
    spellVersionId: 'sU33jCqGk0-RJKDxeiWif',
    inputs: {
      pregunta: 'Example text',
    estado: 'Example text',
    },
  });

  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('https://api.respell.ai/v1/run', {
      method: 'POST',
      headers: {
        // This is your API key
        authorization: 'Bearer 260cee54-6d54-48ba-92e8-bf641b5f4805',
        'Accept': 'application/json',
        'content-type': 'application/json',
      },
      body: JSON.stringify({
        spellId: 'ams1u_FAWQea7sxE6Ffu6',
        // This field can be omitted to run the latest published version
        spellVersionId: 'sU33jCqGk0-RJKDxeiWif',
        inputs: {
          pregunta: 'Example text',
        estado: 'Example text',
        },
      }),
    })
      .then(response => response.json())
      .then(data => {
        setState({ spellId, spellVersionId, inputs });
      })
      .catch(error => setError(error));
  }, []);

  return (
    <div>
      <h1>Vercel App</h1>
      <form onSubmit={handleSubmit}>
        <label for="pregunta">pregunta:</label>
        <input type="text" id="pregunta" name="pregunta" onChange={(e) => setState({ pregunta: e.target.value })} />
        <label for="estado">estado:</label>
        <input type="text" id="estado" name="estado" onChange={(e) => setState({estado: e.target.value })} />
        <label for="inputs">Inputs:</label>
        <input type="text" id="inputs" name="inputs" onChange={(e) => setState({ inputs: data })} />
       
