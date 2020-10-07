import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

import * as firebase from "firebase/app";
import "firebase/auth";
import "firebase/database";

import moduleAccounts from "./accounts";
import moduleMarket from "./market";
import AuthModule from "./AuthModule";
import ChatModule from "./ChatModule";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    accounts: moduleAccounts,
    market: moduleMarket,
    auth: AuthModule,
    chat: ChatModule,
  },
  state: {
    loading: false,
    error: null,
    onlineUsers: [],
  },
  plugins: [
    createPersistedState({
      paths: ["auth"],
    }),
  ],
  mutations: {
    setLoading(state, payload) {
      state.loading = payload;
    },
    setError(state, payload) {
      state.error = payload;
    },
    clearError(state) {
      state.error = null;
    },
    setOnlineUsers(state, payload) {
      state.onlineUsers = payload;
    },
  },
  actions: {
    loadOnlineUsers({ commit }) {
      firebase
        .database()
        .ref("presence")
        .on("value", function(snapshot) {
          let result = [];
          result[0] = snapshot.numChildren();
          result[1] = snapshot.val();
          commit("setOnlineUsers", result);
        });
    },
    clearError({ commit }) {
      commit("clearError");
    },
  },
  getters: {
    loading(state) {
      return state.loading;
    },
    error(state) {
      return state.error;
    },
    onlineUsers(state) {
      return state.onlineUsers;
    },
  },
});
