# Vue

> 📌 배포성공 파일은 `vue-devops` repo에 있습니다

![Vue_logo](Vue_READMD_사진/Vue_logo.png)

- ### 💡 컴포넌트 기반의 SPA를 구축할 수 있게 해주는 프레임워크

  > - `Component`: 웹을 구성하는 다양한 UI 요소. 재사용 가능하도록 구조화 한 것(`navbar`, `logo` ...)
  > - **SPA (Single Page Application)**
  >   - 단일 페이지 어플리케이션으로 하나의 페이지 안에서 필요한 부부만 로딩되는 형태
  >   - 빠른 페이지 변환 (초기 페이지 트레픽이 큼)
  >   - 페이지 변환시 적은 트래픽 양



#### vue 설치

``` bash
$ npm install -g @vue/cli
```

#### vue project 시작

``` bash
$ vue create 폴더명
```

> 프로젝트 생성시 다양한 옵션들을 추가할 수 있음 `Vuex` `Router`



#### 초기폴더구조(`router`, `vuex`X)

``` markdown
> node_modules
> public
> src
	App.vue
	>component
	>asset
	main.js
.gitignore
.babel.config.js
.package.json
.package-lock.json
README.md
```

> `npm run serve` 명령어로 App을 실행시킬 수 있음



#### Vue 컴포넌트 이해

> `Vue` 는 `App.vue`가 가장 최상단에서 하위에 속하는 모든 컴포넌트를 보여줌. `App.vue`와 다른 컴포넌트들에 속하는 모든 컴포넌트 들은 `component` 폴더에서 관리되고 `router`를 사용해서 바뀌는 페이지들은 `views` 폴더에서 관리된다.
>
> 💡 모든 `vue`파일들은 `PascalCase`로 이름을 짓는것이 관행
>
> `router` 로 바뀌는 페이지들은 `router`폴더의 `index.js`에 등록을 해야만 사용 가능함



#### Vue 파일에 data 추가하는 방법

> `data`는 함수형태로 작성한다. (컴포넌트 인스턴스에 데이터 객체를 반환하는 함수)
>
> `data`에서 브라우저의 API객체나 포로토타입 속성과 같이 자체적으로 상태동작을 가진 객체보다 단지, 컴포넌트 데이터를 나타내는 일반객체가 있는것이 좋음(상태동작 객체는 `Vuex`활용)

1. 기본적인 방법

   ``` vue
   ...
   <script>
   export default {
       data(){
           return{
   		data1: ...,
            data2: ...,
               ...
           }
       }
   }
   </script>
   ```

   

2. v-model (입력되는 정보를 즉각적으로 data에 입력하는 양방향 바인딩)

   ``` vue
   <template>
   	<div>
           <input type="text" v-model="data1" />
       </div>
   </template>
   
   <script>
   export default {
       data(){
           return{
   		data1: ...,
            data2: ...,
               ...
           }
       }
   }
   </script>
   ```

   이런 식으로 작성하면 input에 문자입력과 동시에 data에 할당됨

   

## Vue LifeCycle Hook

> 💡Vue는 DOM, Page 형성

1. `beforeCreate`(코드옵션 추가 직전)
2. `created`(computed, watch, method등을 코드옵션 완료)
3. `beforeMount`(component를 Dom에 추가하기 직전)
4. `mounted`(component가 Dom에 추가되고 난 후)
5. `beforeUpdate`(자체 렌더링 일어나기 직전)
6. updated`(자체 렌더링 끝나고 난 후)`
7. `beforeDestroy`(다른 컴포넌트로 이동하기 직전)
8. `destroyed`(완전히 컴포넌트로 이동된 직후)

총 8가지 사이클을 가짐	 

















