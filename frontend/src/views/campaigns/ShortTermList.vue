<template>
  <div>
    <div class="section">
      <v-container>
        <div class="campaign-title">
          <h1>기업 캠페인</h1>
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
        <h1 class="campaign-title">공식 캠페인</h1>
        <v-row>
          <v-col sm="12" md="4">
            <div @click="goCampaignDetail">
              <CampaignCard />
            </div>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<script>
import CampaignCard from "../../components/CampaignCard.vue";
import CompanyCampaignCard from "../../components/CompanyCampaignCard.vue";
import { mapGetters } from "vuex";
import axios from "axios";
import SERVER from "@/api/api";

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
  created() {
    this.getCampaignInfo("company", 1);
    this.getCampaignInfo("official", 1);
  },
  computed: {
    ...mapGetters(["config"]),
  },
  methods: {
    getCampaignInfo(type, pageNo) {
      axios
        .get(
          SERVER.URL + SERVER.ROUTES.campaigns.URL + "/" + type + "/" + pageNo
        )
        .then((res) => console.log(res))
        .catch((err) => console.log(err));
    },
    goCampaignDetail() {
      this.$router.push({ name: "CampaignDetail" });
    },
  },
};
</script>

<style scoped>
.section {
  margin-top: 30px;
  margin-bottom: 100px;
  background: #fcfcfc;
}

.campaign-title {
  margin: 30px 0;
  font-family: "NanumBarunpen";
}
</style>
