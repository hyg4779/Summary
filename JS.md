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

]















