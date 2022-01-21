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



## 숫자, 수학 methods(Number, Math) 

### 1. toString()

10진수 ➡ 2진수 / 16진수

`숫자.toString(변수)`: 숫자를 문자로 바꿔주고 매개변수에 숫자를 넣으면 그 숫자의 진법으로 변환함

이런 숫자, 수학 메서드는 통계에서 자주 쓰임

``` js
let num = 10

num.toString()	// '10'
num.toString(2)	//	'1010'

let num2  = 255

num.toString(16)	// 'ff'
```



### 2. Math.PI

``` js
Math.PI // 3.141592653589793
```



### 3. Math.ceil(): 올림

``` js
let num1 = 5.1
let num2 = 5.7

Math.ceil(num1)	//	6
Math.ceil(num2)	//	6
```



### 4. Math.floor(): 내림

``` js
let num1 = 5.1
let num2 = 5.7

Math.floor(num1)	// 5
Math.floor(num1)	// 5
```



### 5. Math.round(): 반올림

```js
let num1 = 5.1
let num2 = 5.7

Math.round(num1)	// 5
Math.round(num1)	// 6
```

➡ 소수점자릿수 반올림

**ex 요구사항: 소수점 둘째자리 까지 표현(셋째 자리에서 반올림)**

1. 테크닉

   ``` js
   let num1 = 30.1234
   
   Math.round(num*100)/100		// 30.12
   ```

2. **toFixed()**

   ``` js
   let num1 = 30.1234
   
   num1.toFiexd(2);	// '30.12'
   num1.toFixed(0);	// '30'
   num1.toFixed(6);	// '30.123400'
   ```

   > toFixed()는 괄호안에 숫자를 넣으면 그 숫자 만큼의 소수점 이상의 수만 반환함
   >
   > 0일때: 정수부만 남음
   >
   > 소수부 보다 큰 숫자를 넣으면 남은 자리를 0으로 채워줌
   >
   > **toFixed() 는 문자열을 반환함!**



### 6. isNaN(): NaN이면 true, 나머지는 false를 반환함

``` js
let x = Number('x')	// NaN

x == NaN // false
x === NaN // false
NaN == NaN // false
isNaN(x)	// true
```

`isNaN`이 NaN 여부를 볼 수 있는 유일한 방법



### 7. parseInt(): 문자열을 숫자로 바꿔줌 (문자가 있어도 숫자를 반환해줌)

숫자가 먼저 시작해야 숫자만을 반환해줌.

두번째 인수를 받아 진수를 지정할 수 있음

``` js
let margin = '10px'

parseInt(margin)	// 10
Numner(margin)		// NaN

let redColor = 'f3'
parseInt(redColor)	// NaN 
parseIng(redColor, 16)	// 243

parseIng('11', 2)	// 3
```



### 8.parseFloat(): parseInt와 비슷하지만 부동소수점 까지 반환함

``` js
let padding = '18.5%'

parseInt(padding)	// 18
parseFloat(padding)		// 18.5
```



### 9. Math.random(): 0에서 1사이 무작위 숫자 생성

``` js
Math.random()	// 0.265874685142

// 1에서 100까지 임의의 숫자를 뽑고 싶다면

Math.floor(Math.random()*100)+1	// 마지막 +1은 앞선 결과가 floor로 버림했을 때 0이 나올수도 있기에 최솟값을 보장하기위함
```



### 10. 기타 여러가지

``` js
Math.max(1,25,8,632,6,85)	// 최댓값 반환: 632
Math.min(32,5,42,3,8,6,-3,64)	// 최솟값 반환: -3
Math.abs(-2)	// 절댓값 반환: 2
Math.pow(2,10)	// Math.pow(n, m) n의 m 거듭제곱 반환: 1024
Math.sqrt(16)	// 제곱근 반환: 4
```





## 문자열메서드

작은따옴표 ` ' `, ` " `, ``(백틱)` 로 감싸진 문자



### 1. .length: 문자열 길이 반환

``` js
let txt = '하하하하하'

txt.length // 5
```



### 2. 인덱스 접근(0부터 시작). 특정위치 바꾸는 것은 불가

``` js
let txt = '안녕하세요'
txt[2] // '하'
txt[4] = '유'
console.log(txt)	// '안녕하세요'
```



### 3. toUpperCase() / toLowerCase()

``` js
let words = "Hi guys. Nice to meet you."

words.toUpperCase()	// 'HI GUYS. NICE TO MEET YOU.'
words.toLowerCase()	// 'hi guys. nice to meet you.'
```



### 4. .indexOf(text): 문자에서 text의 위치를 반환함

``` js
let words = "Hi guys. Nice to meet you."

words.indexOf('to')	// 14 찾는 문자가 2개이상이어도 첫번째 인덱스 번호를 반환함
words.indexOf('man') // -1 해당 문자가 없으면 -1을 반환

// if문에서 사용을 조심하자
// ex
if(words.indexOf('Hi') > 0){
    console.log('포함됨')		// 여기서 Hi가 포함되어 있을 때 0을 반환하는데 부등호값을 0 초과로 하면 false를 반환하기에
    						// 첫번째 위치할 수 있으니 부등호의 값을 0이 아닌 -1로 두자
}							// 참고로 if(-1)도 true로 통과됨
```



### 5. str.slice(n, m) n부터 m까지 문자를 반환함

m 값을 넣지 않으면 끝까지 반환

양수면 그 숫자위치한 문자의 전 문자까지 반환 ex str.slice(1,5) 1부터 4까지

음수면 끝에서 부터 셈

``` js
let word = 'abcdefg'

word.slice(2)	// 'cdefg'
word.slice(0,5)	 // 'abcde'
word.slice(2,-2)	// 'cde'
```





### str.includes(word): str에 word가 들어있으면 true, 없으면 false 반환

```js
let str = '콜라'

str.includes('콜라')	// true
str.includes('사이다')	// false
```

 





### 5. str.substring(n, m): n과 m-1 인덱스 문자열을 반환함

n과 m을 바꿔도 똑같이 동작하고, 음수는 0으로 인식함

``` js
let word = 'abcdefg'

word.substring(2,5)	// 'cde'
word.substring(5,2) // 'ced'
```





### 6. str.substr(n, m): n부터 m개의 문자를 가져옴

``` js
let word = 'abcdefg'

word.substr(2,4) // 'cdef'
word.substr(-4,2) // 'de'
```





### 7. str.trim(): 앞뒤 공백 제거

``` js
let word = '   code      '

word.trim()	// 'code'
// 보통 사용자로부터 받은 입력에서 사용
```





### 8. str.repeat(n): 문자열을 n번 반복

``` js
let hello = 'Hi'

hello.repeat(4) // 'HiHiHiHi'
```





### 11. 문자열 비교

문자열을 아스키코드로 바꿔 숫자를 비교하여 구분함.

일반적으로 소문자보다 대문자가 크고, 앞문자보다 뒷문자가 크다.

#### str.codePointAt(n) / String.fromCodePoint(n)

``` js
"a".codePointAt(0)	// 97
String.fromCodePoint(97)	// "a"
```



















### 







