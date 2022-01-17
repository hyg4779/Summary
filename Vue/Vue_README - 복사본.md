#### 실전형 README에 작성할 문구

-------

#### Vue 컴포넌트 이해

> `Vue` 는 `App.vue`가 가장 최상단에서 하위에 속하는 모든 컴포넌트를 보여줌. `App.vue`와 다른 컴포넌트들에 속하는 모든 컴포넌트 들은 `component` 폴더에서 관리되고 `router`를 사용해서 바뀌는 페이지들은 `views` 폴더에서 관리된다.
>
> 💡 모든 `vue`파일들은 `PascalCase`로 이름을 짓는것이 관행
>
> `router` 로 바뀌는 페이지들은 `router`폴더의 `index.js`에 등록을 해야만 사용 가능함

----------------------------

# Vue

![Vue_logo](Vue_READMD_사진/Vue_logo.png)

- ### 💡 컴포넌트 기반의 SPA를 구축할 수 있게 해주는 프레임워크

  > - `Component`: 웹을 구성하는 다양한 UI 요소. 재사용 가능하도록 구조화 한 것(`navbar`, `logo` ...)
  > - **SPA (Single Page Application)**
  >   - 단일 페이지 어플리케이션으로 최초의 페이지 로딩 후 필요한 부분만 동적으로 `DOM` 형성
  >   - 빠른 페이지 변환 (초기 페이지 트레픽이 큼)
  >   - 페이지 변환시 적은 트래픽 양
  > - 동작원리의 일부가 CSR(Client Side Rendering)의 구조를 따름
  >   - 서버에서 화면구성(SSR)을 하는 것이 아닌 클라이언트 측에서 구성 (서버와 트래픽 감소 / UX 향상)
  >   - 최초 요청시 HTML, CSS, JS 등 데이터를제외한 각종 리소스를 응답받고 이후에는 클라이언트 측에서 필요한 데이터만 요청해 JS로 DOM을 렌더링 하는 방식
  >   - 처음에 뼈대만 받고 브라우저 동적으로 DOM을 형성(SPA)
  
- ### MVVM Pattern

  - 앱 로직을 UI로부터 분리하기 위해 설계된 디자인 패턴

  - Model / View / ViewModel 구성

    - Model

      > Javascript Object. 즉, Vue Instance에서 data. 이 데이터가 바뀌면 View(DOM)dlm qksdmd

    - View

      > DOM. data에 따라 바뀌는 대상

    - View Model

      > 모든 View Instance.
      >
      > View와 Model 사이에서 Data와 DOM관련된 모든 일을 처리. DOM을 구성하는 과정

**CDN**

```html
<script src="https://cdn.jsdeliver.net/npm/vue/dist/vue.js"></script>
```

**npm**

```bash
$ npm install vue@next
```

**인스턴스 생성 ex**

``` html
<div id="app">
    <span v-bind:title="msg">Hello World!</span>
    <p v-if"seen">
         can u see me?
    </p>
    <ol>
        <li v-for="todo in todos">
        	{{todo.text}}
        </li>
    </ol>
    <p>
        {{Greeting}}
    </p>
    <button v-on:click="reverseGreeting">
        인삿말 뒤집기
    </button>
    <p>
        {{bindingData}}
    </p>
    <input v-model="bindingData">
</div>
```

```js
const app = new Vue({
    el:'#app',
    data(){	
        return{
            msg: '지금 시간은' + new Date() + '입니다.', 
            seen: true,
            todos:[
                text: 'Hi',
                text: 'Hello',
                text:  'Hey',
            ],
            Greeting: 'Hellow',
            bindingData: '안녕 Vue!'
        }
    },
    methods:{
        reverseGreeting(){
            this.Greeting = this.Greeting.split('').reverse().join('')
        }
    }
})
```





## Vue DOM (template 와 render)

> `template`: data, methods, computed ... 등 연결되어 있는 HTML 마크업 문서
>
> `render`:  `template`와 연결되어있는 data를 불러오는 function
>
> DOM 이 형성된다 ➡ `template`가 `render`된다



## Vue LifeCycle Hook

![Vue_LifeCycle_Hook](Vue_READMD_사진/Vue_LifeCycle_Hook.PNG)

1. `beforeCreate`(코드옵션 추가 직전)
2. `created`(computed, watch, method등을 코드옵션 완료)
3. `beforeMount`(component를 Dom에 추가하기 직전)
4. `mounted`(component가 Dom에 추가되고 난 후)
5. `beforeUpdate`(자체 렌더링 일어나기 직전)
6. updated`(자체 렌더링 끝나고 난 후)`
7. `beforeDestroy`(다른 컴포넌트로 이동하기 직전)
8. `destroyed`(완전히 컴포넌트로 이동된 직후)

