import './App.css';

function App() {
  const name = "Tom"
  const naver ={
    url: "https://naver.com",
    name: "Naver"
  }
  return (
    <div className="App">
      <h1
        style={{
          color: "#f0f",
          backgroundColor: "green"
        }}  
      >
        Welcome! {name}
        <p>{2+3}</p>
        <a href={naver.url}>{naver.name}</a>
      </h1>
    </div>
  )    
}

export default App;
