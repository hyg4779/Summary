# Javascript



## 변수

> 변수 선언시 규칙
>
> - 예약어를 변수로 설정 불가 (error)
> - 문자, 숫자, `_`, `$`  사용 가능
> - 첫 글자로 숫자 사용 불가
> - 상수값을 가진 변수는 되도록 대문자로 변수명 선언
> - 파악하기 쉬운 변수명 지정
>
> ``` js
> name = "Mike"
> name = "Tom"
> // 최종적으로 name이라는 변수는 'Tom' 이라는 단어로 재 할당 됨
> ```
>
> 

### 변수 선언시 쓰는 키워드

1. const

> - 재할당 불가능
> - 주로 바뀌지 않는 상수값을 넣을 때 사용

2. let

> - 재 할당 가능
>
>   ``` js
>   let num = 2
>   num = 3
>   ```
>
>   재 할당할 때는 `let` 표기 안함



## 자료형

1. 문자형 (큰 따옴표, 작은 따옴표, 백틱으로 표현)

> 백틱은 사용시
>
> ``` js
> const name = "Mike"
> const greeting = `안녕하세요. ${name}입니다`
> // 이처럼 파이썬의 f string 처럼 사용 가능
> ```

2. 숫자형

> + `+`, `-`, `/` , `*`, `%` 등 사칙연산 가능
>
> ``` js
> const x  = 1/0 // => Infinity
> 
> const name = 'Mike'
> const y = name/2 // => NaN (Not a Number: 숫자가 아님을 뜻하는 오류)
> ```



**숫자형과 문자형은 `+`연산시 숫자가 문자형으로 바뀌는 암시적 형변환이 일어남. 결과적으로 문자형 객체 반환.** 

3. Boolean

> - 비교연산으로 통해 나오는 `true`, `false` 값

4. null, undefined

> ``` js
> let age; // => undefined 변수는 선언됐지만 할당되지 않음을 뜻
> let name = null // => null
> ```
>
> 객체형, 심볼형

5. typeof

> 객체의 타입을 알아낼 수 있는 연산자
>
> ``` js
> console.log(typeof 3) // => "number"
> ```
>
> 본인이 작성한 코드라면 typeof 연산자를 사용할 일이 거의 없지만
>
> 다른개발자의 코드를 받을할 경우가 생기기에 알아두자
>
> ``` js
> console.log(typeof null) // => object 라고 뜸
> ```
>
> 결과적으로 `null`은 `object` 객체가 아님
>
> 자바스크립트 초기버전의 오류. 하위호완을 위해 수정되지 않음



## alert, prompt, confirm

**사용자와 상호작용 하는 대화상자**

1. alert

   > 일방적으로 알리는 용도

2. prompt

> prompt("띄워지는 문구"(, default))
>
> 사용자에게 어떤 값을 입력 받을 때 사용
>
> ``` js
> const name = prompt("이름을 입력하세요.")
> // => Mike
> alert(`환영합니다, ${name}님`)
> // => "환영합니다, Mike님"
> ```
>
> default값 입력받을 수 있음
>
> ``` js
> const nowTime = prompt("예약일을 입력해 주세요,", "2021-12")
> ```

3. comfirm

> 확인과 취소 버튼이 함께 있음
>
> 확인시 true, 취소시 false
>
> ``` js
> const isAdult = confirm("당신은 성인 입니까?")
> ```

**3개 공통점**

- 창이 떠 있을 시 스크립트가 일시 정지됨
- 스타일링 불가능(브라우저마다 모양도 다름)



## 형변환

**형변환이 필요한 이유**

> 자료형이 다른 상태에서 연산시 의도치 않은 오류 발생
>
> ``` js
> const mathScore = prompt("수학 몇점?") // 90
> const engScore = prompt("영어 몇점?") // 80
> const result = (mathScore + engScore) /2
> 
> console.log(result) // 4540
> ```
>
> => `prompt`로 입력받은 값은 문자열 따라서 90 + 80 = 9080이 된 것
>
> 9080은 문자인데 나눗셈 연산이 됨 => 자동 형변환(암시적 형변환)
>
> 이런 상황을 대비해서 형변환을 직접 해주는 것: 명시적 형변환



`String()`: 문자형으로 변환

`Number()`: 숫자형으로 변환

> ``` js
> console.log(
> 	Number(true) // 1
>     Number(false) // 0
>     Number('1234') // 1234
> 	Number('1234hgsdfdsa') // NaN
> 	Number(null) // 0
> 	Number(undefined) // NaN
> )
> ```

