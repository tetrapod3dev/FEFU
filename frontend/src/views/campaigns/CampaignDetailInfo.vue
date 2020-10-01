<template>
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
</template>

<script>
import SERVER from "@/api/api";

export default {
  name: "CampaignDetailInfo",
  props: ["campaign", "campaignTypeInfo"],
  created() {},
  data() {
    return {
      //   campaign: {
      //     title: "",
      //     content: "",
      //     writer: "",
      //     startDate: "",
      //     endDate: "",
      //     photo: "",
      //     tag: [],
      //     type: "",
      //     no: 0,
      //   },
      //   campaignTypeInfo: {
      //     authEndTime: "",
      //     authProcess: "",
      //     authStartTime: "",
      //     campaignNo: null,
      //     headcount: null,
      //     mission: "",
      //     no: null,
      //     requirement: null,
      //   },
    };
  },
  methods: {
    imageSrc(filename) {
      return SERVER.IMAGE_URL + filename;
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
  min-height: 440px;
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
</style>
