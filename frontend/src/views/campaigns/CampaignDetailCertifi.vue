<template>
  <div class="campaign-info d-flex flex-column">
    <BarChart v-if="campaign.type == 'official'" />
    <UserCertificate v-if="campaign.type == 'personal'" />
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
  props: ["campaign", "campaignTypeInfo"],
  components: {
    BarChart,
    UserCertificate,
  },
  created() {
    this.getPersonalPercentTeam();
  },
  computed: {
    ...mapGetters("accounts", ["config"]),
  },
  data() {
    return {};
  },
  methods: {
    imageSrc(filename) {
      return SERVER.IMAGE_URL + filename;
    },
    getPersonalPercentTeam() {
      axios
        .get(
          SERVER.URL +
            SERVER.ROUTES.campaigns.personalPercentTeam +
            "/" +
            this.$route.params.campaignNo
        )
        .then((res) => {
          console.log(res);
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
