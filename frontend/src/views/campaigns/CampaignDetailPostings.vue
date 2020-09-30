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
        <UserCertificatePosts />
      </div>
    </v-container>
  </div>
</template>

<script>
import UserCertificatePosts from "@/components/campaign/UserCertificatePosts.vue";

import { mapGetters } from "vuex";
import axios from "axios";
import SERVER from "@/api/api";

export default {
  components: {
    UserCertificatePosts,
  },
  created() {
    this.proofPost.writer = this.USERNAME;
  },
  mounted() {
    this.getCampaign();
  },
  computed: {
    ...mapGetters("accounts", ["config", "USERNAME"]),
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
        requirement: "",
      },
      url: null,
      images: null,
      imageRules: [
        (value) =>
          !value ||
          value.size < 2000000 ||
          "이미지 파일은 최대 2 MB까지 가능해요",
      ],
      proofPost: {
        campaignNo: null,
        title: "",
        content: "",
        photo: "",
        writer: "",
      },
      user: null,
    };
  },
  methods: {
    getUserInfo() {
      let configs = {
        headers: {
          Authorization: this.config,
        },
      };
      axios
        .get(SERVER.URL + SERVER.ROUTES.myPage, configs)
        .then((res) => {
          this.user = res.data.user;
        })
        .catch((err) => console.log(err.response));
    },

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
          this.proofPost.campaignNo = res.data["campaign"].no;
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