`Boolean()`: true, false 값으로 변환

> - `숫자 0`, `빈 문자열(공백도 true)''`, `null`, `undefined`, `NaN` 인 경우를 제외하고 모두 `true` 를 반환함



## 연산자

`+`, `-`, `/`, `*`, `%: 나머지`, `**: 거듭제곱`

``` js
let num = 10;
num += 5 // num: 15
// +, -, /, %, ** 모두 가능

++, -- 를 하면 1 씩 +,-됨
let result = num++; // 15 증가되기 전의 값을 할당
result = ++num; // 16 증가된 후 값을 할당
```





## 비교연산자, 조건문

`<`, `>`, `<=`, `>=`, `==`, `!=` `===`

비교 연산자의 결괏값은 항상 `Boolean` 값

`=`: 할당을 의미

`==`: 같은지 판단, 동등연산자

`===`: 타입까지 비교. 일치 연산자

``` js
const a = 1
const b = '1'

console.log(a == b) // true
console.log(a === b) // false
```



### if

``` js
const age = 30

if(age >19){
    console.log('환영합니다')
}else if(age === 19){
    console.log('수능 화이팅')
}else{
    console.log('안녕히가세요')
}

// '환영합니다' 출력
```



## 논리연산자

`|| OR`: 둘 중 하나가 `true` 면 `true` 반환. 따라서 앞 조건이 이미 `true` 면 뒤는 실행하지 않고 `true`로 종료

 `&& AND`: 둘 중 하나가 `false`면 `false`반환. 따라서 앞 조건이 이미 `false` 면 뒤는 실행하지 않고 `false`로 종료

 `!  NOT`

> ``` js
> const age = prompt('나이가..?')
> const isAdult = age > 19
> 
> if(!isAdult){
>     console.log('돌아가')
> }else{
>     console.log('어서오세요')
> }
> ```



``` js
// 우선순위
// 남자이고, 이름이 Mike 이거나 성인이면 통과

const gender = 'F'
const name = 'Jane'
const isAdult = true

if(gender === 'M' && name === 'Mike' || isAdult){
    console.log('pass')
}else{
    console.log('돌아가')
}
// => 'pass' 가 뜸
// &&가 ||보다 우선순위가 높아서 && 부분을 먼저 평가 후 ||을 평가해서 isAdult에서 true가 떳기에 pass가 뜨는것
// 따라서 의도한 대로 하려면 앞 && 조건을 괄호로 묶어야 함
```



## 반복문



`for`

> ``` js
> for(let i = 0; i < 10; i ++){
>     //반복할 코드
> }
> // for(초기값; 반복문이 돌아가는 조건; 반복문이 1번 실행후 실행될 작업)
> ```
>
> 조건이 `false`가 되면 반복문을 빠져나옴

`while`

> ``` js
> let i = 0
> while(i < 10){
>     //코드
>     console.log(i)
>     i ++ ;
> }
> ```

`do while`

> ``` js
> let i = 0
> do{
>     //코드
>     i ++ ;
> }while(i<10)
> ```
>
> 적어도 한 번은 실행 후 조건을 판단.



`break`: 만나는 즉시 멈추고 빠져나옴

`continue`: 만나면 멈추고 다음 반복으로 진행



## switch

`if` 문을 알고있으면 몰라도 되지만, 케이스가 다양한 경우 보다 간결하게 사용할 수 있음

``` js
// 1
switch(평가){
    case A:
        // A일 때 코드
    case B:
        // B일때 코드
    ...
}
    
// 아래 if문으로 변형시
if(평가 === A){
    // A일 때 코드
}else if(평가 === B){
    //B일 때 코드
}
```

**ex**

``` js
let fruit = prompt("무슨 과일을 사고 싶나요?")
switch(fruit){
    case '사과':
		console.log('100원 입니다.')
    case '바나나':
		console.log('200원 입니다.')
    case '키위':
		console.log('300원 입니다.')
    case '멜론':
    case '수박':
		console.log('400원 입니다.')
    default :
        console.log('그런 과일은 없습니다.')
}
```

fruit에 사과가 입력이 되면

> 100원 입니다.
>
> 200원 입니다.
>
> 300원 입니다.
>
> 400원 입니다.

이렇게 모두 출력이 된다.

첫번째에 case에 `true`되면 밑에는 모두 통과가 되기 때문. 따라서 case에 걸리면 break문을 걸어줘야함



## 함수

- 중복되는 코드를 줄여줌

