<template>
  <div>
    <section id="section-hero">
      <v-img
        style="position: absolute"
        :height="$vuetify.breakpoint.smAndDown ? '50vh' : '100vh'"
        src="@/assets/images/about-hero.jpg"
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
        :height="$vuetify.breakpoint.smAndDown ? '50vh' : '100vh'"
        src="@/assets/illust/aboutus-hero.svg"
      />
    </section>

    <v-col class="py-12" style="position: relative; margin: -1px 0 -1px 0">
      <h1 class="c-title">TEAM. AMONG EARTH</h1>
    </v-col>

    <core-section :centerPadding="false" :endPadding="false">
      <template slot="title">
        환경 보호에 관심을 가진
        <br />
        <span class="c-highlight">여러분과 만나 기뻐요.</span>
      </template>
      <template slot="text">
        환경 보호가 중요하다는 것은 알고 있지만 실천하기에는 정말 힘든 일이죠.
        <br />당신이 환경 보호에 관심을 가지게 되었다면 우린 성공한거예요.
        <br />작은 실천이 하나의 문화적 도구가 되어서 많은 사람들이 함께하기를
        바래요.
        <br />
      </template>
      <template slot="content"></template>
    </core-section>
    <v-container>
      <v-row justify="space-around">
        <v-col
          v-for="item in items"
          :key="item.name"
          cols="6"
          sm="4"
          md="3"
          lg="2"
        >
          <card-with-caption
            height="220px"
            :caption="item.name"
            :src="require(`@/assets/images/${item.src}`)"
          />
        </v-col>
      </v-row>
      <v-row align="center">
        <v-col cols="12" class="py-8"></v-col>
        <v-col cols="12">
          <v-responsive class="mb-8"></v-responsive>
          <v-responsive
            class="mx-auto mb-8 c-txt"
            :class="'c-txt-' + $vuetify.breakpoint.name"
            max-width="650"
          >
            <p>
              장기 캠페인, 단기 캠페인과 기업에서 진행하는 기업 캠페인 등
              <br />환경 보호를 위한 다양한 형태의 캠페인을 안내해요.
              <br />친환경 활동은 대부분 이익 활동에 반하지만 <br />중고거래는
              물건을 파는 사람은 안 쓰는 물건을 팔고 돈을 벌 수 있고,
              <br />물건을 사는 사람은 원하는 물건을 싼 가격에 구할 수 있죠.
              <br />캠페인을 통해 에코 포인트를 모아 더 싼 가격에 물건을
              재사용할 수 있어요.
              <br />
            </p>
          </v-responsive>
        </v-col>
        <v-col cols="12" class="py-8"></v-col>
      </v-row>
    </v-container>

    <v-container>
      <v-row justify="center" align="stretch">
        <v-col
          cols="8"
          md="10"
          class="c-txt text-left px-15 py-6 c-banner ma-0"
          :class="'c-banner-' + $vuetify.breakpoint.name"
        >
          For Earth For Us의 일원이 되고 싶지 않나요? 환경 보호를 위해 한번
          시작해 보지 않을래요? 그럼 바로 여기예요! 당장의 한번의 활동도
          환경보호에 큰 도움이 된답니다. 얼른 가입해 보세요!🚀
        </v-col>
        <v-col
          cols="4"
          md="10"
          class="c-banner ma-0 py-6"
          :class="'c-banner-' + $vuetify.breakpoint.name"
        >
          <router-link
            tag="a"
            :to="{ name: 'SignupView' }"
            class="c-btn--text"
            :class="'c-btn--text-' + $vuetify.breakpoint.name"
          >
            회원가입하러 가기
            <v-img
              style="cursor: pointer; margin-top: 3px"
              :width="$vuetify.breakpoint.smAndDown ? 15 : 17"
              :height="$vuetify.breakpoint.smAndDown ? 15 : 17"
              class="c-btn--text-icon"
              contain
              :src="require('@/assets/illust/arrow-right.svg')"
            />
          </router-link>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import CoreSection from "@/components/core/Section";
import CardWithCaption from "@/components/home/CardWithCaption";

export default {
  name: "Home",
  data() {
    return {
      items: [
        { name: "권경은", src: "권경은.png" },
        { name: "김현수", src: "김현수.jpg" },
        { name: "박지윤", src: "박지윤.jpg" },
        { name: "박태록", src: "박태록.jpg" },
        { name: "이동혁", src: "이동혁.png" },
      ],
    };
  },
  components: {
    CoreSection,
    CardWithCaption,
  },
};
</script>

<style lang="scss" scoped>
.c-highlight {
  background: url("~@/assets/illust/one-line-highlight.svg") no-repeat center;
  background-size: 100%;
}

#section-hero {
  z-index: 3;
}

.c-title {
  margin-top: 30px;
  font-family: "NanumBarunpen";
}

.c-txt {
  font-size: 16px;
  word-break: keep-all;
  font-weight: bold;
  color: black;
  font-family: "Nunito", "NanumSquareRound", sans-serif;

  &-md {
    font-size: 18px;
  }
  &-lg,
  &-xl {
    font-size: 20px;
  }
}

.c-banner {
  border-radius: 5px;
  background-color: var(--primary-color);

  &-xs:first-child,
  &-sm:first-child {
    border-top-right-radius: 0;
    border-bottom-right-radius: 0;
  }

  &-xs:last-child,
  &-sm:last-child {
    border-top-left-radius: 0;
    border-bottom-left-radius: 0;
  }

  &-md:first-child,
  &-lg:first-child,
  &-xl:first-child {
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
  }
  &-md:last-child,
  &-lg:last-child,
  &-xl:last-child {
    border-top-left-radius: 0;
    border-top-right-radius: 0;
  }
}

.c-btn--text {
  display: inline-block;
  text-decoration: none;
  border-bottom: 2px solid #000000;
  padding: 2px 0;
  font-family: "Nunito", "NanumSquareRound", sans-serif;
  font-size: 16px;
  color: #000000;
  transition: 0.3s;

  &-md,
  &-lg,
  &-xl {
    font-size: 18px;
    line-height: 1.5;
  }
}

.c-btn--text-icon {
  display: inline-block;
}
</style>