> 총 8가지 사이클을 가짐. methods, computed 처럼 lifecycle 훅 때마다 DOM 동작을 설정할 수 있음.
>
> Life Cycle Hook은 Component 별 데이터의 생성과정이 많아지고 비동기적으로 움직이는 데이터를 관리할 때 매우 중요한 개념!
>
> **ex**
>
> ``` js
> Vue.createApp({
>   data() {
>     return { count: 1 }
>   },
>   created() {
>     console.log('count is: ' + this.count) // => "count is: 1"
>   }
> })
> ```





## Vue  Data

> `data`는 함수형태로 작성한다. (컴포넌트 인스턴스에 데이터 객체를 반환하는 함수)
>
> `data`에서 브라우저의 API객체나 포로토타입 속성과 같이 자체적으로 상태동작을 가진 객체보다 단지, 컴포넌트 데이터를 나타내는 일반객체가 있는것이 좋음(상태동작 객체는 `Vuex`활용)



## 템플릿 문법

1. 문자열 이중괄호 구문

   ``` html
   <span>메세지: {{msg}}</span>
   ```

2. 속성접근 Directive

   ``` html
   <div v-bind:id="dynaminId"></div>
   ```

   > `v-` 방식으로 나타냄 `Directive 문법 따로 정리함`

3. Javascript 표현식 사용 가능

   > `{{ number + 1}}` / `{{ message.split('').reverse().join('') }}`




## 스크립트 문법

#### 📌모든 Vue Instance는 여러 옵션을 사용하여 새 인스턴스를 구성함 (Vue Instance == Vue Component)

**ex**

``` html
<div id="app">
    <button @click="myFuncA">a</button>
    <button @click="myFuncB">b</button>
</div>
<script src="https://cdn.jsdeliver.net/npm/vue/dist/vue.js"></script>
<script>
	const app = new Vue({
        el: '#app',
        data(){
            return({
                a: 1,
            })
        },
        methods:{
            myFuncA(){
                console.log(this) // Vue Instance
            },
            myFuncB: () => {
                console.log(this) // window
            }
        }
    })
</script>
```

> 1. `el`: `template`에 요소와 연결(마운트)하는 DOM 엘리먼트
> 2. `data`: 함수형으로 작성됨. `return`으로 `data`를 `object` 형태로 반환. Vue Instance 내에서 this키워드로 접근 가능
> 3. `methods`: Vue instance에 추가하는 메서드
> 4. `this`: JS 문법을 잘 보고 오자!



## Directive (디렉티브)

> #### v 접두사가 있는 특수 속성
>
> - 전달인자 (Arguments)
>
>   - `:` 을 통해서 전달인자를 받을 수 있음
>
>   - 전달받는 인자는 큰따옴표로 작성
>
>     ``` html
>     <a v-bind:href="url">...</a>
>     ```
>
>     `v-bind:href` 를 `:href` 로 줄여서 사용 가능
>
> - 수식어 (Modifier)
>
>   - `.` 으로 표시되는 접미사로 directive를 바인딩 할 때 나타냄



### 1. v-html

> ``` html
> <p>{{rawHtml}}</p>
> <p><span v-html>{{rawHtml}}></span></p>
> ```
>
> `p태그` 안의 `span태그` 값은 `rawHtml`값으로 대체됨. 웹사이트의 임의의 HTML을 동적으로 렌더링 한다면 **XSS 취약점**으로 이어질 수 있으니 `v-html`은 사용을 자제하는 것이 좋다
>
> **XSS 취약점 (Cross Site Scripting)**
>
> 사용자가 보는 웹페이지를 클라이언트 측에서 스크립트를 삽입 할 수 있다. `XSS`은 심각한 경우 공격자가 사이트의 데이터를 제어할 수 있어 심각한 보안 위험요소이다.



### 2. v-text

> ```vue
> <template>
> 	<div id="app">
>         <p v-text="msg"></p>
>     </div>
> </template>
> <script>
>     const app = new Vue({
>         el: "#app",
>         data(){
> 			return{
>                 msg: "Hello"
>             }
>         }
>     })
> </script>
> ```
>
> 엘리먼트의 textContent를 template에 나타냄



### 3. v-show

> 조건부 렌더링
>
> `Fasle`일 경우에도 엘리먼트는 항상 렌더링 됨. CSS속성이 `hidden` 임.

### 4. v- if / v-else / v-else-if

>  조건부 렌더링
>
> `False`일 경우 렌더링이 되지 않음. (자주 토글하는 요소에는 렌더 비용 증가)



### 5. v-for

