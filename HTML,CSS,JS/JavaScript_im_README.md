# JavaScript_Immediate

## 변수

### var

1. 재 선언 가능
2. 호이스팅 됨

#### 호이스팅

> 스코프 내부 어디에서든 변수 선언은 최상위에서 선언된 것처럼 행동
>
> `let`과 `const`도 호이스팅 되지만 에러가 발생 `Reference Error`
>
> > **Temporal Dead Zone**
> >
> > ``` js
> > console.log(name) // Temporal Dead Zone 영역
> > const name = "Mike" // 함수 선언 및 할당
> > console.log(name) // 사용가능
> > ```
> >
> > 
> >
> > ``` js
> > let age = 30
> > function showAge(){
> >     console.log(age) // TDZ => Reference Error 발생
> >     let age = 20
> > }
> > showAge()
> > ```
> >
> > 호이스팅은 스코프 단위로 일어남

### 변수생성과정

1. 선언 단계
2. 초기화 단계
3. 할당 단계



#### 💡 `Refenece Error` 이유

1. `var`는 선언 과 초기화가 동시에 일어남. 따라서 할당전에 호출을 하면 `Reference Error`가 아닌 `undefined`가 나타남

2. `let` 은 선언과 초기화 단계가 분리되어 일어남.

   호이스팅 되면서 선언단계 > 실제 코드에 도달했을 때 초기화 단계( 이 시점에서 호출하면 `Reference Error`) > 할당 단계

3. `const` 선언, 초기화 할당 이 동시에 일어남 . 따라서 선언 전에 호출시 에러발생



### var 와 const, let의 차이점

| 비교   | var         | let         | const       |
| ------ | ----------- | ----------- | ----------- |
| 스코프 | 함수 스코프 | 블록 스코프 | 블록 스코프 |
|        |             |             |             |

**블록스코프**

> 코드 블록 내에서 선언한 변수는 코드 블록 내에서만 유효. 외부에서는 접근 불가
>
> `for` `if` `함수` `while` `try catch` ...

**함수스코프**

> 함수 내에서 선안한 변수만 그 지역변수.
>
> **ex** `if` 문 안에서 선언한 `var` 함수는 `if`문 밖에서도 호출 가능.
>
> 함수 안에서 선언된 `var`는 함수 밖에서 사용 불가



## 생성자 함수

보통 첫 글자를 대문자로 해서 생성

 ``` js
 function User(name, age){
     // this = {} 실제 적히지 않지만 반영되어있는 모습
     this.name = name
     this.age = age
     this.sayName = function(){
         console.log(this.name)
     }
     // return this	
 }
 
 new 함수명(매개변수1, 매개변수2 ...) // new 연산자를 사용해여 객체를 만듦
 
 let user = new User('Han', 40)
 user.sayName() // 'Han'
 ```

> `new` 를 안 쓰고 할당하면 함수만 실행됨. `console.log` 찍으면 `undefined` 찍힘

**ex**

``` js
function Item(title, price){
    this.title = title
    this.price = price
    this.showPrice = function(){
        console.log(`가격은 ${price}원 입니다`)
    }
}

const item1 = new Item('인형', 3000)
const item1 = new Item('가방', 4000)
const item1 = Item('지갑', 5000)

console.log(item1, item2, item3)
// Item{...}, Item{...}, undefined

item1.showPrcie() // 가격은 3000원 입니다
```

 

## JS Object methods / Computed Property

### Computed Property

``` js
let a = 'age'
const user = {
    name: "Mike",
    [a]: 30,
    ["인"+"사"]: "안녕"
}
console.log(user) // {name: "Mike", 'age': 30, "인사": "안녕"}

```

이처럼 대괄호를 이용해서 사용하는 값을 `Computed Property`라고 함



### Object Methods

