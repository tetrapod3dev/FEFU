<div align=center><img src="images/FEFU.png"></div>

<h2 align=center>A402 - Among Earth</h2>

<div align=center>
    <img src="https://img.shields.io/badge/platform-web-green">
    <img src="https://img.shields.io/static/v1.svg?label=&message=Vue&style=flat-square&logo=Vue.js&logoColor=white&color=42b883">
    <img src="https://img.shields.io/badge/framework-spring boot-blue">
    <img src="https://img.shields.io/badge/framework-django-green">
    <img src="https://img.shields.io/badge/database-MariaDB-9cf">
    <img src="https://img.shields.io/badge/server-AWS-yellow">
    <img src="https://img.shields.io/badge/language-python%2C java%2C javascript-yellowgreen">
    <img src="https://img.shields.io/badge/swagger-valid-brightgreen">
</div>
<img src="images/main_page.JPG" align=center>

<h3 align=center><a href="http://j3a402.p.ssafy.io/">FEFU 바로가기</a></h3>

<h3 align=center><a href="document/DEMO.md">DEMO 바로가기</a></h3>

<div align=center>
    캠페인 기능을 활용하여 다른 사용자들과 함께 환경을 지키기위한 노력을 계속할 수 있습니다.<br>
    캠페인 활동을 통해 얻은 에코포인트를 활용하여 중고물품을 저렴하게 구입하며,<br>
    함께, 그리고 지속 가능한 환경 보호 활동을 할 수 있을 것입니다.
</div>



## :book: 목차

### :earth_asia: [프로젝트 소개](#프로젝트-소개)

### :gear: [환경 보호 준비 과정](#환경-보호-준비-과정)

- ERD
- 시스템 구성도
- 기타 (와이어프레임 / API 문서 / 추천 시스템 소개)

### :package: [환경 보호 수단](#환경-보호-수단)​

* Frontend / Backend의 사용 Package
* 코드 실행 방법

### 🍀 [크루원 소개](#크루원-소개)





## 프로젝트 소개

> **For Earth, For Us**
>
> 자연과 공존할 수 있는 삶터를 지키고 행복한 미래를 만들어 가는 녹색의 길에서
>
> 지구 그리고 당신과 함께 하겠습니다.

지구의 날은 1970년 부터 시작되었고, 올해로 50주년을 맞이했습니다.

저희 FEFU는 지구의 날 50주년을 맞이하여 환경 보호에 대한 중요성을 다시 한번 상기하고자 합니다.

FEFU를 통해 사람들은 함께, 그리고 지속적으로 환경 보호 활동에 참여할 수 있을 것이고,

모두를 위한 아름답고 건강한 미래를 실현할 수 있을 것입니다.  





## 환경 보호 준비 과정
### ERD

> 회원, 캠페인, 중고마켓의 기능이 유기적으로 연결되어있고,
>
> 그를 효율적으로 활용하기 위해 ERD를 작성했습니다.

![ERD](images/ERD.png)



### 시스템 구성도

> 저희는 Spring boot와 Django를 활용한 MSA를 구축했습니다.
>
> 사용자의 클라이언트에서 요청을 보낼 경우 Spring의 Gateway를 통해
>
> 적절한 백앤드 서버로 전달하고, 각각의 백앤드 서버에서 요청을 처리해서 응답을 보내줍니다.
>
> 회원 관리, 캠페인 기능은 Spring boot로 구성된 백앤드 서버에서 처리했고,
>
> 추천 기능이 들어간 중고마켓 기능은 Django로 구성된 백앤드 서버에서 처리했습니다.

![Tech_Flow](images/Tech_Flow.JPG)



### 기타

