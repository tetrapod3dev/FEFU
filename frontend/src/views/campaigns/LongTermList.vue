<template>
  <div>
    <div class="section">
      <v-container>
        <h1 class="campaign-title">
          현재
          <span class="title-point">진행중인</span> 캠페인
        </h1>
        <v-row>
          <v-col v-for="n in 6" :key="n" cols="12" md="4">
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
          <v-col v-for="n in 6" :key="n" cols="12" md="4">
            <CampaignCard />
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<script>
import CampaignCard from "../../components/CampaignCard.vue";

export default {
  components: {
    CampaignCard,
  },
  data() {
    return {};
  },
};
</script>

<style scoped>
.section {
  margin-top: 30px;
  margin-bottom: 70px;
}

.campaign-title {
  margin: 30px 0;
}

.title-point {
  color: #23efb8;
}
</style>
