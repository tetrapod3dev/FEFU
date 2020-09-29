import axios from "axios";

import SERVER from "@/api/api";

export default {
  namespaced: true,
  state: {
    maincategories: [],
    mediumcategories: {},
    filter: {
      maincategory: null,
      mediumcategory: null,
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
