<template>
  <div class="campaign-info d-flex flex-column">
    <v-list
      class="campaign-info-list text-left"
      v-if="campaign.type != 'company'"
    >
      <v-row>
        <v-col cols="12" md="2">
          <span class="campaign-info-title">인증 미션</span>
        </v-col>
        <v-col cols="12" md="10">
          <span>{{ campaignTypeInfo.mission }}</span>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="2">
          <span class="campaign-info-title">인증 방법</span>
        </v-col>
        <v-col cols="12" md="10">
          <span>{{ campaignTypeInfo.authProcess }}</span>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="2">
          <span class="campaign-info-title">인증 시간</span>
        </v-col>
        <v-col cols="12" md="10">
          <span>
            {{ campaignTypeInfo.authStartTime }} -
            {{ campaignTypeInfo.authEndTime }}</span
          >
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="2">
          <span class="campaign-info-title">목표 인원</span>
        </v-col>
        <v-col cols="12" md="10">
          <span> {{ campaignTypeInfo.headcount }}명 </span>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="2">
          <span class="campaign-info-title">멤버 조건</span>
        </v-col>
        <v-col cols="12" md="10">
          <span>{{ campaignTypeInfo.requirement }}</span>
        </v-col>
      </v-row>
    </v-list>

    <v-list class="campaign-info-list text-left" v-else>
      <v-row>
        <v-col cols="12" md="3">
          <span class="campaign-info-title">회사명</span>
        </v-col>
        <v-col cols="12" md="9">
          <span>{{ company.companyName }}</span>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="3">
          <span class="campaign-info-title">캠페인링크</span>
        </v-col>
        <v-col cols="12" md="9">
          <span>{{ company.campaignLink }}</span>
        </v-col>
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
  props: ["campaign", "campaignTypeInfo", "company"],
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
  padding: 0 20px;
  background-color: rgba(55, 205, 194, 0.09);
  border-radius: 10px;
  font-family: "NanumBarunpen";
}

.campaign-info-title {
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
