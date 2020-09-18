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
    category: (state) => state.searchData,
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
    postAuthData({ commit }, info) {
      axios
        .post(SERVER.URL + info.location, info.data)
        .then((res) => {
          if (info.name == "signup") {
            alert("회원 가입에 성공했습니다");
          } else {
            commit("SET_TOKEN", res.data.token);
          }
          router.push({ name: "Home" });
        })
        .catch((err) => {
          if (err.response.data.msg == "이메일 인증 미완료") {
            alert("이메일 미인증 사용자입니다. 이메일 인증을 진행해주세요!");
          } else {
            alert("아이디 혹은 비밀번호를 다시 한 번 확인해주세요.");
          }
        });
    },
    signup({ dispatch }, signupData) {
      const info = {
        data: signupData,
        location: SERVER.ROUTES.accounts.URL + SERVER.ROUTES.accounts.signup,
        name: "signup",
      };
      dispatch("postAuthData", info);
    },

    login({ dispatch }, loginData) {
      const info = {
        data: loginData,
        location: SERVER.ROUTES.accounts.URL + SERVER.ROUTES.accounts.login,
      };
      console.log(info);
      dispatch("postAuthData", info);
    },

    logout({ commit }) {
      commit("SET_TOKEN", null);
      cookies.remove("auth-token");
      router.push({ name: "Home" });
    },
  },
};
