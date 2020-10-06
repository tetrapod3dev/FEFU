import Vue from "vue";
import VueRouter from "vue-router";

// Home
import Home from "../views/Home.vue";
import ErrorPage from "../views/ErrorPage.vue";

// Account
import LoginView from "../views/accounts/LoginView.vue";
import SignupView from "../views/accounts/SignupView.vue";
import Mypage from "../views/accounts/Mypage.vue";
import MypageInfoUpdate from "../views/accounts/MypageInfoUpdate.vue";
import MypageEcoPoint from "../views/accounts/MypageEcoPoint.vue";
import MypageListCampaignAdmin from "../views/accounts/MypageListCampaignAdmin.vue";
import MypageListCampaignJoin from "../views/accounts/MypageListCampaignJoin.vue";
import MypageListProduct from "../views/accounts/MypageListProduct.vue";
import MypageInfo from "../views/accounts/MypageInfo.vue";
import MypageUpdatePwd from "../views/accounts/MypageUpdatePwd.vue";

MypageEcoPoint
// Campaigns
import CampaignLayout from "../views/campaigns/CampaignLayout.vue";
import CampaignMain from "../views/campaigns/CampaignMain.vue";
import CampaignMake from "../views/campaigns/CampaignMake.vue";
import CampaignDetail from "../views/campaigns/CampaignDetail.vue";
import CampaignDetailCertifi from "../views/campaigns/CampaignDetailCertifi.vue";
import CampaignDetailInfo from "../views/campaigns/CampaignDetailInfo.vue";
import CampaignDetailPostings from "../views/campaigns/CampaignDetailPostings.vue";
import CampaignDetailAdmin from "../views/campaigns/CampaignDetailAdmin.vue";
import CampaignTypeList from "../views/campaigns/CampaignTypeList.vue";

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
        path: "info",
        name: "MypageInfo",
        component: MypageInfo,
      },
      {
        path: "eco",
        name: "MypageEcoPoint",
        component: MypageEcoPoint,
      },
      {
        path: "update",
        name: "MypageInfoUpdate",
        component: MypageInfoUpdate,
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
    name: "CampaignLayout",
    component: CampaignLayout,
    children: [
      {
        path: "main",
        name: "CampaignMain",
        component: CampaignMain,
      },
      {
        path: "make/:type",
        name: "CampaignMake",
        component: CampaignMake,
      },
      {
        path: "list/:campaign_type/:page_num/:title?",
        name: "CampaignTypeList",
        component: CampaignTypeList,
      },
      {
        path: "detail/:campaignNo",
        component: CampaignDetail,
        children: [
          {
            path: "info",
            name: "CampaignDetailInfo",
            component: CampaignDetailInfo,
            props: true,
          },
          {
            path: "certificate",
            name: "CampaignDetailCertifi",
            component: CampaignDetailCertifi,
            props: true,
          },
          {
            path: "postings/:page_no",
            name: "CampaignDetailPostings",
            component: CampaignDetailPostings,
            props: true,
          },
          {
            path: "admin/:page_no",
            name: "CampaignDetailAdmin",
            component: CampaignDetailAdmin,
            props: true,
          },
        ],
      },
    ],
  },

  // Campaign End

  // Market Start
  {
    path: "/market",
    component: MarketLayout,
    children: [
      {
        path: "main",
        name: "MarketMainView",
        component: MarketMainView,
      },
      {
        path: "list/:pageNum/:mainCategoryNo?/:mediumCategoryNo?/:content?",
        name: "MarketListView",
        component: MarketListView,
        props: true,
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
