import axios from "axios";

import SERVER from "@/api/api";

export default {
  namespaced: true,
  state: {
    maincategories: [
      { no: 1, main_category_name: "패션의류" },
      { no: 2, main_category_name: "패션잡화" },
      { no: 3, main_category_name: "화장품/미용" },
      { no: 4, main_category_name: "디지털" },
      { no: 5, main_category_name: "가전" },
      { no: 6, main_category_name: "가구/인테리어" },
      { no: 7, main_category_name: "생활/건강" },
      { no: 8, main_category_name: "출산/육아" },
      { no: 9, main_category_name: "스포츠" },
      { no: 10, main_category_name: "레저" },
      { no: 11, main_category_name: "도서/음반/문구" },
    ],
    mediumcategories: {
      "1": [
        { no: 1, medium_category_name: "여성 의류", main_category_no: 1 },
        { no: 2, medium_category_name: "남성 의류", main_category_no: 1 },
        { no: 3, medium_category_name: "기타 의류", main_category_no: 1 },
      ],
      "2": [
        { no: 21, medium_category_name: "여성 신발", main_category_no: 2 },
        { no: 22, medium_category_name: "남성 신발", main_category_no: 2 },
        { no: 23, medium_category_name: "신발 용품", main_category_no: 2 },
        { no: 24, medium_category_name: "지갑", main_category_no: 2 },
        { no: 25, medium_category_name: "가방", main_category_no: 2 },
        { no: 26, medium_category_name: "헤어 액세서리", main_category_no: 2 },
        { no: 27, medium_category_name: "모자", main_category_no: 2 },
        { no: 28, medium_category_name: "패션 소품", main_category_no: 2 },
        { no: 29, medium_category_name: "액세서리", main_category_no: 2 },
        { no: 30, medium_category_name: "장갑", main_category_no: 2 },
        { no: 31, medium_category_name: "벨트", main_category_no: 2 },
        { no: 32, medium_category_name: "양말", main_category_no: 2 },
        {
          no: 33,
          medium_category_name: "선글라스/안경테",
          main_category_no: 2,
        },
        { no: 34, medium_category_name: "시계", main_category_no: 2 },
        { no: 35, medium_category_name: "기타 잡화", main_category_no: 2 },
      ],
      "3": [
        { no: 41, medium_category_name: "스킨케어", main_category_no: 3 },
        { no: 42, medium_category_name: "선케어", main_category_no: 3 },
        { no: 43, medium_category_name: "클렌징", main_category_no: 3 },
        {
          no: 44,
          medium_category_name: "베이스 메이크업",
          main_category_no: 3,
        },
        { no: 45, medium_category_name: "색조 메이크업", main_category_no: 3 },
        { no: 46, medium_category_name: "뷰티 소품", main_category_no: 3 },
        { no: 47, medium_category_name: "마스크/팩", main_category_no: 3 },
        { no: 48, medium_category_name: "네일 케어", main_category_no: 3 },
        { no: 49, medium_category_name: "바디 케어", main_category_no: 3 },
        { no: 50, medium_category_name: "헤어 케어", main_category_no: 3 },
        { no: 51, medium_category_name: "헤어 스타일링", main_category_no: 3 },
        { no: 52, medium_category_name: "향수", main_category_no: 3 },
        { no: 53, medium_category_name: "기타 뷰티", main_category_no: 3 },
      ],
      "4": [
        { no: 61, medium_category_name: "휴대폰", main_category_no: 4 },
        {
          no: 62,
          medium_category_name: "웨어러블 디바이스",
          main_category_no: 4,
        },
        { no: 63, medium_category_name: "PC", main_category_no: 4 },
        { no: 64, medium_category_name: "태블릿 PC", main_category_no: 4 },
        { no: 65, medium_category_name: "노트북", main_category_no: 4 },
        { no: 66, medium_category_name: "PC 주변기기", main_category_no: 4 },
        { no: 67, medium_category_name: "저장장치", main_category_no: 4 },
        { no: 68, medium_category_name: "게임", main_category_no: 4 },
        {
          no: 69,
          medium_category_name: "카메라/캠코더 용품",
          main_category_no: 4,
        },
        { no: 70, medium_category_name: "광학기기/용품", main_category_no: 4 },
        { no: 71, medium_category_name: "자동차기기", main_category_no: 4 },
        { no: 72, medium_category_name: "기타", main_category_no: 4 },
      ],
      "5": [
        { no: 81, medium_category_name: "주방 가전", main_category_no: 5 },
        { no: 82, medium_category_name: "영상 가전", main_category_no: 5 },
        { no: 83, medium_category_name: "생활 가전", main_category_no: 5 },
        { no: 84, medium_category_name: "음향 가전", main_category_no: 5 },
        { no: 85, medium_category_name: "계절 가전", main_category_no: 5 },
        { no: 86, medium_category_name: "미용 가전", main_category_no: 5 },
      ],
      "6": [
        { no: 101, medium_category_name: "침실 가구", main_category_no: 6 },
        { no: 102, medium_category_name: "거실 가구", main_category_no: 6 },
        { no: 103, medium_category_name: "주방 가구", main_category_no: 6 },
        { no: 104, medium_category_name: "수납 가구", main_category_no: 6 },
        {
          no: 105,
          medium_category_name: "아동/주니어 가구",
          main_category_no: 6,
        },
        {
          no: 106,
          medium_category_name: "서재/사무용 가구",
          main_category_no: 6,
        },
        { no: 107, medium_category_name: "아웃도어 가구", main_category_no: 6 },
        { no: 108, medium_category_name: "DIY자재/용품", main_category_no: 6 },
        { no: 109, medium_category_name: "침구", main_category_no: 6 },
        { no: 110, medium_category_name: "카페트/러그", main_category_no: 6 },
        { no: 111, medium_category_name: "커튼/블라인드", main_category_no: 6 },
        { no: 112, medium_category_name: "인테리어 소품", main_category_no: 6 },
        { no: 113, medium_category_name: "기타 가구", main_category_no: 6 },
      ],
      "7": [
        { no: 121, medium_category_name: "공구", main_category_no: 7 },
        { no: 122, medium_category_name: "수집품", main_category_no: 7 },
        { no: 123, medium_category_name: "관상어 용품", main_category_no: 7 },
        { no: 124, medium_category_name: "반려동물 용품", main_category_no: 7 },
        { no: 125, medium_category_name: "자동차 용품", main_category_no: 7 },
        { no: 126, medium_category_name: "악기", main_category_no: 7 },
        { no: 127, medium_category_name: "종교", main_category_no: 7 },
        { no: 128, medium_category_name: "욕실 용품", main_category_no: 7 },
        { no: 129, medium_category_name: "세탁 용품", main_category_no: 7 },
        {
          no: 130,
          medium_category_name: "건강 관리 용품",
          main_category_no: 7,
        },
        { no: 131, medium_category_name: "주방 용품", main_category_no: 7 },
        { no: 132, medium_category_name: "생활 용품", main_category_no: 7 },
        { no: 133, medium_category_name: "안마 용품", main_category_no: 7 },
        {
          no: 134,
          medium_category_name: "수납/정리 용품",
          main_category_no: 7,
        },
        { no: 135, medium_category_name: "청소 용품", main_category_no: 7 },
        { no: 136, medium_category_name: "기타", main_category_no: 7 },
      ],
      "8": [
        { no: 141, medium_category_name: "유아 식품", main_category_no: 8 },
        {
          no: 142,
          medium_category_name: "유아 위생 용품",
          main_category_no: 8,
        },
        {
          no: 143,
          medium_category_name: "유아 청결 용품",
          main_category_no: 8,
        },
        {
          no: 144,
          medium_category_name: "유아 외출 용품",
          main_category_no: 8,
        },
        { no: 145, medium_category_name: "유아용 가구", main_category_no: 8 },
        { no: 146, medium_category_name: "유아동 의류", main_category_no: 8 },
        { no: 147, medium_category_name: "부모 용품", main_category_no: 8 },
        { no: 148, medium_category_name: "유아 잡화", main_category_no: 8 },
      ],
      "9": [
        { no: 161, medium_category_name: "수영", main_category_no: 9 },
        { no: 162, medium_category_name: "골프", main_category_no: 9 },
        { no: 163, medium_category_name: "헬스", main_category_no: 9 },
        { no: 164, medium_category_name: "축구", main_category_no: 9 },
        { no: 165, medium_category_name: "야구", main_category_no: 9 },
        { no: 166, medium_category_name: "농구", main_category_no: 9 },
        { no: 167, medium_category_name: "배구", main_category_no: 9 },
        { no: 168, medium_category_name: "탁구", main_category_no: 9 },
        { no: 169, medium_category_name: "라켓 스포츠", main_category_no: 9 },
        {
          no: 170,
          medium_category_name: "스포츠 액세서리",
          main_category_no: 9,
        },
        { no: 171, medium_category_name: "기타 스포츠", main_category_no: 9 },
      ],
      "10": [
        { no: 181, medium_category_name: "등산", main_category_no: 10 },
        { no: 182, medium_category_name: "스키/보드", main_category_no: 10 },
        { no: 183, medium_category_name: "자전거", main_category_no: 10 },
        { no: 184, medium_category_name: "낚시", main_category_no: 10 },
        { no: 185, medium_category_name: "캠핑", main_category_no: 10 },
        { no: 186, medium_category_name: "볼링", main_category_no: 10 },
        {
          no: 187,
          medium_category_name: "오토바이/스쿠터",
          main_category_no: 10,
        },
        {
          no: 188,
          medium_category_name: "스케이트/보드/롤러",
          main_category_no: 10,
        },
        {
          no: 189,
          medium_category_name: "요가/필라테스",
          main_category_no: 10,
        },
        { no: 190, medium_category_name: "기타 레저", main_category_no: 10 },
      ],
      "11": [
        { no: 201, medium_category_name: "도서", main_category_no: 11 },
        { no: 202, medium_category_name: "음반", main_category_no: 11 },
        { no: 203, medium_category_name: "문구", main_category_no: 11 },
        { no: 204, medium_category_name: "기타", main_category_no: 11 },
      ],
    },
    filter: {
      maincategory: { no: null, name: null },
      mediumcategory: { no: null, name: null },
      pageNum: 1,
      content: null,
    },
  },
  getters: {
    MAINCATEGORIES: (state) => state.maincategories,
    MEDIUMCATEGORIES: (state) => state.mediumcategories,
    FILTER: (state) => state.filter,
    FILTER_MAINCATEGORY: (state) => state.filter.maincategory,
    FILTER_MEDIUMCATEGORY: (state) => state.filter.mediumcategory,
    FILTER_PAGENUM: (state) => state.filter.pageNum,
    FILTER_CONTENT: (state) => state.filter.content,
  },
  mutations: {
    SET_MAINCATEGORIES(state, maincategories) {
      state.maincategories = maincategories;
    },
    SET_MEDIUMCATEGORIES(state, mediumcategories) {
      state.mediumcategories = mediumcategories;
    },
    SET_FILTER(state, filter) {
      state.filter = filter;
    },
    SET_FILTER_MAINCATEGORY(state, maincategory) {
      state.filter.maincategory = maincategory;
    },
    SET_FILTER_MEDIUMCATEGORY(state, mediumcategory) {
      state.filter.mediumcategory = mediumcategory;
    },
    SET_FILTER_PAGENUM(state, pageNum) {
      state.filter.pageNum = pageNum;
    },
    SET_FILTER_CONTENT(state, content) {
      state.filter.content = content;
    },
  },
  actions: {
    CLEAR_MARKET_FILTER({ commit }) {
      commit("SET_MAINCATEGORY", null);
      commit("SET_MEDIUMCATEGORY", null);
      commit("SET_PAGENUM", 1);
      commit("SET_CONTENT", null);
    },
    async GET_AXIOS_MAINCATEGORIES({ commit }) {
      await axios
        .get(SERVER.URL + SERVER.ROUTES.products.maincategory)
        .then((res) => {
          commit("SET_MAINCATEGORIES", res.data);
        })
        .catch((err) => console.log(err.response));
    },
    async GET_AXIOS_MEDIUMCATEGORIES({ commit, getters }) {
      let medium = {};
      let main = getters.MAINCATEGORIES;

      await main.forEach(async (element) => {
        await axios
          .get(SERVER.URL + SERVER.ROUTES.products.mediumcategory, {
            params: { mainCategoryNo: element.no },
          })
          .then((res) => {
            medium[element.no] = res.data;
          })
          .catch((err) => {
            console.log(err.response);
          });
      });
      commit("SET_MEDIUMCATEGORIES", medium);
    },
  },
};
