import './App.css';
import React, {useState} from 'react'
import { axiosClient } from './lib/fetch/ApiClient';

function App() {

  const [loading, isLoading] = useState(false)
  const [results, setResults] = useState(null)

  async function getData() {
    return await axiosClient.get(`/api/v1/data/show`)
    .then(function(req) {
      return req.data;
    })
    .catch(function (error) {
        console.log(error);
    })
  }

  async function handleClick() {
    isLoading(true)
    const res = await getData();
    console.log(res)
    setResults(res)
    isLoading(false)
  }

  return loading ? (
    <div className="loading">
      Loading
    </div>
  ) : (
    <div className="App">
      It works
      {/* <input type="text" placeholder='name'></input> */}
      <button onClick={handleClick}>Show data</button>
      {results && JSON.stringify(results, null, 2)}
    </div>
  );
}

export default App;
