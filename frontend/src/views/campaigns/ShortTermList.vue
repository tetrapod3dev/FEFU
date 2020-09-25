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
            <CompanyCampaignCard
              :campaign="campaigninfo[0]"
              :src="require('@/assets/campaign/' + campaigninfo[0].src)"
            />
          </v-col>
        </v-row>
      </v-container>
      <v-btn>더보기</v-btn>
    </div>

    <div class="section">
      <v-container>
        <h1 class="campaign-title">공식 캠페인</h1>
        <v-row>
          <v-col sm="12" md="4">
            <div @click="goCampaignDetail">
              <CampaignCard
                :campaign="campaigninfo[1]"
                :src="require('@/assets/campaign/' + campaigninfo[1].src)"
              />
            </div>
          </v-col>
        </v-row>
      </v-container>
      <v-btn>
        <!-- <router-link :to="{ name: 'CompanyCampaignList' }">더보기</router-link> -->
        <div @click="goCompanyCampaignList">
          <button>더보기</button>
        </div>
      </v-btn>
    </div>
  </div>
</template>

<script>
import CampaignCard from "../../components/campaign/CampaignCard.vue";
import CompanyCampaignCard from "../../components/campaign/CompanyCampaignCard.vue";
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
    goCompanyCampaignList() {
      this.$router.push({ name: "CompanyCampaignList" });
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
