<template>
  <div>
    <v-container justify="start">
      <div class="campaign-welcome">
        <span class="campaign-title">{{ campaign.title }}</span>
        <small class="ml-3">
          {{ campaign.startDate }} - {{ campaign.endDate }}
        </small>
      </div>

      <div class="campaign-info d-flex flex-column">
        <BarChart />
        <UserCertificate />
      </div>
    </v-container>
  </div>
</template>

<script>
import BarChart from "@/components/campaign/BarChart.vue";
import UserCertificate from "@/components/campaign/UserCertificate";

import { mapGetters } from "vuex";
import axios from "axios";
import SERVER from "@/api/api";

export default {
  name: "CampaignDetailCertifi",
  components: {
    BarChart,
    UserCertificate,
  },
  created() {
    this.getCampaign();
    console.log(this.$route.params);
  },
  computed: {
    ...mapGetters("accounts", ["config"]),
  },
  data() {
    return {
      campaign: {
        title: "",
        content: "",
        writer: "",
        startDate: "",
        endDate: "",
        photo: "",
        tag: [],
        type: "",
        no: 0,
      },
      campaignTypeInfo: {
        authEndTime: "",
        authProcess: "",
        authStartTime: "",
        campaignNo: null,
        headcount: null,
        mission: "",
        no: null,
        requirement: null,
      },
    };
  },
  methods: {
    imageSrc(filename) {
      return SERVER.IMAGE_URL + filename;
    },
    getCampaign() {
      axios
        .get(
          SERVER.URL +
            SERVER.ROUTES.campaigns.URL +
            "/" +
            this.$route.params.campaignNo +
            "/"
        )
        .then((res) => {
          this.campaign = res.data["campaign"];
          if (res.data["official"]) {
            this.campaignTypeInfo = res.data["official"];
          } else if (res.data["personal"]) {
            this.campaignTypeInfo = res.data["personal"];
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style lang="scss" scoped>
.campaign-welcome {
  border: 2px solid black;
  border-radius: 5px;
  padding: 10px 20px;
  margin: 10px 0;
  text-align: start;
}

.campaign-title {
  font-size: 1.5rem;
  font-family: "NanumBarunpen";
}

.capmaign-info {
  font-family: "NanumBarunpen";
}

.custom-white {
  background: var(--white-color);
}

.custom-make-btn {
  font-family: "S-CoreDream-7ExtraBold";
  font-size: 1rem;
  width: 100%;
  height: 48px;
  margin-top: 20px;
  background-color: var(--primary-color);
  border: 2px solid black;
  border-radius: 10px;
  text-align: center;
}
</style>
