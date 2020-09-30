import Vue from "vue";
import VueRouter from "vue-router";

// Home
import Home from "../views/Home.vue";
import ErrorPage from "../views/ErrorPage.vue";

// Account
import LoginView from "../views/accounts/LoginView.vue";
import SignupView from "../views/accounts/SignupView.vue";
import Mypage from "../views/accounts/Mypage.vue";
import MypageListCampaignAdmin from "../views/accounts/MypageListCampaignAdmin.vue";
import MypageListCampaignJoin from "../views/accounts/MypageListCampaignJoin.vue";
import MypageListProduct from "../views/accounts/MypageListProduct.vue";
import MypageInfo from "../views/accounts/MypageInfo.vue";
import MypageUpdatePwd from "../views/accounts/MypageUpdatePwd.vue";

// Campaigns
import CampaignMain from "../views/campaigns/CampaignMain.vue";
import CampaignMake from "../views/campaigns/CampaignMake.vue";
import CampaignDetail from "../views/campaigns/CampaignDetail.vue";
import CampaignDetailCertifi from "../views/campaigns/CampaignDetailCertifi.vue";
import CampaignDetailInfo from "../views/campaigns/CampaignDetailInfo.vue";
import CampaignDetailPostings from "../views/campaigns/CampaignDetailPostings.vue";

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
  {
    path: "/mypage",
    component: Mypage,
    children: [
      {
        path: "admin",
        name: "MypageListCampaignAdmin",
        component: MypageListCampaignAdmin,
      },
      {
        path: "join",
        name: "MypageListCampaignJoin",
        component: MypageListCampaignJoin,
      },
      {
        path: "product",
        name: "MypageListProduct",
        component: MypageListProduct,
      },
      {
        path: "",
        name: "MypageInfo",
        component: MypageInfo,
      },
      {
        path: "pwd",
        name: "MypageUpdatePwd",
        component: MypageUpdatePwd,
      },
    ],
  },
  // Account End

  // Campaign Start
  {
    path: "/campaigns",
    name: "CampaignMain",
    component: CampaignMain,
  },
  {
    path: "/campaigns/:campaignNo",
    component: CampaignDetail,
    children: [
      {
        path: "",
        name: "CampaignDetailInfo",
        component: CampaignDetailInfo,
      },
      {
        path: "certificate",
        name: "CampaignDetailCertifi",
        component: CampaignDetailCertifi,
      },
      {
        path: "postings",
        name: "CampaignDetailPostings",
        component: CampaignDetailPostings,
      },
    ],
  },
  {
    path: "/campaigns/make/:type",
    name: "CampaignMake",
    component: CampaignMake,
  },
  // Campaign End

  // Market Start
  {
    path: "/market",
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
    path: "/market",
    component: MarketLayout,
    props: { sidebar: false },
    children: [
      {
        path: "make",
        name: "MarketMakeView",
        component: MarketMakeView,
      },
      {
        path: "update/:productNo",
        name: "MarketUpdateView",
        component: MarketUpdateView,
      },
    ],
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
