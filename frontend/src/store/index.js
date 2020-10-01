import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

import moduleAccounts from "./accounts";
import moduleMarket from "./market";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    accounts: moduleAccounts,
    market: moduleMarket,
  },
  plugins: [
    createPersistedState({
      paths: ["market"],
    }),
  ],
});
