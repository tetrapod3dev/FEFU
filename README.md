# A402 - Among Earth / F E F U

<center>
    <img src="https://img.shields.io/badge/platform-web-green">
    <img src="https://img.shields.io/static/v1.svg?label=&message=Vue&style=flat-square&logo=Vue.js&logoColor=white&color=42b883">
    <img src="https://img.shields.io/badge/framework-spring boot-blue">
    <img src="https://img.shields.io/badge/framework-django-green">
    <img src="https://img.shields.io/badge/database-MariaDB-9cf">
    <img src="https://img.shields.io/badge/server-AWS-yellow">
    <img src="https://img.shields.io/badge/language-python%2C java%2C javascript-yellowgreen">
    <img src="https://img.shields.io/badge/swagger-valid-brightgreen">
</center>

## :book: 목차
- [FEFU](#fefu)
- [와이어프레임](#wire-frame)
- [기술 설명](#tech)
	- [ERD](#erd)
	- [디렉토리 구조도](#directory)
	- [시스템 구성도](#system)
	- [기타](#etc)
- [Among Earth Team](#Among-Earth-Team)


<div id='fefu' />
## 🌏 FEFU

> **For Earth, For Us**
>
> 자연과 공존할 수 있는 삶터를 지키고 행복한 미래를 만들어 가는 녹색의 길에서
> 지구 그리고 당신과 함께 하겠습니다.

지구의 날은 1970년 부터 시작하여 50주년을 맞은 이 시점에서
환경 보호에 대한 중요성을 다시 한번 상기하고
사람들로부터 참여할 수 있도록 도와주어 
아름답고 건강한 미래를 위해 실현하는데 매진합니다.  


<div id='wire-frame' />
## :desktop_computer: [와이어프레임](https://xd.adobe.com/view/3881961c-b080-4c11-84fe-019b89b3ba21-6dd2/?fullscreen&hints=off)
> Adobe XD를 활용하여 만든 와이어 프레임입니다.


<div id='tech' />
## :gear: 기술 설명
<div id='erd' />
### ERD

![ERD](images/new_ERD.JPG)
<div id='directory' />
### 디렉토리 구조도
> 폴더 구조가 어떻게 되는지 폴더, 파일별 역할들을 간략하게 적어주세요  
> 너무 자세히 적을 필요는 없습니다
<div id='system' />
### 시스템 구성도

![Tech_Flow](images/Tech_Flow.JPG)


<div id='etc' />
### 기타

#### [API Documentation](document/REST_API_document.md)

#### [추천 시스템 구성 방법](document/recommendation.md)




<div id='Among-Earth-Team' />
## 🍀 Among Earth Team

* **권경은** - *PM, backend*- [chriskwon96](https://lab.ssafy.com/chriskwon96)
* **김현수** - *backend* - [gustn16113](https://lab.ssafy.com/gustn16113)
* **박지윤** - *frontend* - [bellnuite](https://lab.ssafy.com/bellnuite)
* **박태록** - *frontend* - [sdf7575](https://lab.ssafy.com/sdf7575)
* **이동혁** - *data analysis* - [lee33843](https://lab.ssafy.com/lee33843)



### Git Branch 전략

### branch

```bash
(master) -> (develop) -> (develop-front / back / data) -> (feature/feature명)
```

* master : 배포 가능한 상태로 유지
* develop : 개발용 최상위 branch
* front / back / data
    * front : Frontend 개발 branch
    * back : Backend 개발 branch
    * data : 데이터 분석 개발 branch
* Fetaure : 기능별 branch

### commit

```bash
[이름] Feature / 행위 + 설명 으로 구성
    예시]
        [LDH] Login / FIX bugs from login modal
        [LDH] README / ADD README.md
```

### merge

```bash
merge 하기 전에 현재 작업 진행 상황 공유
merge 권한은 모두가 가지고 있지만 같은 팀의 다른 사람에게 리뷰 신청 후 merge 하기
merge 후 불필요한 branch 지우기
```

