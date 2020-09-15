import cookies from "vue-cookies";
import axios from "axios";

import SERVER from "@/api/api";
import router from "@/router";

export default {
  namespaced: true,
  state: {
    authToken: cookies.get("auth-token"),
  },
  getters: {
    isLoggedIn(state) {
      return !!state.authToken;
    },
    config: (state) => `Bearer ${state.authToken}`,
  },
  mutations: {
    SET_TOKEN(state, token) {
      state.authToken = token;
      cookies.set("auth-token", token, 60 * 60);
    },
  },
  actions: {
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
        route: SERVER.ROUTES.accounts.URL + SERVER.ROUTES.accounts.signup,
        name: "signup",
      };
      dispatch("postAuthData", info);
    },

    login({ dispatch }, loginData) {
      const info = {
        data: loginData,
        location: SERVER.ROUTES.accounts.URL + SERVER.ROUTES.accounts.login,
      };
      dispatch("postAuthData", info);
    },

    logout({ commit }) {
      commit("SET_TOKEN", null);
      cookies.remove("auth-token");
      router.push({ name: "Home" });
    },
  },
};
