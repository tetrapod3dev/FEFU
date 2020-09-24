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
      state.authToken = token.substr(7);
      cookies.set("auth-token", state.authToken, 60 * 60);
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
            console.log(res);
            commit("SET_TOKEN", res.headers.authorization);
          }
          router.push({ name: "Home" });
        })
        .catch((err) => {
          // alert("아이디 혹은 비밀번호를 다시 한 번 확인해주세요.");
          console.log(err);
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
      dispatch("postAuthData", info);
    },

    logout({ commit }) {
      commit("SET_TOKEN", null);
      cookies.remove("auth-token");
      router.push({ name: "Home" });
    },
  },
};
