import './App.css';
import Hello from './component/Hello';
// import Welcome from './component/Welcome';
import styles from './App.module.css';
function App() {
  return( 
    <div className="App">
      <Hello />
      <div className={styles.box}>App</div>
    </div>
  )
}
// 개발자도구로 보면 컴포넌트이름_클래스(아이디)명_해시값 으로 스타일이 적용됨
// 따라서 style 네이밍 중복, 상속 등 걱정을 안할 수 있음
// 컴포넌트명.module.css 라고 작성한 css파일을 생성
export default App;
