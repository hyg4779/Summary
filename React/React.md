# React_voca app 만들기

``` bash
$ create-react-app voca
...
  npm start
    Starts the development server.

  npm run build
    Bundles the app into 
static files for production.

  npm test
    Starts the test runner.


  npm run eject
    Removes this tool and copies build dependencies, configuration files
    and scripts into the app directory. If you do this, you can’t go 
back!

We suggest that you begin by typing:

  cd voca
  npm start

Happy hacking!
```

> voca 폴더에서 `VScode`실행



## 📌프로젝트 진행 전 사전 학습



#### 초기 폴더구조

``` markdown
> node_modules		# 프로젝트에 사용되는 dependency module들이 모여있음
> public			# index.html 파일이 있는 곳
> src				# App.js 가 있는 곳
	.gitignore
	package-lock.json
	package.json	# 설치된 모듈들 이름이 적혀있음
	README.md
```



### React PJT 유의사항

- 리액트로 만든 페이지는 컴포넌트로 구성되어 있음(JSX 문법)
- 모든 컴포넌트는 함수컴포넌트 이며 대문자로 시작(함수로 만들어진 컴포넌트)
- 컴포넌트는 `src` 폴더에서 `component` 폴더를 만들어 생성

> JSX: js에서 html 태그를 작성 하는 문법(JS XML) 



#### src 폴더

```markdown
>component
	Hello.js
	World.js
App.js
App.css
index.js
index.css
...
```



#### index.js

``` jsx
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';	// App 컴포넌트 호출
import reportWebVitals from './reportWebVitals';

ReactDOM.render(		// React DOM 생성하여 render
  <React.StrictMode>
    <App /> 		// App 컴포넌트를 보여줌
  </React.StrictMode>,
  document.getElementById('root')	// HTML 파일에 'root' 를 id명으로 쓰는 곳에 render
);

...중략...

reportWebVitals();

```



#### App.js

``` jsx
import './App.css';
import Hello from './component/Hello';		// Hello 컴포넌트 호출
function App() {
  return( 
    <div className="App">
      <Hello />			// Hello 컴포넌트
      <div className={styles.box}>App</div>
    </div>
  )
}
export default App;
```



#### component 생성방법

컴포넌트 폴더를 만들고 컴포넌트.js  파일 작성법

``` jsx
1.
const Hello = function(){
    ...
}
export default Hello;
    
    
2.
const Hello = () => {
    ...
}
export default Hello;
    
    
3.
export default function Hello(){
    ...
}
```

**component 작성법**

``` jsx
import World from './World'

export default function Hello{
    return (
    	<div>
        	<h1>Hello!!</h1>
        	<World />
            <World />
        </div>
    )
}
```

- return 안에서는 하나의 태그만 가능 ➡ div 태그로 감싸서 하나의 태그처럼 사용
- 컴포넌트 안에 동일레벨 다른 컴포넌트를 사용할 수 있음
- 여러 컴포넌트를 사용할 수 있고, 같은 컴포넌트 중복사용 가능
- 컴포넌트를 호출시 `import` 하고 `<World />` 처럼 self close 해서 사용



#### Style 적용방법

1. App.module.css 활용

   1. src 폴더에서 App.module.css 파일생성

      > - CSS 파일은 꼭 `컴포넌트 명.module.css` 로 생성
      > - 컴포넌트와 동일한 폴더레벨에서 생성

   2. App.js 에서 호출 (import styles from '경로')

      ``` jsx
      import styles from './App.module.css';
      ...
      		<div className={style.box}>
                  App
      		</div>
      ```

      > #### 💡 이 방식의 장점
      >
      > 개발자도구로 확인시 클래스명이 `컴포넌트이름_클래스명_해시값` 으로 적용됨.
      >
      > 따라서 style 네이밍 중복, 상속 같은 이슈가 발생하지 않음
      >
      > + 컴포넌트 별 style관리가 쉬워짐

2. Inline 방식

   ``` jsx
   <div>
       <h1 style={
           {
           	color: '#f00',
           	borderRight: '2px solid #000',
           	marginBottm: "50px",
           	opacity: 1,
       	}
       }>
           Home
   	</h1>
   ```

   - 태그 안에서 Inlin 방식으로 작성
   - 각 속성들은 `camelCase`로 작성
   - 속성값은 따옴표로 적음 (숫자는 따옴표 없이 가능)

   > 특별한 경우가 아니면 추천하지 않음

3. index.css 와 App.css 활용

   - 각 css파일에 들어가서 클래스를 추가하여 사용.

   - index.css는 모든 컴포넌트에 적용되게 하는 속성

   > 💡 `App.css` 또는 `index.css` 에 적고 Component 별 css파일이 따로 있는 경우, 클래스명이 중복될 시 오버라이딩 됨
   >
   > 개발자 도구를 보면 header에서 style들이 적히는데, 마지막으로 언급된 style이 적용됨



#### Event 적용

1. 선언후 사용

   ``` jsx
   export default function Hello() {
       function showName(){
           console.log("Mike")
       }
       return(
       	<div>
           	<button onClick={showName}></button>
           </div>
       )
   }
   ```

   - 함수와 Event 는 `camelCase`로 작성

2. Event에서 바로 사용

   ``` jsx
   <div>
   	<button
           onClick={function showAge(){
           	console.log(30)
               }
           }>Show Age
       </button>
   </div>
   ```

   - 화살표 함수도 가능

     ``` markdown
     ex.
     onClick={()=>{
         ...
     }}
     ```

3. 매개변수 사용

   ``` jsx
   <input type="text" onChange={(e)=>{
           const txt = e.target.value
           console.log(txt)
       }}
   ```

   





