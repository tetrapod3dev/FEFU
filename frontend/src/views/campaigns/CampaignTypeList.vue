<template>
  <v-container>
    <v-row class="mb-8">
      <v-col cols="12" sm="8" lg="9">
        <h1 class="c-title text-left">
          검색 정보 - {{ types[campaignType].name }}
        </h1>
      </v-col>
      <v-col cols="12" sm="4" lg="3">
        <!-- 검색의 경우 음... 음... router 링크만 바꾸면 되는거라서 그냥 keydown과 click 시에 해당 함수가 호출되도록 했습니다.-->
        <input
          v-model="searchInput"
          type="text"
          class="campaign-search"
          placeholder="🔍 검색어를 입력하세요"
          @keydown.enter="searchCampaign"
        />
      </v-col>
    </v-row>
    <v-row v-if="endPage == 0">
      <h1 class="mx-auto">없어요!</h1>
    </v-row>
    <v-row v-else>
      <v-col
        cols="12"
        sm="6"
        md="4"
        v-for="(campaign, idx) in campaigns"
        :key="idx"
        align="center"
      >
        <CampaignCard
          :campaign="campaign"
          :to="{
            name: 'CampaignDetailInfo',
            params: { campaignNo: campaign.no },
          }"
        />
      </v-col>
    </v-row>

    <core-pagination
      :curPage="curPage"
      :maxPage="endPage"
      @move-page="movePage"
    />
  </v-container>
</template>

<script>
import SERVER from "@/api/api";
import axios from "axios";

import CampaignCard from "@/components/campaign/CampaignCard.vue";
import CorePagination from "@/components/core/Pagination";

export default {
  name: "CampaignTypeList",
  components: {
    CampaignCard,
    CorePagination,
  },
  data() {
    return {
      campaignType: this.$route.params.campaign_type,
      types: [
        { type: "", name: "" },
        { type: "personal", name: "100일캠페인" },
        { type: "company", name: "기업캠페인" },
        { type: "official", name: "공식캠페인" },
      ],
      campaigns: [],
      endPage: 0,
      searchInput: "",
    };
  },
  created() {
    this.getCampaignList();
    this.searchInput = this.searchTitle;
  },
  computed: {
    // router push로 다른 router로 이동시킨 후에 그걸 자동으로 다시 대입하기 위해 computed에 넣었습니다.
    curPage() {
      return parseInt(this.$route.params.page_num);
    },
    searchTitle() {
      return this.$route.params.title;
    },
    type() {
      return this.searchTitle != undefined ? "title" : "";
    },
    content() {
      return this.searchTitle != undefined ? this.searchTitle : "";
    },
  },
  watch: {
    // router link의 title과 page를 감시합니다.. (변경될 경우 캠페인 리스트를 새로 불러옵니다.)
    searchTitle() {
      this.getCampaignList();
    },
    curPage() {
      this.getCampaignList();
    },
  },
  methods: {
    // 주어진 조건에 따라 캠페인 리스트를 새로 불러오기 위한 함수입니다.
    // campaign_type은 한번 정해지면 안 바뀌니까 그냥 data에서 가져왔고,
    // curPage와 content와 type은 계속 바뀌면서 그에 따라 적절한 값을 넣어줘야돼서 computed에서 가져왔습니다.
    getCampaignList() {
      axios
        .get(SERVER.URL + SERVER.ROUTES.campaigns.URL, {
          params: {
            campaign_type: this.types[this.campaignType].type,
            page_no: this.curPage,
            content: this.content,
            type: this.type,
          },
        })
        .then((res) => {
          this.campaigns = res.data.list;
          this.endPage = res.data.page.endPage;
        })
        .catch((err) => console.log(err));
    },
    searchCampaign() {
      // 검색어를 입력할 경우 router link를 바꾸기 위한 함수입니다.
      // router push에서 title: ""이 들어갈 경우 문제가 되기 때문에 분기를 나누어서
      // title이 없는 경우는 아예 안 보내도록 했습니다.
      if (this.searchInput != "") {
        this.$router.push({
          name: "CampaignTypeList",
          params: {
            campaign_type: this.campaignType,
            page_num: 1,
            title: this.searchInput,
          },
        });
      } else {
        this.$router.push({
          name: "CampaignTypeList",
          params: {
            campaign_type: this.campaignType,
            page_num: 1,
          },
        });
      }
    },
    movePage(page) {
      if (page == "«") {
        this.$router.push({ params: { page_num: 1 } });
      } else if (page == "»") {
        this.$router.push({ params: { page_num: this.endPage } });
      } else {
        this.$router.push({ params: { page_num: parseInt(page) } });
      }
      scroll(0, 0);
    },
  },
};
</script>

<style lang="scss" scoped>
.c-title {
  font-family: "NanumBarunpen";
}

.campaign-search {
  font-family: "NanumBarunpen";
  text-align: start;
  border: 2px solid black;
  border-radius: 10px;
  padding: 7px 10px;
  width: 100%;
  height: 48px;

  &:focus {
    outline: none;
  }
}
</style>