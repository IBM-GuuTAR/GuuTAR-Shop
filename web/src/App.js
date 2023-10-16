import { useEffect, useState } from 'react'

import './App.css';
import ProductCard from './components/ProductCard';
import AddProduct from './components/AddProduct';
import { BACKEND_ENDPOINT } from './config/config';

function App() {

  const [isShowAddProduct, setIsShowAddProduct] = useState(false)
  const [items, setItems] = useState([])
  const [greeting, setGreeting] = useState("No greeting message")

  useEffect(() => {
    const fetchProductData = async () => {
      const rawData = await fetch(`${BACKEND_ENDPOINT}/api/items/get-items`)
      const response = (await rawData.json())?.data

      if (response) {
        const { items } = response
        setItems(items)
      }
    }

    const fetchGreetingMsg = async () => {
      const rawData = await fetch(`${BACKEND_ENDPOINT}/api/greeting/`)
      const response = (await rawData.json())?.data

      if (response) {
        const { greeting } = response
        setGreeting(greeting)
      }
    }

    fetchGreetingMsg()
    fetchProductData()
  }, [])
  
  return (
    <div className="App">
      {/* <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header> */}

      <div className="Root">
        <h1>GuuTAR Shop</h1>
        <div>
          <h3>Greeting Message</h3>
          <p>{greeting}</p>
        </div>
        {isShowAddProduct ? <AddProduct setIsShowAddProduct={setIsShowAddProduct} /> :  <div className="FlexRow">
          <button onClick={() => setIsShowAddProduct(true)}>Add new product</button>
        </div>}
        <h3>Product List</h3>
        <div className="FlexRow" style={{ gap: 16 }}>
          {items.map(item => <ProductCard key={item.id} {...item} />)}
        </div>
        <div></div>
      </div>
    </div>
  );
}

export default App;
