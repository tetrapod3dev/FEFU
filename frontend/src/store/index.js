import Vue from "vue";
import Vuex from "vuex";

import moduleAccounts from "./accounts";

Vue.use(Vuex);

const modules = {
  accounts: moduleAccounts,
};

export default new Vuex.Store({
  modules,
  state: {},
  mutations: {},
  actions: {},
});
