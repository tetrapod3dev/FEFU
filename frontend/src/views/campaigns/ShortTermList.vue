<template>
  <div>
    <div class="section">
      <v-container>
        <div class="d-flex justify-space-between">
          <h3 class="text-left">기업 캠페인</h3>
          <p>* 클릭하시면 해당 기업 캠페인 페이지로 이동합니다.</p>
        </div>
        <v-row>
          <v-col sm="12" md="4">
            <CompanyCampaignCard />
          </v-col>
        </v-row>
      </v-container>
    </div>

    <div class="section">
      <v-container>
        <h3 class="text-left">공식 캠페인</h3>
        <v-row>
          <v-col sm="12" md="4">
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
  data() {
    return {
      campaigninfo: [],
    };
  },
};
</script>

<style scoped>
.section {
  margin-top: 30px;
  margin-bottom: 100px;
}
</style>