> `item in items` 구문처럼 사용. 항상 `:key` 속성을 같이 사용하도록 함
>
> `item`가 배열이면 `index`를 `key`로사용하여 활용할 수 있음.
>
> `items`가 `Object` 이면 `key`로 `:key`를 사용할 수 있음
>
> 💡 `v-if` 와 같이 사용할 시 `v-for`구문의 우선순위가 더 높아 무시될 수 있음. 따라서 같이 사용은 지양하자
>
> #### 배열의 v-for 구문
>
> ``` html
> <ul id="example-2">
>   <li v-for="(item, index) in items">
>     {{ parentMessage }} - {{ index }} - {{ item.message }}
>   </li>
> </ul>
> ```
>
> ``` js
> var example2 = new Vue({
>   el: '#example-2',
>   data: {
>     parentMessage: 'Parent',
>     items: [
>       { message: 'Foo' },
>       { message: 'Bar' }
>     ]
>   }
> })
> ```
>
> 출력
>
> - Parent-0-Foo
> - Parent-1-Bar
>
> 
>
> #### Object의 v-for 구문
>
> ``` html
> <ul id="v-for-object" class="demo">
>   <li v-for="(index, name, value) in object">
>     {{ index.name: value }}
>   </li>
> </ul>
> ```
>
> 
>
> ``` js
> new Vue({
>   el: '#v-for-object',
>   data: {
>     object: {
>       title: 'How to do lists in Vue',
>       author: 'Jane Doe',
>       publishedAt: '2016-04-10'
>     }
>   }
> })
> ```
>
> 출력
>
> - 0.title: How to do lists in Vue
> - 1.author: Jane Doe
> - 2.publishedAt: 2016-04-10



### 6. v-on 

> 엘리먼트에 이벤트 리스너를 연결하여 사용
>
> shorthand: `@`
>
> `v-on:submit="enterTheInput"`➡`@submit="enterTheInput"`
>
> ``` html
> <input type="text" />
> <button @submit="enterTheInput">
>     Enter
> </button>
> ```



### 7. v-bind

> Vue의 data 값을 할당
>
> `Object`형태로 사용하면 value가 `true`인 `key`가 `class`에 할당됨
>
> shorthand: `:`
>
> ``` html
> <div :class="{active: todo.isTrue}">
> </div>
> <li :style="{ fontSize: fontSize + 'px'}"
> ```



### 8. v-model

> `html` 요소값과 `data` 양방향 바인딩
>
> ``` html
> <input type="text" v-model="checked" />
> <label>{{checked}}</label>
> ...
> <script>
> data(){
> 	return{
> 	checked: true,
> 	}
> }
> </script>
> ```
>
> `v-model` 뒤에 `.lazy` / `.number` / `.trim` 수식어를 붙이면 추가 기능 가능
>
> `lazy`: `change` 이벤트 이후에 동기화 할 수 있음
>
> `number`: 사용자 입력이 자동으로 숫자 형변환 일어남. 주로 `input` 태그에서 일어남
>
> `trim`: 입력된 값이 자동으로 `trim`됨



### 9. computed

> 데이터 기반 계산된 속성
>
> 함수의 형태로 정의하지만 반환값이 바인딩 됨 **꼭 반환값이 있어야함!!**
>
> #### 종속된 데이터가 변경될 때만 함수 실행



### 10. watch

> 데이터를 감시하고 감시하는 데이터에 변화가 일어날 때만 실행되는 함수
>
> **computed 는 종속된 데이터가 변하면 실행하여 반환값이 있는 선언형 프로그래밍 **
>
> **watch는 특정 데이터의 변화값을 보고 다른 data를 바꿀때 주로 사용 명령형 프로그래밍**
>
> #### 특정값이 변동하면 다른 작업을 한다. 특정 변화에 대한 트리거



### 11. filters

> `interpolation` 또는 `v-bind`를 이용할 때 사용가능
>
> JS표현식처럼 `|` 파이프를 함께 추가하여 사용 **chaining 가능**
>
> ``` html
> <div>
>     <p>{{ numbers | oddNumbers | higherTen }}</p>
> </div>
> ...
> <script>
> ...
> filters:{
>     oddNumbers(args){
>         const oddNums = args.filter(function(arg){
>             return arg%2
>         })
>     },
>     higherTen(args){
>         const highNums = args.filter(function(arg){
>           return arg > 10  
>         })
>     }
> }
> </script>
> ```





## Vue3 가 Vue2와 달라진점

- Composition APi를 기본적으로 지원

  > 기존 2.0에서는 Component의 옵션을 `Data` `Computed` `Methods` `Watch` 로 구분해 보다 직관적인 느낌을 줌.
  >
  > ➡ 컴포넌트의 크기가 커질수록 각각의 코드를 위 아래로 읽어야해 이해도와 가독성 저하
  >
  > 
  >
  > #### 📌Composition API
  >
  > 기존의 분산된 기능들을 `Setup`으로 묶음
  >
  > `Reactive` `Ref` `Methods` `Computed`

- Life Cycle Hook 변화

  > 이전에 `Created` `Mounted` `Updated` 메서드를 사용했음. **Composition API**로 들어가면서 명칭이 바뀜.
  >
  > `created` : `setup`이 실행되자마자 실행
  >
  > `mounted` : `onMounted`로 바뀜
  >
  > `updated`: `onUpdated`로 바뀜

- templated 생성시 루트 엘리먼트가 2개이상 가능

  > 이전에는 `template` 안에 하나의 `element`만 가능했지만 3.0.부터 2개 이상이 가능

- 인터넷 익스플로러 지원 중단





