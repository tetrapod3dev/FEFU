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
            router.push({ name: "LoginView" });
          } else {
            console.log(res);
            commit("SET_TOKEN", res.headers.authorization.substr(7));
            router.push({ name: "Home" });
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    signup({ dispatch }, signupData) {
      const info = {
        data: signupData,
        location: SERVER.ROUTES.accounts.URL,
        name: "signup",
      };
      dispatch("postAuthData", info);
    },

    login({ dispatch }, loginData) {
      const info = {
        data: loginData,
        location: SERVER.ROUTES.accounts.login,
      };
      dispatch("postAuthData", info);
    },

    logout({ commit }) {
      commit("SET_TOKEN", null);
      cookies.remove("auth-token");
      router.push({ name: "Home" }).catch((error) => {
        if (error.name === "NavigationDuplicated") {
          location.reload();
        }
      });
    },
  },
};
