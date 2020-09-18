<template>
  <div>
    <div class="section">
      <v-container>
        <h3 class="text-left">현재 진행중인 캠페인</h3>
        <v-row>
          <v-col v-for="n in 6" :key="n" cols="12" md="4">
            <CampaignCard />
          </v-col>
        </v-row>
      </v-container>
    </div>

    <div class="section">
      <v-container>
        <h3 class="text-left">오픈 예정 캠페인</h3>
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
</style>
