<template>
  <div class="about">
    <section id="section-hero">
      <img
        id="about-hero"
        ref="abouthero"
        :style="resizeHeroWithBreakpoint()"
        src="@/assets/images/about-hero.jpg"
      />
      <v-container
        :style="'min-height: calc(80vh - ' + $vuetify.application.top + 'px)'"
        fill-height
      ></v-container>
    </section>
    <v-row align="center" class="mx-auto" justify="center" style="position: relative">
      <v-img src="@/assets/illust/wave-line-white.svg" />
      <v-overlay :absolute="true" opacity="0" z-index="4">
        <v-container fill-height>
          <v-col>
            <v-img
              :width="titleWidth"
              min-width="260px"
              contain
              :src="require('@/assets/illust/about-us.svg')"
            />
          </v-col>
        </v-container>
      </v-overlay>
    </v-row>

    <v-col class="py-12 custom-white" style="position: relative;margin: -1px 0 -1px 0"></v-col>
    <v-col class="py-12 custom-white" style="position: relative;margin: -1px 0 -1px 0">
      <h1 class="about-title">TEAM. AMONG EARTH</h1>
    </v-col>

    <core-section id="about-us" :centerPadding="false" :endPadding="false">
      <template slot="title">
        환경 보호에 관심을 가진
        <br />
        <span class="custom-highlight">여러분과 만나 기뻐요.</span>
      </template>
      <template slot="text">
        환경 보호가 중요하다는 것은 알고 있지만 실천하기에는 정말 힘든 일이죠.
        <br />당신이 환경 보호에 관심을 가지게 되었다면 우린 성공한거예요.
        <br />작은 실천이 하나의 문화적 도구가 되어서 많은 사람들이 함께하기를 바래요.
        <br />
      </template>
      <template slot="content"></template>
    </core-section>
    <v-container>
      <v-row justify="space-around">
        <v-col cols="6" sm="4" md="3" lg="2">
          <card-with-caption
            height="220px"
            caption="권경은"
            :src="require('@/assets/images/권경은.png')"
          />
        </v-col>
        <v-col cols="6" sm="4" md="3" lg="2">
          <card-with-caption
            height="220px"
            caption="김현수"
            :src="require('@/assets/images/김현수.jpg')"
          />
        </v-col>
        <v-col cols="6" sm="4" md="3" lg="2">
          <card-with-caption
            height="220px"
            caption="박지윤"
            :src="require('@/assets/images/박지윤.jpg')"
          />
        </v-col>
        <v-col cols="6" sm="4" md="3" lg="2">
          <card-with-caption
            height="220px"
            caption="박태록"
            :src="require('@/assets/images/박태록.jpg')"
          />
        </v-col>
        <v-col cols="6" sm="4" md="3" lg="2">
          <card-with-caption
            height="220px"
            caption="이동혁"
            :src="require('@/assets/images/이동혁.png')"
          />
        </v-col>
      </v-row>
      <v-row align="center">
        <v-col cols="12" class="py-8"></v-col>
        <v-col cols="12">
          <v-responsive class="mb-8"></v-responsive>
          <v-responsive
            class="mx-auto mb-8 custom-text"
            :class="'custom-text-'+$vuetify.breakpoint.name"
            max-width="650"
          >
            <p>
              장기 캠페인, 단기 캠페인과 기업에서 진행하는 기업 캠페인 등
              <br />환경 보호를 위한 다양한 형태의 캠페인을 안내해요.
              <br />친환경 활동은 대부분 이익 활동에 반하지만
              <br />중고거래는 물건을 파는 사람은 안 쓰는 물건을 팔고 돈을 벌 수 있고,
              <br />물건을 사는 사람은 원하는 물건을 싼 가격에 구할 수 있죠.
              <br />캠페인을 통해 에코 포인트를 모아 더 싼 가격에 물건을 재사용할 수 있어요.
              <br />
            </p>
          </v-responsive>
        </v-col>
        <v-col cols="12" class="py-8"></v-col>
      </v-row>
      <v-row class="custom-text text-left ml-auto mr-auto py-8 custom-banner">
        For Earth For Us의 일원이 되고 싶지 않나요? 환경 보호를 위해 한번 시작해 보지 않을래요? 그럼 바로 여기예요!
        당장의 한번의 활동도 환경보호에 큰 도움이 된답니다. 얼른 가입해 보세요!
      </v-row>
    </v-container>
  </div>
</template>

<script>
import CoreSection from "@/components/core/Section";
import CardWithCaption from "@/components/home/CardWithCaption";

export default {
  name: "Home",
  components: {
    CoreSection,
    CardWithCaption,
  },

  computed: {
    titleWidth() {
      let resultWidth;
      switch (this.$vuetify.breakpoint.name) {
        case "xs":
          resultWidth = 240;
          break;
        case "sm":
          resultWidth = 300;
          break;
        case "md":
          resultWidth = 360;
          break;
        case "lg":
          resultWidth = 420;
          break;
        case "xl":
          resultWidth = 480;
          break;
      }
      return resultWidth;
    },
  },
  methods: {
    resizeHeroWithBreakpoint() {
      return this.$vuetify.breakpoint.smAndDown
        ? "height: 100vh;margin-left:auto;margin-right:auto;transform: scaleX(-1);"
        : "width: 100%;";
    },
  },
};
</script>

<style lang="scss" scoped>
.custom-highlight {
  background: url("~@/assets/illust/one-line-highlight.svg") no-repeat center;
  background-size: 100%;
}

.custom-white,
#about-us {
  background-color: #fcfcfc;
  z-index: 3;
  position: relative;
}

#about-hero {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 0;
}

#section-hero {
  z-index: 0;
}

.about-title {
  margin-top: 30px;
  font-family: "NanumBarunpen";
}

.custom-text {
  font-size: 16px;
  word-break: keep-all;
  font-weight: bold;
  color: black;
  font-family: "Nunito", "NanumSquareRound", sans-serif;
  max-width: 650px;

  &-md {
    font-size: 18px;
  }
  &-lg,
  &-xl {
    font-size: 20px;
  }
}

.custom-banner {
  border-radius: 5px;
  background-color: var(--primary-color);
  padding: 10px 20px;
  margin: 12px;
}
</style>