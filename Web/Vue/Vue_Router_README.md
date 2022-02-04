# Vue_Router

![Vue_logo](Vue_README_사진/Vue_logo.png)

#### router/index.js 에 컴포넌트를 선언해 매핑하는 렌더링 방식.



### router 사용방법

1. plugin 설치

   ``` bash
   $vue add router
   ```

2. pjt생성시 옵션에서 추가하기

router를 설치하면 `App.vue` 에 코드가 새로 추가됨

``` vue
...
<router-link to="/">Home</router-link>
<router-link to="/about">About</router-link>
<router-view/>
...
```

**<router-link>**: 목표 경로를 `to`로 지정하여 움직이게 하는 컴포넌트

- `to` 로 이동할 경로 지정. 일반적으로 a 태그 처럼`GET`요청을 보내는 것과 다르게 `GET`요청을 보내는 이벤트를 제거한 형태로 구성.
- `to`는 `to="{name:Home}"` 과 같이 name으로 router 요소를 전달할 수 있음. **선언적방식**

**<router-view/>**: 주어진 라우터 컴포넌트를 렌더링 하는 컴포넌트. 실제 컴포넌트가 DOM에 부착되어 보이는 자리

**History mode**

- 브라우저의 url이동 히스토리는 남기지만 실제로 페이지가 전환되지 않는 기능. (페이지 재 로드 없음)
- SPA의 단점인 URL이 변경되지 않음을 해결



**name route**

- 이름을 가진 라우트

- router/index.js에 명명된 이름을 따라 해당 url로 이동함

  ``` js
  // router/index.js
  ...
  import Home from '../views/Home.vue'	// 매핑하고자 하는 컴포넌트 import
  const route = [
      {
          path: '/',
          name: 'Home',	// name route
          component: Home
      }
  ]
  ```

  #### template에서 사용하기 (선언적 방식)

  ``` vue
  <router-link :to="{name: 'Home'}">Home</router-link>
  ```

  #### script에서 사용하기 (프로그래밍 방식)

  ``` js
  this.$router.push({name:'Home'})
  ```



**동적인자 전달(params, query)**

- url에 파라미터 또는 쿼리를 담아 넘기는 경우 사용(보통 유저 프로필 페이지는 유저마다 다르게 렌더링 되어야 하기에 파라미터를 사용)

- 콜론으로 시작함

- 컴포넌트에서 `$route.params.동적인자이름`로 접근

  ``` js
  // router/index.js
  ...
      {
          path: '/user/:userId',
          name: 'userProfile',	// name route
          component: userProfile
      }
  ]
  ```

  #### template에서 접근

  ``` vue
  <router-link :to="{name: 'userProfile', params: {userId: $route.params.userId}}">프로필페이지</router-link>
  ```

  

  #### script에서 접근

  ``` js
  ...
  this.$route.params.userId
  ```

  

**Vue Router 의 필요성**

- SPA 등장 이전 여러 페이지를 렌더해야할 때 서버거 모든 라우팅을 통제하고 요청 경로에 맞는 html파일을 제공했음

- SPA 등장 이후 서버는 index.html만 제공하고 html파일 위에 JS코드를 활용해 보여주는 view를 변경함

  ➡ 요청에 대한 처리를 서버가 하지 않음 ➡ SSR(라우팅 결정권: 서버)에서 CSR(라우팅 결정권: 클라)로 변화









