# REST API 문서



## **회원 관리**

- 닉네임 체크 GET : /users/check-nickname
- 내 정보 수정 PATCH : /users
- 내 정보 가져오기  GET : /users/{username}
- 비밀번호 변경  PATCH : /users/password

1. Login

    ```
    POST /auth/login
    ```

2. Find Password

3. Change Password

4. Logout : 프론트에서 토큰지우기

5. 회원가입

    ```
    POST /users/
    ```

6. 이메일 중복 체크

    ```
    GET /users/check-email/{email}
    ```

7. My Page

    1. 회원 정보 확인

        ```
        GET /users/{username}
        ```

    2. 회원정보 수정

        ```
        PATCH /users
        ```

    3. 포인트 전송

        ```
        PATCH /users/eco-point
        {
        	"receiver" : "test1",
        	"point" : 20
        }
        // 로그인 필수
        // 보내는 유저의 포인트가 입력값 보다 적으면 실패함
        ```

        - Body

        ```
        {
            "buyer": "구매자_id",
            "product_no": "판매글_no"
        }
        ```

    4. 회원 탈퇴

        ```
        DELETE /users/{username}
        ```

## **이미지**

1. Image upload

    ```
    POST /images/upload
    ```

2. Image download

    ```
    GET /images/download/{fileName}
    ```

## **캠페인**

### **일일퀘스트 (로그인 필수)**

1. 해당 유저 일일 퀘스트 목록 가져오기

    ```
    GET /campaigns/daily-quest
    ```

    - 전체 유저의 퀘스트 별 완료 횟수 포함

2. 유저 퀘스트 여부 리스트

    ```
    GET /campaigns/daily-quest/detail
    ```

3. 퀘스트 완료하기

    ```
    POST /campaigns/daily-quest
    ```

    - Body

    ```
    {
        "quest_no": "완료한 퀘스트_no"
    }
    ```

### **기업 / 공식 / 개인 공통**

- 내가 참여한 캠페인 목록 GET : /campaigns/join
- 내가 등록한 캠페인 목록 GET : /campaigns/my-campaign

1. 캠페인 목록 불러오기

    ```
    GET /campaigns?campaign_type=personal&type=&content=&page_no=1
    ```

    - {campaign_type} : 캠페인 종류
        - company / official / personal

2. 제목 / 태그로 검색

    ```
    GET /campaigns?campaign_type=캠페인종류&type=검색방식&content=검색내용&page_no=1
    ```

    - campaign_type : 캠페인 종류
        - company / official / personal
    - type : 검색 방식
        - title / tag
    - content : 검색 내용
    - page_num : 페이지네이션

3. 캠페인 상세 페이지

    ```
    GET /campaigns/{campaign_no}
    ```

4. 캠페인 글 작성

    ```
    POST /campaigns
    ex)
    {
      "campaign" : {
          "content": "테스트 내용임다",
          "endDate": "2020-09-23",
          "startDate": "2020-09-20",
          "title": "테스트 캠페인",
          "type": "official",
          "writer": "test",
          "photo" : ""
       },
       "tag" : ["저탄소", "친환경 발자국"],
      }
    --------------------------------------------------------
      "official" : {  // 공식 or 100일 추가 정보
          "mission" : "사진 등록하기",
          "authProcess" : "사진 올리고 글 등록하기",
          "authStartTime" : "매일 00:00",
          "authEndTime" : "다음날 00:00",
          "headcount" : 100,
    			"requirement" : "아무나"
      }
    --------------------------------------------------------
      "company" : {  // 기업 추가 정보
    			"companyName" : "네이버",
    			"campaignLink" : "www.naver.com"
    	}
    }
    ```

5. 캠페인 글 수정

    ```
    PATCH /campaigns
    ```

6. 캠페인 글 삭제

    ```
    DELETE /campaigns/{campaign_no}
    ```

### **공식 / 개인 공통**

### **참여/탈퇴 (로그인 필수)**

1. 캠페인 참석 : POST /campaigns/join —- campaign_no

    ```
    POST /campaigns/join 
    {
    	"campaign_no" : 1
    }
    ```

2. 캠페인 탈퇴 : DELETE /campaigns/leave/{campaign_no}

    ```
    DELETE /campaigns/leave/{campaign_no}
    ```

3. 참여자 강퇴 : DELETE /campaigns/kick/{campaign_no}/{username}

    ```
    DELETE /campaigns/kick/{campaign_no}/{username}
    ```

4. 현재 유저 캠페인 참여 여부 확인 : GET /campaigns/join/{campaign_no}

### **인증 게시글**

1. 인증 게시글 목록(유저용) : GET /campaigns/proof/{campaign_no}/{page_no}

    인증 안된 게시글 목록(관리자용) : GET /campaigns/proof/yet/campaign_no}/{page_no}

    ```
    GET /campaigns/proof/{campain_no}/{page_no}
    ```

2. 인증 게시글 작성

    ```
    POST /campaigns/proof
    ```

3. 인증 게시글 삭제

    1. (관리자가 삭제할 경우) / 본인이 삭제할 경우

        ```
        DELETE /campaigns/proof/{proof_no}
        ```

