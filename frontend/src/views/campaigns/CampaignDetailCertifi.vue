<template>
  <div class="campaign-info">
    <!-- bar chart start -->
    <bar-chart
      v-if="campaign.type == 'official'"
      :data="dataList"
      :labels="labelList"
    />
    <!-- bar chart end -->

    <!-- user certificate start -->
    <v-container v-if="campaign.type == 'personal'" class="my-7">
      <h2 class="text-left">멤버별 인증현황 ({{ userList.length }}명)</h2>
      <v-row v-for="(user, index) in userList" :key="index">
        <v-col cols="3" sm="2" md="1">
          <v-avatar color="teal">
            <img
              :src="
                !!user.profile_image
                  ? imageSrc(user.profile_image)
                  : require(`@/assets/images/${'남자'}.png`)
              "
            />
          </v-avatar>
        </v-col>
        <v-col cols="9" sm="10" md="11">
          <div class="d-flex pa-0">
            <span class="mr-auto mb-0">
              {{ user.writer }}
            </span>
            <span class="ml-auto mb-0">{{ user.count }}일</span>
          </div>
          <v-progress-linear
            v-model="user.count"
            color="teal lighten-1"
            height="15"
          ></v-progress-linear>
        </v-col>
      </v-row>
    </v-container>
    <!-- user certificate end -->
  </div>
</template>

<script>
import BarChart from "@/components/campaign/BarChart.vue";
import { mixinGetUserInfo } from "@/components/mixin/mixinGetUserInfo";

import { mapGetters } from "vuex";
import axios from "axios";
import SERVER from "@/api/api";

export default {
  name: "CampaignDetailCertifi",
  props: ["campaign", "campaignTypeInfo"],
  mixins: [mixinGetUserInfo],
  data() {
    return {
      userList: [],
      dataList: {},
      labelList: ["일", "월", "화", "수", "목", "금", "토"],
    };
  },
  components: {
    BarChart,
  },
  created() {
    if (this.campaign.type == "personal") {
      this.getPersonalPercentTeam();
    }
    if (this.campaign.type == "official") {
      for (let i = 1; i < 8; i++) {
        this.dataList[this.parseDate(this.addDays(new Date(), -i))] = 0;
      }
      // console.log(this.dataList);
      this.getOfficialPercentWeek();
      console.log(this.dataList);
    }
  },
  computed: {
    ...mapGetters("accounts", ["config"]),
  },
  methods: {
    parseDate(date) {
      return date.toISOString().substr(0, 10);
    },
    addDays(date, days) {
      const copy = new Date(Number(date));
      copy.setDate(date.getDate() + days);
      return copy;
    },
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
          this.userList = res.data;
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getOfficialPercentWeek() {
      axios
        .get(
          SERVER.URL +
            SERVER.ROUTES.campaigns.officialPercentWeek +
            "/" +
            this.$route.params.campaignNo
        )
        .then((res) => {
          res.data.forEach((element) => {
            this.dataList[element.time] = element.count;
          });

          // console.log(Object.keys(this.dataList));
          // console.log(Object.values(this.dataList).reverse());
          // console.log(
          //   Object.keys(this.dataList).map((e) => {
          //     return this.dataList[e];
          //   })
          // );
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

.campaign-info {
  font-family: "NanumBarunpen";
  border: 2px solid black;
  border-radius: 5px;
  padding: 10px 20px;
  margin: 10px 0;
  min-height: 440px;
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
