import cookies from "vue-cookies";
import axios from "axios";

import SERVER from "@/api/api";
import router from "@/router";

export default {
  namespaced: true,
  state: {
    category: "",
    subCategory: "",
    pageNo: 1,
  },
  getters: {
    category: (state) => state.category,
    subCategory: (state) => state.subCategory,
    pageNo: (state) => state.pageNo,
  },
  mutations: {
    SET_CATEGORY(state, category) {
      state.category = category;
    },
    SET_SUBCATEGORY(state, subCategory) {
      state.subCategory = subCategory;
    },
    SET_PAGENO(state, pageNo) {
      state.pageNo = pageNo;
    },
  },
  actions: {
    clearMarketPageData({ commit }) {
      commit("SET_CATEGORY", "");
      commit("SET_SUbCATEGORY", "");
      commit("SET_PAGENO", 1);
    },
  },
};
