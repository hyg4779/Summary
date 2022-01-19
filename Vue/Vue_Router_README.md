# Vue_Router

![Vue_logo](Vue_READMD_사진/Vue_logo.png)

### route.js 에 `.Vue`를 주소와 같이 선언해 매핑하는 렌더링 방식.

### route 사용방법

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

> <router-link>(템플릿문법)
>
> `to` 로 이동할 경로 지정. 일반적으로 a 태그 처럼`GET`요청을 보내는 것과 다르게 `GET`요청을 보내는 이벤트를 제거한 형태로 구성.
>
> `to`는 `to="{name:Home}"` 과 같이 name으로 router 요소를 전달할 수 있음. **선언적방식**
>
> ``` vue
> <router-link :to="{name:"room", params:{userId: this.roomId}}">SearchPage</router-link>
> <!--parameter 포함하여 보내는 방식!-->
> <router-link :to="{name:"room", query:{grout: 'member', category: 'trail'}}">SearchPage</router-link>
> <!--parameter 포함하여 보내는 방식!-->
> <!-- url뒤에 ?group=member&category=trail 식으로 물음표 문자와 함께 쿼리가 들어감 !-->
> ```
>
> > **프로그래밍 방식**
> >
> > `$router.push(...)` Vue 인스턴스 내부에서 `$router`로 라우팅을 할수 있음.
> >
> > **예시 (script)**
> >
> > ``` js
> > router.push('home')		// 문자열 path
> > router.push({path:'home'})		// object 형 path
> > router.push({name:"room", params:{userId: this.roomId}})	// name선언 + parameter 함께 보내기
> > router.push({path:"profile", query:{info:indivisual}})		// object형 + query 함께  예시: /profile?info=indivisual
> > ```
>
> <router-view/>
>
> router.js에 등록된 라우트들을 보여주는 **컴포넌트**. `router-link`를 누르면 해당 연결된 컴포넌트를 보여주는 위치

router/index.js 폴더와 파일이 생성된다

**router/index.js**

``` js
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    {
        path: '/about',
        name: 'About',
        // ...
        component: () => import('../views/About.vue')
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
```

> 라우팅할 페이지들을 모두 등록하는 파일. 등록하지 않은 vue파일은 라우팅이 되지않음(오류)
>
> `History mode`
>
> 브라우저의 url이동 히스토리는 남기지만 실제로 페이지가 전환되지 않는 기능. (페이지 재 로드 없음)
>
> SPA의 단점인 URL이 변경되지 않음을 해결



### 동적 인자(파라미터 or 쿼리)  사용하기

1. route/index.js 에서 path 작성시 콜론을 붙여서 사용

   ``` js
   path: '/lotto/:lottoNum'
   ```

2. Component 에서 `$route.params.인자명` 으로 사용 가능

   ``` vue
   <template>
       <h2>
           {{$route.params.lottoNum}}
       </h2>
   </template>
   <script>
   ...
   	const numbers = _.sampleSize(nums, this.$route.params.lottoNum)
   </script>
   ```

