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
          <!-- <SideBar :campaign="campaign" /> -->
          <v-img
            class="campaign-header-img"
            height="200px"
            :src="
              campaign.photo
                ? imageSrc(campaign.photo)
                : '@/assets/images/lazy-loading.jpg'
            "
            lazy-src="@/assets/images/lazy-loading.jpg"
          >
            <template v-slot:placeholder>
              <lazy-loading />
            </template>
          </v-img>

          <div v-if="campaign">
            <v-list v-if="campaign.type != 'company'" class="custom-list">
              <v-list-item
                v-for="(item, index) in items"
                :key="index"
                no-action
                class="custom-list-item"
                :class="`custom-list-item-${
                  listColorName[index % listColorName.length]
                }`"
                :to="{
                  name: item.link,
                  params: {
                    campaignNo: campaign.no,
                    ...item.params,
                  },
                }"
              >
                <v-list-item-content>
                  <v-list-item-title v-text="item.name"></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-list-item
                v-if="campaign.writer == USERNAME"
                no-action
                class="custom-list-item"
                :class="`custom-list-item-${listColorName[4]}`"
                :to="{
                  name: 'CampaignDetailAdmin',
                  params: {
                    campaignNo: campaign.no,
                    page_no: 1,
                  },
                }"
              >
                <v-list-item-content>
                  <v-list-item-title v-text="'인증관리'"></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list>
            <v-list v-if="campaign.type == 'company'" class="custom-list">
              <v-list-item
                no-action
                class="custom-list-item"
                :class="`custom-list-item-${listColorName[1]}`"
                :to="{
                  name: 'CampaignDetailInfo',
                  params: {
                    campaignNo: campaign.no,
                  },
                }"
              >
                <v-list-item-content>
                  <v-list-item-title v-text="'캠페인소개'"></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </div>

          <a
            v-if="campaign.type == 'company'"
            :href="'//' + company.campaignLink"
            target="_blank"
            class="custom-make-btn py-3 mt-5"
            style="
              display: block;
              text-decoration: none;
              color: black;
              width: 100%;
            "
          >
            사이트 가기
          </a>

          <ProofCreateBtn
            v-if="campaign.type != 'company' && isJoined"
            :campaign="campaign"
          />

          <button
            v-if="campaign.type != 'company' && !isJoined"
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
            <router-view
              :campaign="campaign"
              :campaignTypeInfo="campaignTypeInfo"
            />
          </v-container>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
// import SideBar from "@/components/campaign/SideBar.vue";
import ProofCreateBtn from "@/components/campaign/ProofCreateBtn.vue";
// import CampaignCertificate from "../../components/campaign/CampaignCertificate.vue";
// import CampaignInfo from "../../components/campaign/CampaignInfo.vue";

import { mapGetters } from "vuex";
import axios from "axios";
import SERVER from "@/api/api";
import router from "@/router";

export default {
  components: {
    // SideBar,
    ProofCreateBtn,
    // CampaignCertificate,
    // CampaignInfo,
  },
  created() {
    this.getCampaign();
    this.getIsJoinedCampaign();
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
        { name: "캠페인소개", link: "CampaignDetailInfo", params: {} },
        { name: "인증현황", link: "CampaignDetailCertifi", params: {} },
        {
          name: "인증게시판",
          link: "CampaignDetailPostings",
          params: { page_no: 1 },
        },
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
        requirement: null,
      },
      company: {
        campaignLink: "",
        campaignNo: 0,
        companyName: "",
        no: 0,
      },
    };
  },
  computed: {
    ...mapGetters("accounts", ["config", "USERNAME"]),
  },
  methods: {
    imageSrc(filename) {
      return SERVER.IMAGE_URL + filename;
    },
    openCompanySite() {
      window.open(this.company.campaignLink);
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
          console.log(res);
          this.campaign = res.data["campaign"];
          if (res.data["company"]) {
            this.company = res.data["company"];
          }
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
                name: "CampaignDetailInfo",
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

.campaign-info {
  font-family: "NanumBarunpen";
  border: 2px solid black;
  border-radius: 5px;
  padding: 10px 20px;
  margin: 10px 0;
}

.campaign-info-list {
  margin: 10px 0;
  background-color: rgba(55, 205, 194, 0.09);
  border-radius: 10px;
  font-family: "S-CoreDream-7ExtraBold";
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

.campaign-header-img {
  border: 2px solid black;
  border-radius: 15px;
}
.custom-list {
  margin-top: 20px;
  font-family: "S-CoreDream-7ExtraBold";
}
.custom-list-item {
  border: 2px solid black;
  &:first-child {
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
  }
  &:last-child {
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
  }

  &:not(:last-child) {
    // border-bottom: 2px solid black;
    margin-bottom: -2px;
  }

  &-red.v-list-group--active,
  &-red:hover {
    background: #cf6a87;
  }

  &-orange.v-list-group--active,
  &-orange:hover {
    background: #f19066;
  }

  &-yellow.v-list-group--active,
  &-yellow:hover {
    background: #fdcb6e;
  }

  &-green.v-list-group--active,
  &-green:hover {
    background: #b8e994;
  }

  &-blue.v-list-group--active,
  &-blue:hover {
    background: #82ccdd;
  }

  &-indigo.v-list-group--active,
  &-indigo:hover {
    background: #60a3bc;
  }

  &-purple.v-list-group--active,
  &-purple:hover {
    background: #786fa6;
  }
}
</style>