4. 인증 게시글 승인 처리

    ```
    PATCH /campaigns/proof/{proof_no}
    ```

5. 인증 현황 (다시 한번 회의)

    1. 공식 캠페인

        > 캠페인 참석 유저들의 인증 현황 (오늘 목표인원대비 몇 %가 인증했는지)

        1. 공식 캠페인 오늘 인증 현황

        ```
        GET /campaigns/proof/official-percent/today/{campaign_no}
        ```

        - 오늘, (D -1 ~ D - 8) 7일

        1. 공식 캠페인 일주일 인증 현황

        ```
        GET /campaigns/proof/official-percent/week/{campaign_no}
        ```

        - 오늘, (D -1 ~ D - 8) 7일

    2. 개인 캠페인

        > 캠페인 참석 유저들의 인증 현황 (전체 유저들 중 지금까지 몇 % 참석했는지 며칠)

        1. 전체 팀원들이 각각 지금까지 몇 %인증했는지랑 평균 인증률 보여주기

        ```
        GET /campaigns/proof/personal-percent/team/{campaign_no}
        ```

        1. 내 인증률과 캘린더에서 지금까지 몇 % 인증했는지 보여주기

        ```
        GET /campaigns/proof/personal-percent/me/{campaign_no}
        ```

        - 지금까지 작성한 인증 게시글 숫자랑 인증게시글 목록 중 날짜만

## **중고거래**

🚨 api의 마지막 `/` 유무에 유의하세요!

### 상품 CRUD

1. 상품 목록 불러오기 : GET /products/{page_num}

    - 모든 상품 글 불러오기

    ```json
    GET /products
    ```

    - 이렇게 해도 모든 상품 글을 불러옵니다.

    ```json
    GET /products?mainCategory=&mediumCategory=&content=&pageNum=1
    ```

    - Response

    ```json
    [
        "page": {
            "curPage": 1,
            "perPageNum": 12,
            "totalCount": 38,
            "startPage": 1,
            "endPage": 4,
            "prev": false,
            "next": true,
            "startIndex": 1
    		},
    		"list": [
    		    {
    		        "no": 117,
                "title": "25kg 덤벨 팔아요~~~",
                "content": "여러분도 3대 500 할 수 있습니다\\n이것만 있으면!!! 얼마 안썻어요~~",
                "contact": "채팅 메세지 주세요~~",
                "price": 25000,
                "photo": "951382d4-b8d3-4168-b24c-e3c754660219.jpg",
                "eco_point": 10000,
                "status": 0,
                "reg_time": "2020-10-06T15:11:58Z",
                "writer": "kyungeunssafy@ssafy.com",
                "main_category_no": 9,
                "medium_category_no": 171,
                "sub_category_no": 962
    		    },
    		
    				...
    
    ]
    ```

2. 상품 리스트 검색

    ```
    GET /products?mainCategory=대분류&mediumCategory=중분류&content=검색어&pageNum=1
    ```

    - mainCategory : 대분류 카테고리 필터링
    - mediumCategory : 중분류 카테고리 필터링
    - content : 검색 내용
        - 검색어 / 검색한 태그 등

3. 상품 상세보기

    ```json
    GET /products/{product_no}/
    ```

4. 상품 등록 : POST /products (로그인 필수)

    ```json
    POST /products
    ```

    - Body (작성자 writer를 포함한 모든 필드 값을 body에 넣어서 보내주세요)

    ```json
    {
        "title": "createtest0925",
        "content": "hello",
        "writer": "test",
        "contact":"ssafy@gmail.com",
        "price": 50000,
        "photo": "phone.jpg",
        "eco_point":10000,
        "main_category_no": 1,
        "medium_category_no" : 1,
        "sub_category_no": 1
    }
    ```

5. 상품 수정

    ```json
    PATCH /products
    ```

    1. Body

    ```json
    { 
    	"writer": 글 작성자 이름,
    	"product_no": 판매글 번호,
    	...
    }
    ```

6. 상품 삭제

    ```json
    DELETE /products/{product_no}/
    ```

### 상품 관련

1. 가장 최신 상품 3개 리스트

    ```json
    GET /products/get_latest_products/
    ```

2. 오늘 가장 많이 조회된 상품 리스트

    ```json
    GET /products/top_three_viewed_today/
    ```

3. 조회중인 상품과 연관된 상품 리스트

    ```json
    GET /products/?product_pk={product_pk}
    ```

4. 상품 판매 상태 변경

    ```json
    PATCH /products/{product_no}/sold/
    ```

    1. Body

    ```json
    {
        "buyer": "구매자_username",
    }
    ```

5. 상품 조회 기록 생성

    ```
    POST /products/{product_no}/viewed/
    ```

6. 추천 상품 목록

    ```
    GET /products/recommendation/
    ```

7. 내 상품 불러오기

    ```json
    GET /products/get_my_products/
    ```

### 카테고리

1. 대분류 불러오기

    ```json
    GET /products/get_main_category/
    ```

2. 중분류 불러오기

    ```json
    GET /products/get_medium_category/?mainCateogryNo={대분류번호}
    ```

3. 소분류 불러오기

    ```json
    GET /products/get_sub_category/?mediumCategoryNo={중분류번호}
    ```

