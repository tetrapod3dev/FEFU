export default {
  // URL: "http://localhost:8080",
  // URL: "http://j3a402.p.ssafy.io",
  URL: "http://j3a402.p.ssafy.io:8801",
  IMAGE_URL: "http://j3a402.p.ssafy.io:8888/upload/",
  ROUTES: {
    accounts: {
      URL: "",
      login: "/auth/login",
      signup: "/users",
    },
    products: {
      URL: "/products",
      maincategory: "/products/get_main_category/", // GET / 대분류 카테고리 목록 불러오기
      mediumcategory: "/products/get_medium_category/", // GET / 중분류 카테고리 목록 불러오기
      subcategory: "/products/get_sub_category/", // GET / 소분류 카테고리 목록 불러오기
      top_three_viewed_today: "/products/top_three_viewed_today/",
    },
    campaigns: {
      URL: "/campaigns",
      search: "/search",
    },
    images: {
      upload: "/images/upload",
      download: "/images/download",
    },
  },
};
