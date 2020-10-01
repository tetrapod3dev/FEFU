<template>
  <div>
    <div class="section">
      <v-container>
        <v-row v-if="campaignType.id == 1" class="mb-8">
          <v-col cols="12" md="7">
            <h1 class="c-title text-left">
              {{ campaignType.name }} - {{ state }}
            </h1>
          </v-col>

          <v-col cols="3" md="1">
            <v-menu offset-y>
              <template v-slot:activator="{ on, attrs }">
                <button class="c-btn" v-bind="attrs" v-on="on">
                  {{ state }}
                </button>
              </template>
              <v-list>
                <v-list-item
                  v-for="(item, index) in items"
                  :key="index"
                  @click="state = item"
                >
                  <v-list-item-title class="c-txt">{{
                    item
                  }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
          </v-col>
          <v-col cols="6" md="3">
            <input
              type="text"
              class="campaign-search"
              placeholder="🔍 검색어를 입력하세요"
            />
          </v-col>
          <v-col cols="3" md="1">
            <router-link
              tag="button"
              class="c-btn c-primary"
              :to="{
                name: 'CampaignMake',
                params: { type: campaignType.id },
              }"
            >
              등록
            </router-link>
          </v-col>
        </v-row>
        <v-row v-else class="mb-8">
          <v-col cols="12" md="8">
            <h1 class="c-title text-left">
              {{ campaignType.name }}
            </h1>
          </v-col>
          <v-col cols="9" md="3"
            ><input
              type="text"
              class="campaign-search"
              placeholder="🔍 검색어를 입력하세요"
            />
          </v-col>
          <v-col cols="3" md="1">
            <router-link
              tag="button"
              class="c-btn c-primary"
              :to="{
                name: 'CampaignMake',
                params: { type: campaignType.id },
              }"
            >
              등록
            </router-link>
          </v-col>
        </v-row>

        <v-row>
          <v-col
            cols="12"
            sm="6"
            md="4"
            v-for="(campaign, idx) in campaigninfo"
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
      </v-container>
    </div>
  </div>
</template>

<script>
import CampaignCard from "../../components/campaign/CampaignCard.vue";

export default {
  props: {
    campaignType: Object,
    campaigninfo: Array,
  },
  mounted() {
    console.log(this.campaigninfo);
    console.log(this.campaignType);
  },
  components: {
    CampaignCard,
  },
  data() {
    return {
      state: "전체",
      items: ["전체", "진행 중", "오픈 예정", "종료 된"],
      // campaigninfo: [
      //   {
      //     title: "분리수거해요",
      //     org: "경기도시공사",
      //     valueDeterminate: 50,
      //     src: "4.png",
      //   },
      //   {
      //     title: "에코영수증캠페인",
      //     org: "환경부",
      //     valueDeterminate: 34,
      //     src: "5.png",
      //   },
      //   {
      //     title: "분바스틱캠페인",
      //     org: "바나나맛우유",
      //     valueDeterminate: 79,
      //     src: "6.png",
      //   },
      // ],
    };
  },
};
</script>

<style lang="scss" scoped>
.c-txt {
  font-family: "S-CoreDream-7ExtraBold";
  font-size: 1rem;
}

.section {
  margin-top: 30px;
  margin-bottom: 100px;
  background: #fcfcfc;
}

.c-title {
  font-family: "NanumBarunpen";
}

.c-primary {
  background-color: var(--primary-color);
}

.c-btn {
  @extend .c-txt;
  width: 100%;
  height: 48px;

  border: 2px solid black;
  border-radius: 10px;
  text-align: center;

  &:focus {
    outline: none;
  }
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

.c-select {
  border: 2px solid #000000;
}
</style>