- 한번에 한 작업에 집중

- 읽기 쉽고 어떤 동작인지 알 수 있게 네이밍!

``` js
function sayHello(name){
    console.log(`Hello ${naem}`)
}
```

function 함수명(매개변수){

​	표현식

}

``` js
function showError(){
    alert('Error! Plz Refresh');
}

showError();
=================
function sayHello(name){
    let msg = 'Hello'
    if(name){
        msg += name
        // msg = `Hello ${name}`
    }
    console.log(msg)
}

sayHello('Mike')
sayHello('Tom')
```

> msg 는 함수 내에서만 사용할 수 있는 지역변수 (함수 안에서 선언되었기 때문)

``` js
console.log('함수 호출 전')
let msg = 'Hello'
console.log(msg) // Hello

function sayHello(name){
    if(name){
        msg += `, ${name}`
        // msg = `Hello, ${name}`
    }
    console.log('함수 내부')
    console.log(msg) // Hello, Mike / Hello, Tom
}

sayHello('Mike')
sayHello('Tom')
console.log('함수 호출 후')
console.log(msg) // Hello, Tom
```

> 어디서나 접근할 수 있는 변수: 전역변수



``` js
let msg "welcome";
console.log(msg) // welcome
function sayHello(name){
    let msg = "Hello"
    console.log(msg + ' ' + name) // welcome Mike
}

sayHello('Mike')
console.log(msg) // welcome
```

> 함수 내에서 let으로 지역변수로 다시 선언했기에 전역변수에 영향을 받지 않는다

``` js
let name = "Mike"

function sayHello(name){
    console.log(name) // undefined / Jane
}

sayHello();
sayHello('Jane')
```



**OR 연산자, 기본값을 사용한 함수**

``` js
function sayHello(name){
    let newName = name || 'friend'
    let msg = `Hello ${newName}`
    console.log(msg) // Hello, friend / Hello, Jane
}

sayHello()
sayHello('Jane')

function sayHello(name = 'friend'){
    let newName = name
    let msg = `Hello ${newName}`
    console.log(msg) // Hello, friend / Hello, Jane
}

sayHello()
sayHello('Jane')
```



**return 으로 값 반환**

``` js
function add(num1, num2){
    return num1 + num2
}
const result = add(2,3)
console.log(result) // 5
```



``` js
function showError(){
    alert('Error!')
    return
    alert('이 코드는 절대 실행되지 않습니다.')  // return 다음 문장이라 실제로 실행 안됨
}
const result  = showError()
console.log(result) // Error!
```



### 함수표현식

1. 함수 선언문

``` js
sayHello()

function sayHello(){
    console.log('Hello')
}

sayHello()
```

> - 어디서든 호출 가능
>
>   - JS는 인터프리터 언어 
>
>     인터프리터 언어: 위에서 아래로 순차적으로 읽어서 실행하는 언어  
>
> > #### 그럼 어떻게 호출이 먼저 될 수 있는가
> >
> > JS 는 모든 선언된 함수를 찾아서 먼저 실행함.
> >
> > 따라서 눈으로 봤을 때는 선언이 뒤에 되어 있어도 실제 사용 가능한 범위는 전체영역으로 넓어짐(코드위치가 실제로 올라가는 것이 아님)
> >
> > 이를 **호이스팅(Hoisting)** 이라고 부름

2. 함수 표현식

``` js
let sayHello = function(){
    cnosole.log('Hello')
}
```

> 함수 표현식은 한 줄 씩 읽으면서 실행함
>
> 따라서 먼저 선언하면 읽을 수 없음(호이스팅 불가)



### 화살표 함수 (ES6이후 활발하게 사용되고 있음)

``` js
let add = (num1, num2)=>{
    return num1 + num2
}

let add = (num1, num2)=>(
    num1 + num2
) // return을 소괄호로 대체할 수 있음, return 전에 코드가 여러줄이면 소괄호 사용 불가!

let add = (num1, num2) => num1 + num2
// return문이 한 줄이면 괄호도 생략 가능

let sayHello = name => `Hello ${name}`
// 매개변수가 하나면 매개변수 괄호도 생략 가능, 인수가 없는 함수는 괄호 생략 불가! 
```



## 객체 Object

``` js
const supermane = {
    name: 'clark',
    age: 33,
}
```

- 중괄호

- key, value가 페어로 들어감

- 객체 접근시 `.` 사용

  `superman.name` ('clark'), `superman.age` (33)

