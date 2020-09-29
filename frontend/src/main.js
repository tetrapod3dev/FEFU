import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import router from "./router";
import store from "./store";

Vue.config.productionTip = false;

new Vue({
  vuetify,
  router,
  store,
  render: (h) => h(App),
  async created() {
    await this.$store.dispatch("market/GET_AXIOS_MAINCATEGORIES", null, {
      root: true,
    });
    await this.$store.dispatch(
      "market/GET_AXIOS_MEDIUMCATEGORIES",
      { mainCategoryNo: 1 },
      {
        root: true,
      }
    );
  },
}).$mount("#app");
