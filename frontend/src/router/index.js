import Vue from "vue";
import VueRouter from "vue-router";

// Home
import Home from "../views/Home.vue";
import ErrorPage from "../views/ErrorPage.vue";

// Account
import LoginView from "../views/accounts/LoginView.vue";
import SignupView from "../views/accounts/SignupView.vue";

// Campaigns
import CampaignMain from "../views/campaigns/CampaignMain.vue";
import CampaignMake from "../views/campaigns/CampaignMake.vue";
import CampaignDetail from "../views/campaigns/CampaignDetail.vue";
import CampaignCertifi from "../views/campaigns/CampaignCertifi.vue";
import CampaignPostings from "../views/campaigns/CampaignPostings.vue";

// market
import MarketLayout from "../views/market/MarketLayout.vue";
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
    name: "CampaignMain",
    component: CampaignMain,
  },
  {
    path: "/campaigns/make/:type",
    name: "CampaignMake",
    component: CampaignMake,
  },
  {
    path: "/campaigns/:campaignNo",
    name: "CampaignDetail",
    component: CampaignDetail,
  },
  {
    path: "/campaigns/:campaignNo/certificate",
    name: "CampaignCertifi",
    component: CampaignCertifi,
  },
  {
    path: "/campaigns/:campaignNo/postings",
    name: "CampaignPostings",
    component: CampaignPostings,
  },
  // Campaign End

  // Market Start
  {
    path: "/market",
    name: "MarketLayout",
    component: MarketLayout,
    children: [
      {
        path: "",
        name: "MarketMainView",
        component: MarketMainView,
      },
      {
        path: "list/:pageNum/:mainCategory?/:mediumCategory?/:content?",
        name: "MarketListView",
        component: MarketListView,
      },
      {
        path: "detail/:productNo",
        name: "MarketDetailView",
        component: MarketDetailView,
      },
    ],
  },
  {
    path: "/market/make",
    name: "MarketMakeView",
    component: MarketMakeView,
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
  {
    path: "*",
    name: "ErrorPage",
    component: ErrorPage,
  },
];

const router = new VueRouter({
  scrollBehavior() {
    return { x: 0, y: 0 };
  },
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
