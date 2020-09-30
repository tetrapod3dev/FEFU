<template>
  <div>
    <!-- hero start -->
    <core-hero
      subtitle="우리 함께 지구를 구해요"
      :mainimage="require('@/assets/illust/hero-title.svg')"
      backimage="https://cdn.imweb.me/upload/S20200610f999ac5b4f199/be7483f8a30b9.gif"
    >
      <template slot="footer">
        <v-row align="end">
          <v-col align="center">
            <v-img
              style="cursor: pointer"
              width="40"
              height="40"
              contain
              @click="$vuetify.goTo('#section-theproblem')"
              :src="require('@/assets/illust/arrow-down.svg')"
            />
          </v-col>
        </v-row>
      </template>
    </core-hero>
    <!-- hero end -->

    <!-- section the problem start -->
    <core-section subtitle="THE PROBLEM" min-height="100vh">
      <template slot="title">
        지나친 개발로 인한
        <br />
        <span class="c-highlight">엄청난 환경 오염 문제</span>
      </template>
      <template slot="text">
        환경 문제에 대해 위기 의식은 공유하지만, 환경 친화와 이해 관계는 함께 할
        수 없어 자신의 이익을 위해 환경 파괴에 거리낌이 없는 경우가 대다수
        입니다.
      </template>
    </core-section>
    <!-- section the problem end -->

    <!-- section the solution start -->
    <core-section subtitle="THE SOLUTION" pb="12">
      <template slot="title">
        작은 실천부터 시작하고,
        <br />
        <span class="c-highlight">더 이상 버리지 말고 재사용하자!</span>
      </template>
      <template slot="text">
        쓰레기를 버리는 것만으로도 환경 오염에 영향이 가요.
        <br />불필요한 물건을 다른 사람들과 나눠보면 어떨까요?
      </template>
      <template slot="content">
        <v-col v-for="item in contentSolution" :key="item.src" cols="12" sm="4">
          <card-with-caption
            :caption="item.text"
            :src="require(`@/assets/images/${item.src}`)"
          />
        </v-col>
      </template>
    </core-section>
    <!-- section the solution end -->

    <!-- section campaign start -->
    <core-section
      subtitle="CAMPAIGN"
      :centerPadding="false"
      :endPadding="false"
    >
      <template slot="title">
        <span class="c-highlight">다양한 종류의 캠페인으로</span>
        <br />여러 사람들과 같이 실천해요!
      </template>
      <template slot="text">
        아래 사진들은 다양한 캠페인들을 보여주고 있는 사진이에요.
        <br />어때요? 정말 멋지지 않나요?
      </template>
    </core-section>

    <v-container>
      <v-row>
        <v-col cols="12" sm="4">
          <v-img
            class="c-sheet"
            src="@/assets/campaign/4.png"
            position="50% 30%"
            lazy-src="@/assets/images/lazy-loading.jpg"
          >
            <template v-slot:placeholder>
              <lazy-loading />
            </template>
          </v-img>
        </v-col>
        <v-col cols="12" sm="4" class="pr-3 pb-3">
          <v-img
            class="c-sheet"
            src="@/assets/campaign/5.png"
            position="50% 13%"
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
        </v-col>
        <v-col cols="12" sm="4" class="pr-3 pb-3">
          <v-img
            class="c-sheet"
            src="@/assets/campaign/6.png"
            position="50% 10%"
            lazy-src="@/assets/images/lazy-loading.jpg"
          >
            <template v-slot:placeholder>
              <lazy-loading />
            </template>
          </v-img>
        </v-col>

        <v-col cols="12" class="py-12">
          <router-link
            tag="button"
            :to="{ name: 'CampaignMain' }"
            class="c-btn c-primary"
          >
            더보기
          </router-link>
        </v-col>
      </v-row>
    </v-container>
    <!-- section campaign end -->

    <!-- section secondhand start -->
    <core-section subtitle="SECONDHAND" pb="12">
      <template slot="title">
        <span class="c-highlight">재활용보다 재사용이</span>
        <br />환경을 더욱 보호하는 길이예요
      </template>
      <template slot="text">
        전 세계에서 매년 최소 800만 톤의 플라스틱이 바다로 유출되지만 재활용되는
        양은 전체의 단 7%에 불과합니다. 재활용보단 재사용을 하세요.
      </template>
      <template>
        <v-col cols="12">
          <router-link
            tag="a"
            :to="{ name: 'MarketMainView' }"
            class="c-btn--text"
            :class="'c-btn--text-' + $vuetify.breakpoint.name"
          >
            중고마켓 둘러보러 가기
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
      </template>
    </core-section>
    <v-row
      align="center"
      class="mx-auto"
      justify="center"
      style="position: relative"
    >
      <v-img src="@/assets/illust/wave-line.svg" />
      <v-overlay :absolute="true" opacity="0">
        <v-container fill-height>
          <v-col>
            <v-img
              max-height="260"
              contain
              :src="require('@/assets/images/ecobag.png')"
            />
          </v-col>
        </v-container>
      </v-overlay>
    </v-row>
    <!-- section secondhand end -->

    <v-col class="py-12 c-primary" style="margin: -1px 0px -1px 0px"></v-col>
    <v-col class="py-12 c-primary" style="margin: -1px 0px -1px 0px"></v-col>

    <!-- section group start -->
    <core-section
      class="c-primary"
      pb="12"
      :centerPadding="false"
      :endPadding="false"
    >
      <template slot="title">
        다양한 환경 단체를
        <br />살펴보세요!
      </template>
    </core-section>
    <section class="c-primary">
      <v-container>
        <v-row justify="center">
          <v-col cols="12" xl="8"
            ><v-row>
              <v-col v-for="index in 6" :key="index" cols="12" sm="6" md="4">
                <v-img
                  :src="require('@/assets/images/logo' + index + '.jpg')"
                  style="
                    height: 80px;
                    width: 100%;
                    border: 2px solid #000000;
                    border-radius: 5px;
                    background-color: #ffffff;
                  "
                  lazy-src="@/assets/images/lazy-loading.jpg"
                >
                  <template v-slot:placeholder>
                    <lazy-loading />
                  </template>
                </v-img>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-container>
    </section>
    <!-- section group end -->
  </div>
</template>

<script>
import CoreHero from "@/components/core/Hero";
import CoreSection from "@/components/core/Section";
import CardWithCaption from "@/components/home/CardWithCaption";

export default {
  name: "Home",
  data() {
    return {
      contentSolution: [
        { text: "캠페인", src: "main-info-campaign.jpg" },
        { text: "중고거래", src: "main-info-market.jpg" },
        { text: "에코포인트", src: "main-info-point.jpg" },
      ],
    };
  },
  components: {
    CoreHero,
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

.c-sheet {
  border: 2px solid black;
  border-radius: 5px;
  width: 100%;
  height: 290px;
}

.c-btn {
  border: 2px solid black;
  border-radius: 5px;
  padding: 10px 20px !important;
  background-color: var(--white-color);
  top: 0px;
  font-family: "S-CoreDream-7ExtraBold";
  letter-spacing: 0px;
  transition: 0.3s;

  &:hover {
    box-shadow: 2px 2px 0px 0px rgba(0, 0, 0, 1);
    transform: translate3d(0px, -5px, -5px);
    transition: 0.3s;
    cursor: pointer;
  }
  &:focus {
    outline: 0;
  }
}

.c-primary {
  background-color: var(--primary-color);
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
