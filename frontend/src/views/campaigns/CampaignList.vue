<template>
  <div>
    <!-- 헤더 캐로젤 -->
    <div>
      <v-carousel cycle height="400" hide-delimiter-background show-arrows-on-hover>
        <v-carousel-item v-for="(slide, i) in slides" :key="i" :src="slide.src">
          <v-row class="fill-height" justify="start" align="center">
            <v-col>
              <div class="d-flex flex-column mb-5">
                <span class="display-1">{{ slide.title }}</span>
                <span class="body-2 mt-3">{{ slide.content }}</span>
              </div>
            </v-col>
          </v-row>
        </v-carousel-item>
      </v-carousel>
    </div>

    <!-- 탭 -->
    <v-container>
      <!-- <v-container :class="[$vuetify.breakpoint.smAndDown ? '': 'mt-5']"> -->
      <v-tabs v-model="tab" centered grow color="#222">
        <v-tabs-slider color="#222"></v-tabs-slider>
        <v-tab v-for="item in items" :key="item" class="ml-0">
          <span :class="[$vuetify.breakpoint.smAndDown ? 'text-caption': 'text-h6']">{{ item }}</span>
        </v-tab>
      </v-tabs>
      <v-tabs-items v-model="tab">
        <v-tab-item v-for="item in items" :key="item">
          <LongTermList v-if="item=='100일 캠페인'" />
          <ShortTermList v-if="item=='상시 캠페인'" />
          <DailyQuest v-if="item=='일일 퀘스트'" />
        </v-tab-item>
      </v-tabs-items>
      <!-- </v-container> -->
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
      slides: [
        {
          title: "100일 캠페인",
          content:
            "뜻을 함께하는 사람들과 함께, 100일 동안 함께하며 지구를 살리는 습관 만들기.",
          src: require("@/assets/images/nature-3.jpg"),
        },
        {
          title: "상시 캠페인",
          content:
            "오늘 당장 시작할 수 있는 기업캠페인과 공식 캠페인, 오늘 지구를 살리기 위한 당신의 실천은 무엇인가요?",
          src: require("@/assets/images/bg3.jpg"),
        },
        {
          title: "일일퀘스트",
          content:
            "일상 생활 속에서 쉽게 실천할 수 있는 12가지의 환경보호 생활 방안들, 지구를 살리는 한발자국",
          src: require("@/assets/images/bg7.jpg"),
        },
      ],
      tab: null,
      items: ["100일 캠페인", "상시 캠페인", "일일 퀘스트"],
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
