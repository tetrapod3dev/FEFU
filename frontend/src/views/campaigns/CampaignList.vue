<template>
  <div>
    <!-- 헤더 캐로젤 -->
    <div>
      <h2>운영자 추천 캠페인</h2>
      <v-carousel cycle height="400" hide-delimiter-background show-arrows-on-hover>
        <v-carousel-item v-for="(slide, i) in slides" :key="i">
          <v-sheet :color="colors[i]" height="100%">
            <v-row class="fill-height" align="center" justify="center">
              <div class="display-3">{{ slide }} Slide</div>
            </v-row>
          </v-sheet>
        </v-carousel-item>
      </v-carousel>
    </div>

    <!-- 탭 -->
    <v-container class="mt-5">
      <v-tabs v-model="tab" align-with-title fixed-tabs color="indigo">
        <v-tabs-slider color="indigo"></v-tabs-slider>
        <v-tab v-for="item in items" :key="item">
          <h2>{{ item }}</h2>
        </v-tab>
      </v-tabs>
      <v-tabs-items v-model="tab">
        <v-tab-item v-for="item in items" :key="item">
          <LongTermList v-if="item=='100일 캠페인'" />
          <ShortTermList v-if="item=='상시 캠페인'" />
          <DailyQuest v-if="item=='일일 퀘스트'" />
        </v-tab-item>
      </v-tabs-items>
    </v-container>
  </div>
</template>

<script>
import LongTermList from "./LongTermList.vue";
import ShortTermList from "./ShortTermList.vue";
import DailyQuest from "./DailyQuest.vue";

export default {
  components: {
    LongTermList,
    ShortTermList,
    DailyQuest,
  },
  data() {
    return {
      colors: ["indigo", "warning", "pink darken-2"],
      slides: ["First", "Second", "Third"],
      tab: null,
      items: ["100일 캠페인", "상시 캠페인", "일일 퀘스트"],
      text:
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    };
  },
  methods: {},
};
</script>

<style scoped>
h2 {
  margin-top: 20px;
  margin-bottom: 20px;
}
</style>
