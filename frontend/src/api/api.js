export default {
  // URL: "http://localhost:8080",
  // URL: "http://j3a402.p.ssafy.io",
  URL: "http://j3a402.p.ssafy.io:8801",
  IMAGE_URL: "http://j3a402.p.ssafy.io:8888/upload/",
  ROUTES: {
    accounts: {
      URL: "/users", // CRUD / 유저 CRUD
      login: "/auth/login",
      checkEmail: "/users/check-email/", // GET / 이메일 중복 체크
      checkNickname: "/users/check-nickname/", // GET / 닉네임 중복 체크
      password: "/users/password",
    },
    products: {
      URL: "/products",
      viewed: "/viewed/",
      maincategory: "/products/get_main_category/", // GET / 대분류 카테고리 목록 불러오기
      mediumcategory: "/products/get_medium_category/", // GET / 중분류 카테고리 목록 불러오기
      subcategory: "/products/get_sub_category/", // GET / 소분류 카테고리 목록 불러오기
      top_three_viewed_today: "/products/top_three_viewed_today/",
      get_my_products: "/products/get_my_products/", // GET / 내가 등록한 상품 목록 불러오기
      related_products: "/products/related_products/", // GET 연관된 상품 불러오기
      recommendation: "/products/recommendation/", //GET 추천상품 불러오기
      get_latest_products: "/products/get_latest_products/", //GET 가장 최신 물품 3개 불러오기
      sold: "/products/sold/", //PATCH 상품의 판매 status를 변경 + 판매 로그 생성/삭제
    },
    campaigns: {
      URL: "/campaigns",
      join: "/campaigns/join", // POST / 캠페인 참여 신청, GET / 내가 참여한 캠페인 목록 불러오기
      search: "/campaigns/search",
      proof: "/campaigns/proof",
      yet: "/campaigns/proof/yet",
      myCampaign: "/campaigns/my-campaign", // GET / 내가 등록한 캠페인 목록 불러오기
      personalPercentTeam: "/campaigns/proof/personal-percent/team",
      officialPercentWeek: "/campaigns/proof/official-percent/week",
    },
    images: {
      upload: "/images/upload",
      download: "/images/download",
    },
  },
};