* [와이어프레임](https://xd.adobe.com/view/3881961c-b080-4c11-84fe-019b89b3ba21-6dd2/?fullscreen&hints=off)
    * Adobe XD를 사용하여 제작된 와이어프레임
* [API Documentation](document/REST_API_document.md)
    * RESTful 서버의 API 문서입니다.
* [추천 시스템 구성 방법](document/recommendation_summary.md)
    * 어떠한 방식으로 추천 시스템이 구성되어 있는지와 그러한 판단의 근거를 기록해놨습니다.





## 환경 보호 수단

### Frontend 구성 요소

|        Package         |    Version    | Comment                                         |
| :--------------------: | :-----------: | :---------------------------------------------- |
|       vue-router       |     3.2.0     | 요청 URL에 따라 브라우저에서 돔을 변경          |
|          vuex          |     3.5.1     | 상태 관리 패턴 + 라이브러리                     |
|      vue-cookies       |     1.7.4     | 로그인 상태를 유지하기 위해 사용 (token 저장)   |
|         axios          |    0.20.0     | REST API 서버로부터 데이터를 받아오기 위해 사용 |
|        vuetify         |     2.3.8     | UI 구성을 위해 사용                             |
| chart.js / vue-chartjs | 2.9.3 / 3.5.1 | 데이터를 시각화하여 보여주기 위해 사용          |
|        firebase        |    7.22.0     | 중고마켓의 채팅 시스템 구현을 위해 사용         |

### Backend 구성 요소

|   기술 스택    |   Version   | Comment                                    |
| :------------: | :---------: | :----------------------------------------- |
|    OpenJDK     |     1.8     | Java vendor 사용                           |
|   SpringBoot   |    2.3.3    | Rest API 웹 애플리케이션 개발              |
|     Maven      |    3.6.3    | 프로젝트를 빌드하고 라이브러리를 관리 도구 |
|     MySQL      |   10.5.4    | DB vendor 사용                             |
|    MyBatis     |    2.1.2    | 서버와 DB의 연동을 위해 사용               |
|     Ubuntu     | 18.04.1 LTS | 서비스 제공을 위해 리눅스 서버 구축        |
|     Docker     | 17.04.0-ce  | 컨테이너화 된 애플리케이션 관리            |
| Docker-Compose |   1.27.0    | 컨테이너 환경 및 실행 관리                 |
|    Jenkins     |   2.249.1   | 자동화 배포 및 빌드                        |
|     Nginx      |   1.15.8    | Vue 클라이언트 웹 서버 사용                |

|      Spring 라이브러리       |  Version   | Comment                              |
| :--------------------------: | :--------: | :----------------------------------- |
|  Spring Cloud Dependencies   | Hoxton.SR7 | Cloud 라이브러리 호환 버전 통합 관리 |
| Spring Netflix Eureka Client |     -      | 서비스 되는 애플리케이션 구축        |
| Spring Netflix Eureka Server |     -      | 서비스 되는 애플리케이션 통합 관리   |
|     Spring Netflix Zuul      |     -      | API Gateway 라우팅을 위한 서버 구축  |
|       Spring Security        |     -      | 손쉬운 보안 관리를 위해 사용         |
|           Swagger2           |   2.9.2    | Rest API 스펙 문서화                 |
|             Gson             |     -      | Json - Object 능동 변환을 위해 사용  |
|           Java JWT           |   3.8.3    | 로그인 유저 인증을 위해 토큰 사용    |

|  Django 라이브러리  | Version | Comment                                              |
| :-----------------: | :-----: | :--------------------------------------------------- |
|       Django        | 2.1.15  | 중고마켓 관련 백앤드 구성을 위해 사용                |
| djangorestframework | 3.10.3  | RESTful API 서버를 쉽게 구축하기 위한 라이브러리     |
|      drf-yasg       | 1.17.1  | Django REST framework API를 문서화하기 위해 사용     |
|       PyMySQL       | 0.10.1  | 데이터베이스 커넥터 / MySQL 서버와 통신을 위해 사용  |
|       pandas        | 0.25.3  | 추천 시스템 구현을 위한 데이터분석 라이브러리        |
|        numpy        | 1.17.3  | 추천 시스템 구현을 위한 데이터분석 라이브러리        |
|        scipy        |  1.3.1  | 계산의 효율성을 높이기 위해 사용한 라이브러리        |
|    scikit-learn     | 0.21.3  | 추천 시스템 고도화를 위해 사용한 머신러닝 라이브러리 |



### [코드 실행 방법](document/how_to.md)





## 크루원 소개

### 🍀 Among Earth 팀

* **권경은** - *PM, backend*- [chriskwon96](https://lab.ssafy.com/chriskwon96)
* **김현수** - *backend* - [gustn16113](https://lab.ssafy.com/gustn16113)
* **박지윤** - *frontend* - [bellnuite](https://lab.ssafy.com/bellnuite)
* **박태록** - *frontend* - [sdf7575](https://lab.ssafy.com/sdf7575)
* **이동혁** - *data analysis* - [lee33843](https://lab.ssafy.com/lee33843)



### :star: Git Branch 전략

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
* Hotfix : 급한 버그 수정이 필요한 경우 버그 수정 branch

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



### :calendar: 개발 일정

![calendar](images/calendar.JPG)