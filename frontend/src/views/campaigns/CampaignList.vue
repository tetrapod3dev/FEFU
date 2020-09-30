<template>
  <div>
    <div class="section">
      <v-container>
        <div class="campaign-title">
          <div v-if="campaignType.id == 1">
            <v-row>
              <v-col cols="6">
                <h1 class="text-left">{{ campaignType.name }} - {{ state }}</h1>
              </v-col>

              <v-col cols="2">
                <v-select v-model="state" :items="items" outlined></v-select>
              </v-col>
              <v-col cols="2"
                ><input
                  type="text"
                  class="campaign-search"
                  placeholder="🔍 검색어를 입력하세요"
                />
              </v-col>
              <v-col cols="2"
                ><router-link
                  tag="button"
                  class="custom-make-btn"
                  :to="{
                    name: 'CampaignMake',
                    params: { type: campaignType.id },
                  }"
                >
                  캠페인 등록
                </router-link></v-col
              >
            </v-row>
          </div>
          <div v-else>
            <v-row>
              <v-col cols="8">
                <h1 class="text-left">{{ campaignType.name }}</h1>
              </v-col>
              <v-col cols="2"
                ><input
                  type="text"
                  class="campaign-search"
                  placeholder="🔍 검색어를 입력하세요"
                />
              </v-col>
              <v-col cols="2"
                ><router-link
                  tag="button"
                  class="custom-make-btn"
                  :to="{
                    name: 'CampaignMake',
                    params: { type: campaignType.id },
                  }"
                >
                  캠페인 등록
                </router-link></v-col
              >
            </v-row>
          </div>
        </div>

        <v-row>
          <v-col
            sm="12"
            md="4"
            v-for="(campaign, idx) in campaigninfo"
            :key="idx"
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
.section {
  margin-top: 30px;
  margin-bottom: 100px;
  background: #fcfcfc;
}

.campaign-title {
  margin: 30px 0;
  font-family: "NanumBarunpen";
}

.custom-make-btn {
  font-family: "S-CoreDream-7ExtraBold";
  font-size: 1rem;
  width: 100%;
  height: 48px;
  background-color: var(--primary-color);
  border: 2px solid black;
  border-radius: 10px;
  text-align: center;

  &:focus {
    outline: none;
  }
}

.campaign-search {
  border: 2px solid black;
  border-radius: 10px;
  padding: 7px 10px;
  text-align: start;
  width: 100%;
  height: 48px;
  font-family: "NanumBarunpen";

  &:focus {
    outline: none;
  }
}
</style>
