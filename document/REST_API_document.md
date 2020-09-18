# 0917 REST API 문서



## 회원 관리

1. Login

   ```json
   POST /auth/login
   ```

2. Find Password

3. Change Password

4. Logout : 프론트에서 토큰지우기

5. 회원가입

   ```json
   POST /users/signup
   ```

6. 이메일 중복 체크

   ```json
   POST /users/check-email/{email}
   ```

7. My Page

   1. 회원 정보 확인

      ```json
      GET /users/{username}
      ```

   2. 회원정보 수정

      ```json
      PATCH /users
      ```

      

   3. 포인트 전송

      ```json
      POST /users/trans-point
      ```

      * Body

      ```json
      {
          "buyer": "구매자_id",
          "product_no": "판매글_no"
      }
      ```

      

   4. 회원 탈퇴

      ```json
      DELETE /users/{username}
      ```

      



## 이미지

1. Image upload

   ```json
   POST /images/upload
   ```

2. Image download

   ```json
   GET /images/download/{fileName}
   ```





## 캠페인

#### 일일퀘스트 (로그인 필수)

1. 해당 유저 일일 퀘스트 목록 가져오기

   ```json
   GET /campaigns/daily-quest
   ```

   - 전체 유저의 퀘스트 별 완료 횟수 포함

2. 유저 퀘스트 여부 리스트

   ```json
   GET /campaigns/daily-quest/detail
   ```

3. 퀘스트 완료하기

   ```json
   POST /campaigns/daily-quest
   ```

   * Body
   
   ```json
   {
       "quest_no": "완료한 퀘스트_no"
   }
   ```
   
   

#### 기업 / 공식 / 개인 공통

1. 캠페인 목록 불러오기

   ```json
   GET /campaigns/{campaign_type}/{page_num}
   ```

   * {campaign_type} : 캠페인 종류
     * company / official / personal

2. 제목 / 태그로 검색

   ```json
   GET /campaigns/search?campaign-type=&type=&content=&page-num=1
   ```
   
   * campaign_type : 캠페인 종류
     * company / official / personal
   * type : 검색 방식
     * title / tag
   * content : 검색 내용
   * page_num : 페이지네이션

3. 캠페인 상세 페이지

   ```json
   GET /campaigns/{campaign_no}
   ```

4. 캠페인 글 작성

   ```json
   POST /campaigns
   ```

5. 캠페인 글 수정

   ```json
   PATCH /campaigns
   ```
6. 캠페인 글 삭제

   ```json
   DELETE /campaigns/{campaign_no}
   ```

  

#### 공식 / 개인 공통

##### 참여/탈퇴

1. 캠페인 참석 : POST /campaigns/join —- campaign_no

   ```json
   POST /campaigns/join
   ```

   

2. 캠페인 탈퇴 : DELETE /campaigns/leave/{campaign_no}

   ```json
   DELETE /campaigns/{campaign_no}/leave
   ```

   

3. 참여자 강퇴 : DELETE /campaigns/kick/{campaign_no}/{username}

   ```json
   DELETE /campaigns/{campaign_no}/kick/{username}
   ```

   

##### 인증 게시글

1. 인증 게시글 목록 : GET /campaigns/proof/{campaign_no}

   ```json
   GET /campaigns/{campain_no}/proof
   ```

   

2. 인증 게시글 작성

   ```json
   POST /campaigns/proof
   ```

   

3. 인증 게시글 삭제

   1. (관리자가 삭제할 경우) / 본인이 삭제할 경우

      ```json
      DELETE /campaigns/proof/{proof_no}
      ```

      

4. 인증 게시글 승인 처리

   ```json
   PATCH /campaigns/proof
   ```

   

5. 인증 현황
   1. 공식 캠페인
      > 캠페인 참석 유저들의 인증 현황 (오늘 목표인원대비 몇 %가 인증했는지)

      1. 모든 공식 캠페인 인증 현황

      ```json
      GET /campaigns/official-percent
      ```

      - 오늘, (D -1 ~ D - 8) 7일

      

      2. 특정 공식 캠페인 인증 현황

      ```json
      GET /campaigns/{campaign_no}/official-percent
      ```

      * 오늘, (D -1 ~ D - 8) 7일

      

   2. 개인 캠페인

      > 캠페인 참석 유저들의 인증 현황 (전체 유저들 중 지금까지 몇 % 참석했는지 며칠)

      1. 전체 팀원들이 각각 지금까지 몇 %인증했는지랑 평균 인증률 보여주기

      ```json
      GET /campaigns/{campaign_no}/personal-percent/team
      ```

      2. 내 인증률과 캘린더에서 지금까지 몇 % 인증했는지 보여주기

      ```json
      GET /campaigns/{campaign_no}/personal-percent/me	
      ```

      * 지금까지 작성한 인증 게시글 숫자랑 인증게시글 목록 중 날짜만



## 중고거래

1. 상품 목록 불러오기 : GET /products/{page_num}

   ```json
   GET /products/{page_num}
   ```

   

2. 상품 리스트 검색

   ```json
   GET /products/search?main-category=None&sub-category=None&content=None&page-num=1
   ```

   * main-category : 대분류 카테고리 필터링
   * sub-category : 중분류 카테고리 필터링
   * content : 검색 내용
     * 검색어 / 검색한 태그 등

   

3. 상품 등록 : POST /products (로그인 필수)

   - 카테고리 목록 불러오기

     ```json
     GET /products/categories
     ```

     * Response

     ```json
     {
         "대분류1": [소분류1, 소분류2],
         "대분류2": [소분류3, 소분류4],
         ...
     }
     ```

4. 상품 수정 

   ```json
   PATCH /products
   ```

5. 상품 삭제

   ```json
   DELETE /products/{product_no}
   ```

6. 상품 상세 보기

   ```json
   GET /products/{product_no}
   ```

7. 추천 상품 목록

   ```json
   GET /products/recommendation/{user_no}
   ```

8. 상품 판매 완료 상태 변경

   ```json
   PATCH /products/sold
   ```

   - Body

   ```json
   {
       "buyer": "구매자_id",
       "product_no": "판매글_no"
   }
   ```

   

------

