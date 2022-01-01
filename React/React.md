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

#### 폴더구조

``` markdown
> node_modules		# 프로젝트에 사용되는 dependency module들이 모여있음
> public			# index.html 파일이 있는 곳
> src				# App.js 가 있는 곳
	.gitignore
	package-lock.json
	package.json	# 설치된 모듈들 이름이 적혀있음
	README.md
```



리액트로 만든 페이지는 컴포넌트로 구성되어 있음. 비슷한 부분들을 재사용이 쉽고 유지보수가 쉬워짐



모든 컴포넌트는 대문자로 시작(ex. App.js)

함수로 만들어진 컴포넌트를 함수컴포넌트라고 함

JSX: js에서 html 태그를 작성 하는것(JS XML) 