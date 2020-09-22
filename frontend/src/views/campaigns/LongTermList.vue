<template>
  <div>
    <div class="section">
      <v-container>
        <h1 class="campaign-title">
          현재
          <span class="title-point">진행중인</span> 캠페인
        </h1>
        <v-row>
          <v-col v-for="n in 3" :key="n" cols="12" md="4" @click="goCampaignDetail">
            <CampaignCard />
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
            <CampaignCard />
          </v-col>
        </v-row>
      </v-container>
    </div>

    <div class="section">
      <v-btn>캠페인 만들기</v-btn>
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
    return {};
  },
  methods: {
    goCampaignDetail() {
      this.$router.push({ name: "CampaignDetail" });
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