- 추가 삭제 가능

  ``` js
  superman.gender = 'male'
  supermane['hairColor'] = 'black'
  
  delete superman.hairColor
  ```

### 단축 프로퍼티

``` js
const name = 'clark'
const age = 33

const superman = {
    name: name,
    age: age,
    gender: 'male'
}

// 아래로 변환 가능
const superman = {
    name,
    age,
    gender: 'male'
}
```

### 프로퍼티 존재 여부 확인

``` js
superman.birthDay // undefined
'birthDay' in superman // false
'age' in superman // true 
```

### for...in 반복문

``` js
for(let key in superman){
    console.log(key)
    console.log(superman[key])
}
```



**객체 in 예제**

``` js
function makeObject(name, age){
    return {
        name,
        age,
        hobby: 'football',
    }
}

const Mike = makeObject("Mike", 30)
console.log(Mike)
// Object = {name: 'Mike', age: 30, hobby: 'football'}

console.log('age' in Mike) // true
console.log('birthDay' in Mike) // false

function isAdult(user){
    if(user.age < 20){
        return false
    }
    return true
}

const Jane = {
    name:'Jane'
}

console.log(isAdult(Mike)) // true
console.log(Jane) // true
```

> `Jane` 이 `true`가 뜨는 이유
>
> > `age`란이 없어서 `undefined`가 발생하여 `if`문이 `false`처리됨. 따라서 순차적으로 `return true`가 되는 현상 발생

**수정**

``` js
function isAdult(user){
    if(!('age' in user) || user.age < 20){ // user에 age가 없거나, 20살 이하라면 false
        return false
    }
    return true
}
const Jane = {
    name:'Jane'
}

console.log(Jane) // false
```



**for...in 예제**

``` js
const Mike = {name: 'Mike', age: 30, hobby: 'football'}

for(x in Mike){
    console.log(Mike[x]) // Mike['name'] / Mike['age']
}
```



## 객체 method, this

``` js
const superman ={
    name: 'clark',
    age: 33,
    fly(){
        cnosole.log('날아갑니다')
    }
}
superman.fly // 날아갑니다
// fly: superman의 method
```

``` js
let user = {
    name: 'Mike',
    sayHello: function(){
        console.log(`Hello ${this.name}`)
    }
}
// 여기서 user를 사용하지 않고 웬만하면 this를 사용함 예제로 설명
// this 는 지금 scope의 객체를 가르킴

user.sayHello() // Hello Mike
```

> 객체 내에서 `method`를 사용할 때 `화살표함수`를 사용하고 `this`를 사용하면 안됨
>
> `화살표함수`는 일반 함수와 달리 자신만의 `this`를 가지지 않음 따라서 화살표함수 내에서 `this`를 사용하면 외부의 값을 가져옴

``` js
let boy = {
    name: 'Mike',
    sayHello: ()=> {
        console.log(this); // 전역객체를 가르킴 (브라우저 환경: window / Node.js환경: global)
    }
}
// this != boy
```



**ex1**

``` js
let boy = {
    name: 'Mike',
    sayHello:(){
    console.log(boy.name)
	}
}

let man = boy
boy = null
console.log(man.name) // TypeError: cannot read property 'name' of null

// boy 를 다른 변수에 할당하고 null으로 만든다음 다른변수에서 method를 사용하면 boy가 없어졌기 때문에 실행이 안된다
// 이를 방지하기 위해 this를 사용하는것이 편하다
```



**ex2**

``` js
let boy = {
    name: 'Mike',
    sayHello:() => {
    console.log(this)
	}
}

boy.sayHello() // console창에 window가 나타남
```



## 배열 Array

**순서가 있는 리스트**

- 대괄호로 묶어주고 쉼표로 나누어줌
- Index는 0부터 시작
- 배열은 문자 뿐만 아니라 숫자, 객체, 함수 등도 포함할 수 있음

`length`: 배열의 길이를 나타냄

`push`: 배열 끝에 추가(여러요소 한번에 추가 가능)

`pop`: 배열 끝 요소 제거

`unshift`: 배열 앞에 추가(여러요소 한번에 추가 가능)

`shift`: 배열 앞에 제거



``` js
let days = ['mon', 'tue', 'wed']

days.push('thu')
days.unshift('sun')

for(let index=0; index < days.length; index ++;){
    console.log(days[index])
}
// 'sun' / 'mon' / 'tue' / 'wed' / 'thu'

for(let day of days){
    console.log(day)
}
// 'sun' / 'mon' / 'tue' / 'wed' / 'thu'
```



























