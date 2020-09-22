<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="10">
        <v-img
          class="campaign-header-img"
          height="200px"
          src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
        >
          <div class="campaign-header-content">
            <p class="mb-0">{{campaign_info.title}}</p>
            <p class="mb-0">{{campaign_info.date}}</p>
          </div>
        </v-img>
        <div class="tab-wrapper">
          <v-tabs v-model="tab" centered grow color="#222" class="campaign-detail-tabs">
            <v-tab v-for="item in items" :key="item" class="campaign-detail-tab">
              <span :class="[$vuetify.breakpoint.smAndDown ? 'text-caption': 'text-h6']">{{ item }}</span>
            </v-tab>
          </v-tabs>
          <v-tabs-items v-model="tab">
            <v-tab-item v-for="item in items" :key="item"></v-tab-item>
          </v-tabs-items>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      campaign_info: {
        title: "캠페인 제목",
        date: "2019-11-12",
      },
      items: ["소개", "인증"],
    };
  },
};
</script>

<style scoped>
.campaign-header-img {
  position: relative;
}

.campaign-header-content {
  position: absolute;
  color: white;
  left: 0;
  right: 0;
  top: 90px;
}

.tab-wrapper {
  position: relative;
}

.campaign-detail-tabs {
  position: absolute;
  top: -50px;
}

.campaign-detail-tab {
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
}
</style>