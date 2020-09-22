<template>
  <div class="home">
    <core-hero>
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

    <core-section
      id="section-theproblem"
      subtitle="THE PROBLEM"
      text="환경 문제에 대해 위기 의식은 공유하지만, 환경 친화와 이해 관계는 함께 할 수 없어 자신의 이익을 위해 환경 파괴에 거리낌이 없는 경우가 대다수 입니다."
      min-height="100vh"
    >
      <template slot="title">
        현 시점에서 인류의 존망을
        <br />
        <span class="custom-highlight">크게 위협하는 문제</span>
      </template>
      <template slot="text">
        환경 문제에 대해 위기 의식은 공유하지만, 환경 친화와 이해 관계는 함께 할 수
        없어 자신의 이익을 위해 환경 파괴에 거리낌이 없는 경우가 대다수 입니다.
      </template>
    </core-section>

    <core-section id="section-thesolution" subtitle="THE SOLUTION" pb="12">
      <template slot="title">
        작은 실천부터 시작하고,
        <br />
        <span class="custom-highlight">더 이상 버리지 말고 재사용하자!</span>
      </template>
      <template slot="text">
        쓰레기를 버리는 것만으로도 환경 오염에 영향이 가요.
        <br />불필요한 물건을 다른 사람들과 나눠보면 어떨까요?
      </template>
      <template slot="content">
        <v-col cols="12" sm="4">
          <card-with-caption
            caption="캠페인"
            :src="require('@/assets/images/main-info-campaign.jpg')"
          />
        </v-col>
        <v-col cols="12" sm="4">
          <card-with-caption caption="중고거래" :src="require('@/assets/images/main-info-market.jpg')" />
        </v-col>
        <v-col cols="12" sm="4">
          <card-with-caption caption="에코포인트" :src="require('@/assets/images/main-info-point.jpg')" />
        </v-col>
      </template>
    </core-section>

    <core-section id="section-campaign" subtitle="CAMPAIGN">
      <template slot="title">
        <span class="custom-highlight">다양한 종류의 캠페인으로</span>
        <br />여러 사람들과 같이 실천해요!
      </template>
      <template slot="text">
        아래 사진들은 다양한 캠페인들을 보여주고 있는 사진이에요.
        <br />어때요? 정말 멋지지 않나요?
      </template>
      <template slot="content">
        <v-col cols="12" sm="4" class="pr-3 pb-3">
          <v-img class="custom-img" src="@/assets/images/main-info-campaign.jpg" />
        </v-col>
        <v-col cols="12" sm="4" class="pr-3 pb-3">
          <v-img class="custom-img" src="@/assets/images/main-info-market.jpg" />
        </v-col>
        <v-col cols="12" sm="4" class="pr-3 pb-3">
          <v-img class="custom-img" src="@/assets/images/main-info-point.jpg" />
        </v-col>
        <v-col cols="12" sm="4" class="pr-3 pb-3">
          <v-img class="custom-img" src="@/assets/images/main-info-campaign.jpg" />
        </v-col>
        <v-col cols="12" sm="4" class="pr-3 pb-3">
          <v-img class="custom-img" src="@/assets/images/main-info-market.jpg" />
        </v-col>
        <v-col cols="12" sm="4" class="pr-3 pb-3">
          <v-img class="custom-img" src="@/assets/images/main-info-point.jpg" />
        </v-col>
        <v-col cols="12" sm="4" class="pr-3 pb-3">
          <v-img class="custom-img" src="@/assets/images/main-info-campaign.jpg" />
        </v-col>
        <v-col cols="12" sm="4" class="pr-3 pb-3">
          <v-img class="custom-img" src="@/assets/images/main-info-market.jpg" />
        </v-col>
        <v-col cols="12" sm="4" class="pr-3 pb-3">
          <v-img class="custom-img" src="@/assets/images/main-info-point.jpg" />
        </v-col>
        <v-col cols="12" class="py-12">
          <router-link
            tag="button"
            :to="{name: 'CampaignList'}"
            class="custom-button custom-primary"
          >더보기</router-link>
        </v-col>
      </template>
    </core-section>

    <core-section id="section-secondhand" subtitle="SECONDHAND" pb="12">
      <template slot="title">
        <span class="custom-highlight">재활용보다 재사용이</span>
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
            :to="{name: 'MarketMainView'}"
            class="custom-text-button"
            :class="'custom-text-button-'+$vuetify.breakpoint.name"
          >
            더보기
            <v-img
              style="cursor: pointer; margin-top: 3px"
              :width="$vuetify.breakpoint.smAndDown ? 15 : 17"
              :height="$vuetify.breakpoint.smAndDown ? 15 : 17"
              class="custom-text-button-icon"
              contain
              :src="require('@/assets/illust/arrow-right.svg')"
            />
          </router-link>
        </v-col>
      </template>
    </core-section>
    <v-row align="center" class="mx-auto" justify="center" style="position: relative;">
      <v-img src="@/assets/illust/wave-line.svg" />
      <v-overlay :absolute="true" opacity="0">
        <v-container fill-height>
          <v-col>
            <v-img max-height="260" contain :src="require('@/assets/images/ecobag.png')" />
          </v-col>
        </v-container>
      </v-overlay>
    </v-row>
    <v-col class="py-12 custom-primary" style="margin: -1px -1px"></v-col>
    <v-col class="py-12 custom-primary" style="margin: -1px -1px"></v-col>

    <core-section id="section-group" class="custom-primary" pb="12">
      <template slot="title">
        다양한 환경 단체를
        <br />살펴보세요!
      </template>
      <template slot="content">
        <v-col v-for="i in 6" :key="i" cols="12" sm="6" md="4">
          <h3
            style="border: 2px solid #000000; border-radius: 5px;padding: 10px 20px; background-color: #ffffff"
            class="font-weight-black mb-4 text-uppercase"
            v-text="i + ' 환경단체'"
          ></h3>
        </v-col>
      </template>
    </core-section>
  </div>
</template>

<script>
import CoreHero from "@/components/core/Hero";
import CoreSection from "@/components/core/Section";
import CardWithCaption from "@/components/home/CardWithCaption";

export default {
  name: "Home",
  components: {
    CoreHero,
    CoreSection,
    CardWithCaption,
  },
  data() {
    return {};
  },
};
</script>

<style lang="scss" scoped>
.custom-highlight {
  background: url("~@/assets/illust/one-line-highlight.svg") no-repeat center;
  background-size: 100%;
}

.custom-img {
  border: 2px solid black;
  border-radius: 5px;
  width: 100%;
  height: 260px;
}

.custom-img-group {
  padding: 6px;

  .custom-img-caption {
    position: relative;
    display: inline-block;
    border: 2px solid black;
    border-radius: 5px;
    padding: 15px 20px;
    background-color: #ffffff;
    min-width: 120px;
    font-family: "S-CoreDream-7ExtraBold";
    transition: 0.3s;
    z-index: 2;
  }
  .custom-img {
    position: relative;
    margin-top: -45px;
    overflow: hidden;
    z-index: 1;
  }
}

.custom-button {
  border: 2px solid black;
  border-radius: 5px;
  padding: 10px 20px !important;
  background-color: #ffffff;
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

.custom-primary {
  background-color: var(--primary-color);
}

.custom-text-button {
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

.custom-text-button-icon {
  display: inline-block;
}
</style>
