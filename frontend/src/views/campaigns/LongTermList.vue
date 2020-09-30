<template>
  <div>
    <div class="section">
      <v-container>
        <h1 class="campaign-title">
          현재
          <span class="title-point">진행중인</span> 캠페인
        </h1>
        <v-row>
          <v-col
            v-for="n in 3"
            :key="n"
            cols="12"
            md="4"
            @click="goCampaignDetail"
          >
            <CampaignCard
              :campaign="campaigninfo[n - 1]"
              :src="require('@/assets/campaign/' + campaigninfo[n - 1].src)"
            />
          </v-col>
        </v-row>
      </v-container>
    </div>

    <div class="section">
      <v-container>
        <h1 class="campaign-title">
          <span class="title-point">오픈 예정</span> 캠페인
        </h1>
        <v-row>
          <v-col v-for="n in 3" :key="n" cols="12" md="4">
            <CampaignCard
              :campaign="campaigninfo[n - 1]"
              :src="require('@/assets/campaign/' + campaigninfo[n - 1].src)"
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
  components: {
    CampaignCard,
  },
  data() {
    return {
      campaigninfo: [
        {
          title: "분리수거해요",
          org: "경기도시공사",
          valueDeterminate: 50,
          src: "4.png",
        },
        {
          title: "에코영수증캠페인",
          org: "환경부",
          valueDeterminate: 34,
          src: "5.png",
        },
        {
          title: "분바스틱캠페인",
          org: "바나나맛우유",
          valueDeterminate: 79,
          src: "6.png",
        },
      ],
    };
  },
  methods: {
    goCampaignDetail() {
      this.$router.push({
        name: "CampaignDetailInfo",
        params: { CampaignNo: 1 },
      });
    },
  },
};
</script>

<style scoped>
.section {
  margin-top: 30px;
  margin-bottom: 70px;
  background: #fcfcfc;
}

.campaign-title {
  margin: 30px 0;
  font-family: "NanumBarunpen";
}

.title-point {
  color: var(--primary-color);
}
</style>
