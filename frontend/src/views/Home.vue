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
      <template slot="content">
        <v-col class="ml-auto mr-auto" cols="8" md="4">
          <v-img src="@/assets/images/ecobag.png" />
        </v-col>
      </template>
    </core-section>

    <section id="features" class="grey lighten-3">
      <div class="py-12"></div>

      <v-container class="text-center">
        <h2 class="display-2 font-weight-bold mb-3">캠페인 - 중고거래 - 포인트</h2>

        <v-responsive class="mx-auto mb-12" width="56">
          <v-divider class="mb-1"></v-divider>

          <v-divider></v-divider>
        </v-responsive>
        <v-row justify="center">
          <v-col cols="12" xl="6">
            <v-carousel cycle height="400" hide-delimiter-background show-arrows-on-hover>
              <v-carousel-item v-for="({ title, text }, i) in features" :key="i">
                <v-sheet height="100%">
                  <h4>{{ title }}</h4>
                  <v-row class="fill-height" align="center" justify="center">
                    <div class="display-5">{{ text }}</div>
                  </v-row>
                </v-sheet>
              </v-carousel-item>
            </v-carousel>
          </v-col>
        </v-row>
      </v-container>

      <div class="py-12"></div>
    </section>

    <section id="stats">
      <v-parallax
        :height="$vuetify.breakpoint.smAndDown ? 700 : 500"
        src="https://www.mallgalleries.org.uk/sites/default/files/Brown-Peter-Early-Morning-The-Market-Hoi-An-Vietnam.jpg"
      >
        <v-container fill-height>
          <v-row class="mx-auto" justify="center">
            <v-col cols="12" md="8">
              <v-sheet height="100%">
                <div class="py-6"></div>
                <h2 class="display-2 font-weight-bold mb-3">중고거래</h2>

                <v-responsive class="mx-auto mb-8" width="56">
                  <v-divider class="mb-1"></v-divider>

                  <v-divider></v-divider>
                </v-responsive>
                <v-responsive class="mx-auto title font-weight-light mb-8" max-width="720">
                  <p>의외로 플라스틱은 재활용률이 낮아 환경을 위협하고 있습니다.</p>
                  <p>재활용보단 재사용이 지구를 생각하는 길입니다.</p>
                </v-responsive>
                <v-btn color="grey" href="https://vuetifyjs.com" outlined large>
                  <span class="grey--text text--darken-1 font-weight-bold">더 알아보기</span>
                </v-btn>
                <div class="py-6"></div>
              </v-sheet>
            </v-col>
          </v-row>
        </v-container>
      </v-parallax>
    </section>

    <section id="blog">
      <div class="py-12"></div>

      <v-container>
        <h2 class="display-2 font-weight-bold mb-3 text-uppercase text-center">환경단체</h2>

        <v-responsive class="mx-auto mb-12" width="56">
          <v-divider class="mb-1"></v-divider>

          <v-divider></v-divider>
        </v-responsive>

        <v-row>
          <v-col v-for="i in 12" :key="i" cols="12" sm="6" md="4">
            <h3 class="font-weight-black mb-4 text-uppercase" v-text="i + ' 환경단체'"></h3>
          </v-col>
        </v-row>
      </v-container>

      <div class="py-12"></div>
    </section>
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
    return {
      articles: [
        {
          src:
            "https://images.unsplash.com/photo-1423784346385-c1d4dac9893a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80",
          title: "Mobile first & Responsive",
          text:
            "Phasellus lorem enim, luctus ut velit eget, convallis egestas eros. Sed ornare ligula eget tortor tempor, quis porta tellus dictum.",
        },
        {
          src:
            "https://images.unsplash.com/photo-1475938476802-32a7e851dad1?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80",
          title: "Think outside the box",
          text:
            "Nam ut leo ipsum. Maecenas pretium aliquam feugiat. Aenean vel tempor est, vitae tincidunt risus. Sed sodales vestibulum nibh.",
        },
        {
          src:
            "https://images.unsplash.com/photo-1416339442236-8ceb164046f8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1892&q=80",
          title: "Small changes, big difference",
          text:
            "Vestibulum in dictum velit, in rhoncus nibh. Maecenas neque libero, interdum a dignissim in, aliquet vitae lectus. Phasellus lorem enim, luctus ut velit eget.",
        },
      ],
      features: [
        {
          title: "캠페인",
          text:
            "캠페인은 다양한 형태의 환경보호를 지속적으로 실천할 수 있게 해줍니다.",
        },
        {
          title: "중고마켓",
          text:
            "중고 거래는 통해 재사용을 하여 자원 소비와 쓰레기 발생을 낮추는데 목표를 두고 있습니다.",
        },
        {
          title: "에코포인트",
          text:
            "캠페인 등으로 벌게 되는 에코 포인트를 중고 거래나 환경 단체에 사용함으로써 환경 보호에 선순환을 유도합니다.",
        },
      ],
      stats: [
        ["24k", "Github Stars"],
        ["330+", "Releases"],
        ["1m", "Downloads/mo"],
        ["5m", "Total Downloads"],
      ],
    };
  },
};
</script>

<style lang="scss" scoped>
.custom-highlight {
  background: url("~@/assets/illust/one-line-highlight.svg") no-repeat center;
  background-size: 100%;
}

// .custom-title {
//   font-size: 35px;
//   letter-spacing: -2px;
//   line-height: 1.3;
//   font-weight: 700;
//   font-family: "Nunito", "NanumBarunpen", sans-serif;

//   &-md {
//     font-size: 52px;
//     letter-spacing: -2.5px;
//     line-height: 1.2;
//   }
//   &-lg {
//     font-size: 64px;
//     letter-spacing: -3px;
//     line-height: 1.2;
//   }
// }

// .custom-subtitle {
//   font-size: 13px;
//   font-weight: bold;
//   letter-spacing: 4px;
//   font-family: "Nunito", "NanumSquareRound", sans-serif;

//   &-md {
//     font-size: 15px;
//   }
//   &-lg {
//     font-size: 16px;
//   }
// }

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
  &-lg {
    font-size: 18px;
    line-height: 1.5;
  }
}

.custom-text-button-icon {
  display: inline-block;
}
</style>
