![logo](images/FEFU.png)

<center><h2>A402 - Among Earth</h2></center>

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
![main_page](images/main_page.JPG)

<center><a href="http://j3a402.p.ssafy.io/"><h2>FEFU 바로가기</h2></a></center>

<center><a href="document/DEMO.md"><h3>Demo 바로가기</h3></a></center>

<center>
    캠페인 기능을 활용하여 다른 사용자들과 함께 환경을 지키기위한 노력을 계속할 수 있습니다.<br>
    캠페인 활동을 통해 얻은 에코포인트를 활용하여 중고물품을 저렴하게 구입하며,<br>
    함께, 그리고 지속 가능한 환경 보호 활동을 할 수 있을 것입니다.
</center>



## :book: 목차

- [FEFU](#:earth_asia:-FEFU)
- [기술 설명](#:gear:-기술-설명)
	- [ERD](#ERD)
	- [시스템 구성도](#시스템-구성도)
	- [기타](#기타)
- [Among Earth Team](#🍀-Among-Earth-Team)



## :earth_asia: FEFU

> **For Earth, For Us**
>
> 자연과 공존할 수 있는 삶터를 지키고 행복한 미래를 만들어 가는 녹색의 길에서
>
> 지구 그리고 당신과 함께 하겠습니다.

지구의 날은 1970년 부터 시작되었고, 올해로 50주년을 맞이했습니다.

저희 FEFU는 지구의 날 50주년을 맞이하여 환경 보호에 대한 중요성을 다시 한번 상기하고자 합니다.

FEFU를 통해 사람들은 함께, 그리고 지속적으로 환경 보호 활동에 참여할 수 있을 것이고,

모두의 아름답고 건강한 미래를 실현할 수 있을 것입니다.  



## :gear: 기술 설명
### ERD

![ERD](images/ERD.png)




### 시스템 구성도

![Tech_Flow](images/Tech_Flow.JPG)



### 기타

#### [API Documentation](document/REST_API_document.md)

#### [추천 시스템 구성 방법](document/recommendation.md)





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

