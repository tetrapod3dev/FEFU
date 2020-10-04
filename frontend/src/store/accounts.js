import cookies from "vue-cookies";
import axios from "axios";
import router from "@/router";

import SERVER from "@/api/api";

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
    USERNAME(state) {
      if (!state.authToken) {
        return "";
      }
      var base64Url = `Bearer ${state.authToken}`.split(".")[1];
      var decodedValue = JSON.parse(window.atob(base64Url));
      return decodedValue.sub;
    },
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
        .post(SERVER.URL + info.location, info.data, {
            headers: {
                'Access-Control-Allow-Origin': '*',
            }
        })
        .then((res) => {
          console.log(res)
          if (info.name != "signup") {
            commit("SET_TOKEN", res.headers.authorization.substr(7));
          }
        });
    },
    signup({ dispatch }, signupData) {
      const info = {
        data: signupData,
        location: SERVER.ROUTES.accounts.URL,
        name: "signup",
      };
      return dispatch("postAuthData", info);
    },

    login({ dispatch }, loginData) {
      const info = {
        data: loginData,
        location: SERVER.ROUTES.accounts.login,
      };
      return dispatch("postAuthData", info);
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
