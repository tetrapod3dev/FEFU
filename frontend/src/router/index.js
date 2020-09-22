import Vue from "vue";
import VueRouter from "vue-router";

// Home
import Home from "../views/Home.vue";

// Account
import LoginView from "../views/accounts/LoginView.vue";
import SignupView from "../views/accounts/SignupView.vue";

// Campaigns
import CampaignList from "../views/campaigns/CampaignList.vue";
import CampaignDetail from "../views/campaigns/CampaignDetail.vue";

// market
import MarketMainView from "../views/market/MarketMainView.vue";
import MarketListView from "../views/market/MarketListView.vue";
import MarketMakeView from "../views/market/MarketMakeView.vue";
import MarketDetailView from "../views/market/MarketDetailView.vue";
import MarketUpdateView from "../views/market/MarketUpdateView.vue";

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
  {
    path: "/campaigns/detail",
    name: "CampaignDetail",
    component: CampaignDetail,
  },
  // 데이터 생기면 연결할게용
  // {
  //   path: "/campaigns/:campaignNo",
  //   name: "CampaignDetail",
  //   component: CampaignDetail,
  // },
  // Campaign End

  // Market Start
  {
    path: "/market",
    name: "MarketMainView",
    component: MarketMainView,
  },
  {
    path: "/market/all/:pageNo",
    name: "MarketListView",
    component: MarketListView,
  },
  {
    path: "/market/make",
    name: "MarketMakeView",
    component: MarketMakeView,
  },
  {
    path: "/market/detail/:productNo",
    name: "MarketDetailView",
    component: MarketDetailView,
  },
  {
    path: "/market/update/:productNo",
    name: "MarketUpdateView",
    component: MarketUpdateView,
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
