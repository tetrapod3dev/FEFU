import axios from "axios";

import SERVER from "@/api/api";
// import router from "@/router";

export default {
  namespaced: true,
  state: {},
  getters: {},
  mutations: {},
  actions: {
    getCampaignInfo(type, pageNo) {
      axios
        .get(
          SERVER.URL + SERVER.ROUTES.campaigns.URL + "/" + type + "/" + pageNo
        )
        .catch((err) => console.log(err));
    },
    goCampaignDetail() {
      this.$router.push({
        name: "CampaignDetailInfo",
        params: { CampaignNo: 1 },
      });
    },
  },
};
