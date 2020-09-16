<template>
  <div>
    <div class="section">
      <v-container>
        <h2 class="text-left">기업 캠페인</h2>
        <v-row>
          <v-col sm="12" md="6" lg="4">
            <CompanyCampaignCard />
          </v-col>
        </v-row>
      </v-container>
    </div>

    <div class="section">
      <v-container>
        <h2 class="text-left">공식 캠페인</h2>
        <v-row>
          <v-col sm="12" md="6" lg="4">
            <CampaignCard />
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<script>
import CampaignCard from "../../components/CampaignCard.vue";
import CompanyCampaignCard from "../../components/CompanyCampaignCard.vue";

export default {
  components: {
    CampaignCard,
    CompanyCampaignCard,
  },
};
</script>

<style scoped>
h2 {
  margin-top: 30px;
  margin-bottom: 30px;
}

.section {
  margin-top: 30px;
  margin-bottom: 100px;
}
</style>