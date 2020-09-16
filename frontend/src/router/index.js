import Vue from "vue";
import VueRouter from "vue-router";

// Home
import Home from "../views/Home.vue";

// Account
import LoginView from "../views/accounts/LoginView.vue";
import SignupView from "../views/accounts/SignupView.vue";

// market
import MarketMainView from "../views/market/MarketMainView.vue";

// Campaigns
import CampaignList from "../views/campaigns/CampaignList.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  // Account Start
  {
    path: "/user/login",
    name: "LoginView",
    component: LoginView,
  },
  {
    path: "/user/signup",
    name: "SignupView",
    component: SignupView,
  },
  // Account End

  // Campaign Start
  {
    path: "/campaigns",
    name: "CampaignList",
    component: CampaignList,
  },
  // Campaign End

  // Market Start
  {
    path: "/market",
    name: "MarketMainView",
    component: MarketMainView,
  },
  // Market End

  {
    path: "/about",
    name: "About",
    component: () => import("../views/About.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
