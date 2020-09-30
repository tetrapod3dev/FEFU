import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import router from "./router";
import store from "./store";
import LazyLoading from "@/components/core/LazyLoading";

Vue.config.productionTip = false;
Vue.component("lazy-loading", LazyLoading);

new Vue({
  vuetify,
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
