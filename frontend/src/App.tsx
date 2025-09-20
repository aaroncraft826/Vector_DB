import './App.css'

import SearchForm from './components/SearchForm'
import InsertForm from './components/InsertForm'

function App() {
  return (
    <>
      <h1>Aaron's Vector DB</h1>
      <div className="card">
        <InsertForm />
        <SearchForm />
        <div>
        </div>
      </div>
    </>
  )
}

export default App