1. Object.assign(): 객체복제

   > ```js
   > const user = {name:"Mike", age:30}
   > const cloneUser = user
   > user.name = 'Tom'
   > console.log(user)	    //{name:'Tom', age:30}
   > console.log(cloneUser)	// {name:'Tom', age:30}
   > ```
   >
   > 변수는 할당된 값을 직접 갖고있는 것이 아닌 할당된 값의 메모리 주소를 갖고있는것!
   >
   > 따라서 위와같이 코드를 작성할면 `cloneUser`는 데이터를 복제하여 갖고있는 것이 아닌 메모리 주소를 공유받은것
   > 
   >
   > ``` js
   > const newUser = Object.assign({}, user);
   > // {} + {name:'Tom', age:30}
   > const newUser = Object.assign({gender: 'male'}, user);
   > // newUser = {gender: 'male', name:'Tom', age:30}
   > console.log(user) // {name:'Tom', age:30}
   > ```
   >
   > `Object.assign` 
   >
   > 첫번째 매개변수: 초기값. 초기값에 이미 있다면 이어서 병합 
   >
   > 두번째 이후 매개변수: 병합할 값
   >
   > ``` js
   > const user = {name: "Mike"}
   > const info1 = {age: 30}
   > const info2 = {gender: 'male'}
   > 
   > console.log(Object.assign(user, info1, info2))
   > // {name: "Mike", age: 30, gender: 'male'}
   > ```

2. Object.keys(): 키배열 반환 / Object.values(): 값 배열 (숫자형 불리언도 문자형으로)반환 / Object.entries(): 각 키와 값 한 쌍씩 배열로 묶은 큰배열 반환

   > ``` js
   > const user = {name: "Mike", age: 30, gender: 'male'}
   > const userKeys = Object.keys(user)	// ["name", "age", "gender"]
   > const userValues = Object.values(user)	// ["Mike", 30, "male"]
   > const userEntries = Object.entries(user)	//[["name", "Mike"], ["age", 30], ["gender", "male"]]
   > ```

3. Object.fromEndtries(): 키 값 배열을 객체로 만들어줌 (Object.entries()와 반대의 기능을 하는 메서드)

   > ``` js
   > const user = {name: "Mike", age: 30, gender: 'male'}
   > const arr = Object.entries(user)
   > const reverseArr = Object.fromEntries(arr)	// {name: "Mike", age: 30, gender: 'male'}
   > ```




## 심볼 Symbol

``` js
const a  = Symbol();
```

### 💡 유일한 식별자를 만듦! 

``` js
const id = Symbol('id');	// new 안붙임
const id2 = Symbol('id');

console.log(id) // Symbol(id)
console.log(id2) // Symbol(id)
console.log(id === id2) // false
```

> - 유일성 보장
> - 전체 코드중에 딱 하나
> - 같은 설명으로 만들어도 동등연산시 false

#### property key: 심볼형

``` js
const id = Symbol('id')
const user = {
    name: "Mike",
    age: 30,
    [id]: "myid"
}

// user
// {name: "Mike", age: 30, Symbol(id): "myid"}
// user[id] = "myid"

//Object.keys(user)		["name", "age"]
//Object.values(user)	 ["Mike", 30]
//Object.entires(user)		[Array(2), Array(2)]
```

> `Object` 메서드를 사용하면 `key`가 `Symbol`형인 `property`는 건너뜀

#### 어디서 사용하나

➡ 특정객체에 원본을 건드리지 않고, 속성을 추가할 수 있음.

코드가 길어질수록 원본객체 또는 상단 코드에 내가 만든 식별자와 같은 네이밍을 한 식별자가 있을 수 있음. 이럴 때 `Symbol`객체를 사용하여 오류를 피할 수 있음



**Symbol.for(식별자이름): 전역심볼**

> - 하나의 식별만 보장받을 수 있음
> - 없으면 만들고, 있으면 가져오기 때문
> - `Symbol`함수는 매번 다른 `Symbol`값을 생성하지만,
> - `Symbol.for` 메서드는 하나를 생성한 뒤 키를 통해 같은 `Symbol`을 공유 
>
> ``` js
> const id = Symbol.for('id');
> const id2 = Symbol.for('id'); 
> 
> id === id2		// true
> Symbol.keyFor(id2)		// "id"
> ```
>
> ketFor(변수)를 사용하여 생성할 때 만들었던 이름을 얻을 수도 있음
>
> 전역심볼이 아닌 심볼은 keyfor를 사용할 수 없음
>
> ➡ `심볼이름.decription`
>
> ``` js
> const id = Symbol('id입니다')
> id.description;		// "id입니다"
> ```



#### 객체에 숨겨진 Symbol key 보는 방법

``` js
const id = Symbol('id')
const user = {
    name: "Mike",
    age: 30,
    [id]: "myid"
}

Object.getOwnPropertySymbols(user);		// [Symbol(id)] 심볼들만 보는 메서드
Reflect.ownKeys(user);		//	["name", "age", Symbol(id)]	심볼을 포함한 객체의 모든 키를 보여줌
```













