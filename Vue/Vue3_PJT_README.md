# Vue_3

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
  > 기존의 분산된 기능들을 `Setup function`으로 묶음
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



### PJT 시작

- vue create <pjtname>

  > ``` bash
  > $ vue create <appname>
  > ```
  >
  > 입력후 Select features 로 설정들 pjt에 맞게 출가 옵션 설정

- `public` 폴더에 `index.hthml`

  > `id="app"` 이라고 적힌 부분에 App.vue 가 나타나게 되고 App.vue 에서 각각의 컴포넌트들이 나타나는 구조

- `package.json`

  > 현재 PJT에 쓰이는 패키지 리스트 들이 저장되어 있는 곳

- npm run serve

  > ```bash
  > $ npm run serve
  > ```
  >
  > Vue PJT를 실행하는 명령어
  >
  > `localhost:8080`



### Vue Component 구성

템플릿, 스크립트, 스타일 로 구성

``` vue
<templates>
	<div class="name">
        My PJT {{ name }}
        Greeting {{ greeting() }}
    </div>
</templates>
<script>
    export default{
        setup(){
            const name="Hong"
            
            const greeting = (name) => {
                return 'Hello' + name;
            }
            return{
                name,
                greeting
            }
        }
    }
</script>
<style>
    .name{
        color: red;
    }
</style>
```

- template

  > Vue2 에서는 template는 무조건 하나의 엘리먼트로 구성되어야 했음.
  >
  > 3로 오면서 다중 엘리먼트가 가능해 짐
  >
  > template 자체가 하나의 div로 생각하면 편함

- 함수선언: `setup function` 에서 선언

- `ref`와 `reactive`

  >   ``` vue
  >   <templates>
  >   	<div class="name">
  >           My PJT {{ name }}
  >           Greeting {{ greeting() }}
  >           <button @click="changeName">
  >               changeName
  >           </button>
  >       </div>
  >   </templates>
  >   <script>
  >       import { ref } from 'vue'
  >       export default{
  >           setup(){
  >               const name= ref('Hong Seok Jun')
  >               
  >               const greeting = (name) => {
  >                   return 'Hello' + name;
  >               }
  >               const changeName(){
  >                   name.value = "Seok Jun Hong"
  >                   console.log(name)
  >               }
  >               return{
  >                   name,
  >                   greeting
  >               }
  >           }
  >       }
  >   </script>
  >   <style>
  >       .name{
  >           color: red;
  >       }
  >   </style>
  >   ```
  >
  >   - **ref**(숫자나 스트링 같은 자료에 사용): 변수 선언시 `ref`를 사용하여 위 코드 처럼 작성하면 `button`을 눌러서 이름을 바꾸었을 때, 화면에 즉각적인 반응이 나타남. 이것을 reactive 하다고 말함.
  >   - **reactive**(배열 또는 객체에서 사용): `const user = reactive({name: "Mike", age: 30})` 처럼 사용할 수 있고, `ref`처럼 value접근이 아닌 기존 객체나 배열처럼 키 또는 인덱스로 접근 가능
  >
  > 
  >
  > `ref`에서 배열 또는 객체를 접근하고 싶다면 변수.value.인덱스 혹은 변수.value.키값 처럼 중간에 value를 적어주고 사용하자

  
