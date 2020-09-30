<template>
  <div id="campaign-list">
    <section id="section-hero">
      <v-img
        id="about-hero"
        style="position: absolute"
        position="top"
        :height="$vuetify.breakpoint.smAndDown ? '24vh' : '49vh'"
        src="@/assets/images/campaign-hero.jpg"
        lazy-src="@/assets/images/lazy-loading.jpg"
      >
        <template v-slot:placeholder>
          <v-row class="fill-height ma-0" align="center" justify="center">
            <v-progress-circular
              indeterminate
              color="grey lighten-5"
            ></v-progress-circular>
          </v-row>
        </template>
      </v-img>
      <v-img
        style="position: relative; z-index: 3"
        position="bottom"
        :height="$vuetify.breakpoint.smAndDown ? '25vh' : '50vh'"
        src="@/assets/illust/campaign-hero.svg"
      />
    </section>

    <v-container>
      <v-row>
        <v-col cols="12" sm="3">
          <!-- 사이드바 -->
          <SideBar :campaign="campaign" />
          <ProofCreateBtn v-if="isJoined" :campaign="campaign" />

          <button
            v-if="!isJoined"
            @click="joinCampaign"
            class="custom-make-btn"
          >
            캠페인 신청
          </button>
        </v-col>

        <v-col cols="12" sm="9" class="pt-0">
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
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import UserCertificatePosts from "@/components/campaign/UserCertificatePosts.vue";
import SideBar from "@/components/campaign/SideBar.vue";
import ProofCreateBtn from "@/components/campaign/ProofCreateBtn.vue";

import { mapGetters } from "vuex";
import axios from "axios";
import SERVER from "@/api/api";
import router from "@/router";

export default {
  components: {
    UserCertificatePosts,
    SideBar,
    ProofCreateBtn,
  },
  created() {
    this.proofPost.writer = this.USERNAME;
    this.getIsJoinedCampaign();
  },
  mounted() {
    this.getCampaign();
  },
  computed: {
    ...mapGetters("accounts", ["config", "USERNAME"]),
  },
  data() {
    return {
      isJoined: false,
      listColorName: [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "purple",
      ],
      items: [
        { name: "캠페인소개", link: "CampaignDetail" },
        { name: "인증현황", link: "CampaignCertifi" },
        { name: "인증게시판", link: "CampaignPostings" },
      ],
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
    getIsJoinedCampaign() {
      let configs = {
        headers: {
          Authorization: this.config,
        },
      };
      axios
        .get(
          SERVER.URL +
            SERVER.ROUTES.campaigns.join +
            "/" +
            this.$route.params.campaignNo,
          configs
        )
        .then((res) => {
          this.isJoined = res.data;
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
    joinCampaign() {
      let configs = {
        headers: {
          Authorization: this.config,
        },
      };
      let body = {
        campaign_no: this.$route.params.campaignNo,
      };
      axios
        .post(SERVER.URL + SERVER.ROUTES.campaigns.join, body, configs)
        .then((res) => {
          if (res.data == "success") {
            alert("신청 완료 되었습니다.");
            router
              .push({
                name: "CampaignDetail",
                params: { campaignNo: this.$route.params.campaignNo },
              })
              .then(() => {
                location.reload();
              })
              .catch((error) => {
                if (error.name === "NavigationDuplicated") {
                  location.reload();
                }
              });
          }
        })
        .catch((err) => {
          console.log(err.response);
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
