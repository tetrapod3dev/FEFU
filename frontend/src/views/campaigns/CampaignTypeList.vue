<template>
  <div>
    <section id="section-hero">
      <v-img
        id="about-hero"
        style="position: absolute"
        position="top"
        :height="$vuetify.breakpoint.smAndDown ? '24vh' : '49vh'"
        src="@/assets/images/campaign-hero.jpg"
        lazy-src="@/assets/images/lazy-loading.jpg"
      >
        <template v-slot:placeholder>
          <v-row class="fill-height ma-0" align="center" justify="center">
            <v-progress-circular
              indeterminate
              color="grey lighten-5"
            ></v-progress-circular>
          </v-row>
        </template>
      </v-img>
      <v-img
        style="position: relative; z-index: 3"
        position="bottom"
        :height="$vuetify.breakpoint.smAndDown ? '25vh' : '50vh'"
        src="@/assets/illust/campaign-hero.svg"
      />
    </section>

    <h1>검색 정보</h1>
    <p>{{ types[campaignType] }} / {{ curPage }} / {{ searchTitle }}</p>

    <!-- 검색의 경우 음... 음... router 링크만 바꾸면 되는거라서 그냥 keydown과 click 시에 해당 함수가 호출되도록 했습니다.-->
    <input 
      v-model="searchInput"
      type="text"
      class="campaign-search"
      placeholder="🔍 검색어를 입력하세요"
      @keydown.enter="searchCampaign"
    >
    <button @click="searchCampaign">
      검색
    </button>

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

    <div v-if="endPage != 0">
      <!-- endPage가 0이면 검색결과가 없으니까, 그냥 페이지네이션 버튼 자체가 안 나오게 했습니다.
      pagination은 좀 더 깔끔한 방법이 있다면 수정하셔야 될것같습니다... 제가 하는건 그냥 돌아가게만 하는거라..-->
      <button v-if="curPage != 1" @click="movePage($event)">처음</button>
      <button v-if="curPage-2 >= 1" @click="movePage($event)">{{ curPage - 2 }}</button>
      <button v-if="curPage-1 >= 1" @click="movePage($event)">{{ curPage - 1 }}</button>
      <button>{{ curPage }}</button>
      <button v-if="curPage+1 <= endPage" @click="movePage($event)">{{ curPage + 1 }}</button>
      <button v-if="curPage+2 <= endPage" @click="movePage($event)">{{ curPage + 2 }}</button>
      <button v-if="curPage != endPage" @click="movePage($event)">마지막</button>
    </div>
  </div>
</template>

<script>
import SERVER from "@/api/api"
import axios from "axios"

import CampaignCard from "../../components/campaign/CampaignCard.vue";

export default {
  name: "CampaignTypeList",
  components: {
    CampaignCard,
  },
  data() {
    return {
      campaignType: this.$route.params.campaign_type,
      types: ["", "personal", "company", "official"],
      campaigns: [],
      endPage: 0,
      searchInput: "",
    }
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
        return (this.searchTitle != undefined) ? "title" : "";
    },
    content() {
        return (this.searchTitle != undefined) ? this.searchTitle : "";
    },
  },
  methods: {
    // 주어진 조건에 따라 캠페인 리스트를 새로 불러오기 위한 함수입니다.
    // campaign_type은 한번 정해지면 안 바뀌니까 그냥 data에서 가져왔고,
    // curPage와 content와 type은 계속 바뀌면서 그에 따라 적절한 값을 넣어줘야돼서 computed에서 가져왔습니다.
    getCampaignList() {
      axios
        .get(SERVER.URL + SERVER.ROUTES.campaigns.URL,
        {
          params: {
            "campaign_type": this.types[this.campaignType],
            "page_no": this.curPage,
            "content": this.content,
            "type": this.type
          }
        })
        .then(res => {
          console.log(res)
          this.campaigns = res.data.list;
          this.endPage = res.data.page.endPage;
        })
        .catch(err => console.log(err))
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
            title: this.searchInput
          },
        });
      } else {
        this.$router.push({
          name: "CampaignTypeList",
          params: {
            campaign_type: this.campaignType,
            page_num: 1,
          }
        });
      }
    },
    movePage(event) {
      // 페이지를 이동할 경우 router link를 바꾸기 위한 함수입니다.
      // router push에서 title: ""이 들어갈 경우 문제가 되기 때문에 분기를 나누어서
      // title이 없는 경우는 아예 안 보내도록 했습니다.
      let targetPage = 1
      if (event.target.outerText == '처음') {
        targetPage = 1
      } else if (event.target.outerText == '마지막') {
        targetPage = this.endPage
      } else {
        targetPage = event.target.outerText
      }
      if (this.searchInput != "") {
        this.$router.push({
          name: "CampaignTypeList",
          params: {
            campaign_type: this.campaignType,
            page_num: targetPage,
            title: this.searchInput
          },
        });
      } else {
        this.$router.push({
          name: "CampaignTypeList",
          params: {
            campaign_type: this.campaignType,
            page_num: targetPage,
          },
        });
      }
    },
  },
  watch: {
    // router link의 title과 page를 감시합니다.. (변경될 경우 캠페인 리스트를 새로 불러옵니다.)
    searchTitle() {
      this.getCampaignList();
    },
    curPage() {
      this.getCampaignList();
    }
  },
  created() {
    this.getCampaignList();
  },
}
</script>

<style lang="scss" scoped>
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