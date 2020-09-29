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
