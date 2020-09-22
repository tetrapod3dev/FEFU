<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="10">
        <v-img
          class="campaign-header-img"
          height="200px"
          src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
        >
          <div class="campaign-header-content">
            <p class="mb-0">{{campaign_info.title}}</p>
            <p class="mb-0">{{campaign_info.date}}</p>
          </div>
        </v-img>

        <v-tabs v-model="tab" centered grow color="#222">
          <v-tab v-for="item in items" :key="item" style="background: #fcfcfc">
            <span>{{ item }}</span>
          </v-tab>
        </v-tabs>
        <v-tabs-items v-model="tab">
          <v-tab-item v-for="item in items" :key="item" style="background: #fcfcfc">
            <CampaignInfo v-if="item=='소개'" />
            <CampaignCertificate v-if="item=='인증'" />
          </v-tab-item>
        </v-tabs-items>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import CampaignCertificate from "../../components/campaign/CampaignCertificate.vue";
import CampaignInfo from "../../components/campaign/CampaignInfo.vue";

export default {
  components: {
    CampaignCertificate,
    CampaignInfo,
  },
  data() {
    return {
      campaign_info: {
        title: "캠페인 제목",
        date: "2019-11-12",
      },
      tab: null,
      items: ["소개", "인증"],
    };
  },
};
</script>

<style scoped>
.campaign-header-img {
  position: relative;
  border: 2px solid black;
  border-radius: 15px;
}

.campaign-header-content {
  position: absolute;
  color: white;
  left: 0;
  right: 0;
  top: 90px;
}
</style>