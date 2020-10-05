import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import router from "./router";
import store from "./store";
import LazyLoading from "@/components/core/LazyLoading";
import * as firebase from "firebase/app";
import "firebase/auth";
import "firebase/database";

Vue.config.productionTip = false;
Vue.component("lazy-loading", LazyLoading);

new Vue({
  vuetify,
  router,
  store,
  render: (h) => h(App),
  created() {
    firebase.initializeApp({
      apiKey: "AIzaSyC97gWkQjdEZ7dLxn6MAxRmm47lL751p-I",
      authDomain: "fefuchat.firebaseapp.com",
      databaseURL: "https://fefuchat.firebaseio.com",
      projectId: "fefuchat",
      storageBucket: "fefuchat.appspot.com",
    });
  },
}).$mount("#app");
