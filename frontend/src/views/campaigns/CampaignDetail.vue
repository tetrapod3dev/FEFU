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
          <div :class="$vuetify.breakpoint.smAndDown ? '' : 'fixed-bar'">
            <!-- 사이드바 -->
            <SideBar :campaign="campaign" />

            <router-link
              tag="button"
              class="custom-make-btn"
              :to="{ name: 'MarketMakeView' }"
            >
              인증글작성
            </router-link>
          </div>
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
              <v-list class="campaign-info-list">
                <v-row>
                  <v-list-item class="campaign-info-list-item">
                    <v-col cols="2">
                      <v-list-item-content>
                        <v-list-item-title>인증 미션</v-list-item-title>
                      </v-list-item-content>
                    </v-col>
                    <v-col cols="10">
                      <v-list-item-content class="text-left">
                        <v-list-item-title>{{
                          campaignTypeInfo.mission
                        }}</v-list-item-title>
                      </v-list-item-content>
                    </v-col>
                  </v-list-item>
                </v-row>
                <v-row>
                  <v-list-item class="campaign-info-list-item">
                    <v-col cols="2">
                      <v-list-item-content>
                        <v-list-item-title>인증 방법</v-list-item-title>
                      </v-list-item-content>
                    </v-col>
                    <v-col cols="10">
                      <v-list-item-content class="text-left">
                        <v-list-item-title>{{
                          campaignTypeInfo.authProcess
                        }}</v-list-item-title>
                      </v-list-item-content>
                    </v-col>
                  </v-list-item>
                </v-row>
                <v-row>
                  <v-list-item class="campaign-info-list-item">
                    <v-col cols="2">
                      <v-list-item-content>
                        <v-list-item-title>인증 시간</v-list-item-title>
                      </v-list-item-content>
                    </v-col>
                    <v-col cols="10">
                      <v-list-item-content class="text-left">
                        <v-list-item-title
                          >{{ campaignTypeInfo.authStartTime }} -
                          {{ campaignTypeInfo.authEndTime }}</v-list-item-title
                        >
                      </v-list-item-content>
                    </v-col>
                  </v-list-item>
                </v-row>
                <v-row>
                  <v-list-item class="campaign-info-list-item">
                    <v-col cols="2">
                      <v-list-item-content>
                        <v-list-item-title>목표 인원</v-list-item-title>
                      </v-list-item-content>
                    </v-col>
                    <v-col cols="10">
                      <v-list-item-content class="text-left">
                        <v-list-item-title
                          >{{ campaignTypeInfo.headcount }}명
                        </v-list-item-title>
                      </v-list-item-content>
                    </v-col>
                  </v-list-item>
                </v-row>
                <v-row>
                  <v-list-item class="campaign-info-list-item">
                    <v-col cols="2">
                      <v-list-item-content>
                        <v-list-item-title>멤버 조건</v-list-item-title>
                      </v-list-item-content>
                    </v-col>
                    <v-col cols="10">
                      <v-list-item-content class="text-left">
                        <v-list-item-title>{{
                          campaignTypeInfo.requirement
                        }}</v-list-item-title>
                      </v-list-item-content>
                    </v-col>
                  </v-list-item>
                </v-row>
              </v-list>

              <p class="text-left mt-4 pa-1">{{ campaign.content }}</p>
              <v-chip-group>
                <v-chip
                  class="ma-1"
                  color="#38C0BD"
                  outlined
                  dense
                  v-for="tag in campaign.tag"
                  :key="tag"
                  >{{ tag }}</v-chip
                >
              </v-chip-group>
            </div>
          </v-container>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import SideBar from "@/components/campaign/SideBar.vue";
// import CampaignCertificate from "../../components/campaign/CampaignCertificate.vue";
// import CampaignInfo from "../../components/campaign/CampaignInfo.vue";

import axios from "axios";
import SERVER from "@/api/api";

export default {
  components: {
    SideBar,
    // CampaignCertificate,
    // CampaignInfo,
  },
  created() {
    this.getCampaign();
  },
  data() {
    return {
      listColorName: [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "purple",
      ],
      campaign_info: {
        title: "캠페인 제목",
        date: "2019-11-12",
      },
      tab: null,
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

.campaign-header-img {
  border: 2px solid black;
  border-radius: 15px;
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
.custom-list {
  margin-top: 20px;
  font-family: "S-CoreDream-7ExtraBold";
}

.campaign-info-list {
  margin: 10px 0;
  background-color: rgba(55, 205, 194, 0.09);
  border-radius: 10px;
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
