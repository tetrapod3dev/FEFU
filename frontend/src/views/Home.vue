<template>
  <div class="home">
    <section id="hero">
      <v-container
        :style="'min-height: calc(100vh - ' + $vuetify.application.top + 'px)'"
        fill-height
      >
        <v-row></v-row>
        <v-row align="center" class="mx-auto" justify="center" style="position: relative;">
          <v-img src="https://cdn.imweb.me/upload/S20200610f999ac5b4f199/be7483f8a30b9.gif" />
          <v-overlay :absolute="true" opacity="0">
            <v-container fill-height>
              <v-col
                class="black--text custom-text"
                :class="'custom-text-'+$vuetify.breakpoint.name"
                cols="12"
              >우리 함께 지구를 구해요</v-col>
              <v-col>
                <v-img max-height="260" contain :src="require('@/assets/illust/hero-title.svg')" />
              </v-col>
            </v-container>
          </v-overlay>
        </v-row>
        <v-row align="end">
          <v-col align="center">
            <v-img
              style="cursor: pointer"
              width="40"
              height="40"
              contain
              @click="$vuetify.goTo('#the-problem')"
              :src="require('@/assets/illust/arrow-down.svg')"
            />
          </v-col>
        </v-row>
      </v-container>
    </section>

    <section id="the-problem">
      <div class="py-12"></div>

      <v-container class="text-center">
        <v-row>
          <v-col
            class="black--text custom-subtitle"
            :class="'custom-subtitle-'+$vuetify.breakpoint.name"
            cols="12"
          >THE PROBLEM</v-col>
          <v-col cols="12">
            <h2 class="custom-title mb-3" :class="'custom-title-'+$vuetify.breakpoint.name">
              현 시점에서 인류의 존망을
              <br />크게 위협하는 문제
            </h2>
          </v-col>
          <v-col>
            <v-responsive class="mx-auto mb-8" width="56"></v-responsive>
            <v-responsive class="mx-auto title font-weight-light mb-8" max-width="720">
              <p>
                환경 문제에 대해 위기 의식은 공유하지만, 환경 친화와 이해 관계는 함께 할 수 없어
                자신의 이익을 위해 환경 파괴에 거리낌이 없는 경우가 대다수 입니다.
              </p>
            </v-responsive>
            <v-btn color="grey" href="https://vuetifyjs.com" outlined large>
              <span class="grey--text text--darken-1 font-weight-bold">더 알아보기</span>
            </v-btn>
          </v-col>
        </v-row>

        <div></div>
      </v-container>

      <div class="py-12"></div>
    </section>

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

    <v-sheet id="contact" color="#333333" dark tag="section" tile>
      <div class="py-12"></div>

      <v-container>
        <h2 class="display-2 font-weight-bold mb-3 text-uppercase text-center">우리와 함께하세요</h2>

        <v-responsive class="mx-auto mb-12" width="56">
          <v-divider class="mb-1"></v-divider>

          <v-divider></v-divider>
        </v-responsive>

        <v-row>
          <v-col cols="12">
            <v-text-field flat label="이메일" solo></v-text-field>
          </v-col>

          <v-col class="mx-auto" cols="auto">
            <v-btn color="accent" x-large>Submit</v-btn>
          </v-col>
        </v-row>
      </v-container>

      <div class="py-12"></div>
    </v-sheet>
  </div>
</template>

<script>
export default {
  name: "Home",
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

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Patrick+Hand&family=Nunito:wght@400;600;700;800;900&display=swap");
@font-face {
  font-family: "NanumSquareRound";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_two@1.0/NanumSquareRound.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: "NanumBarunpen";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_two@1.0/NanumBarunpen.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}

.custom-title {
  font-size: 35px;
  letter-spacing: -2px;
  line-height: 1.3;
  font-weight: 700;
  font-family: "Nunito", "NanumBarunpen", sans-serif;
}
.custom-title-md {
  font-size: 52px;
  letter-spacing: -2.5px;
  line-height: 1.2;
}
.custom-title-lg {
  font-size: 64px;
  letter-spacing: -3px;
  line-height: 1.2;
}

.custom-subtitle {
  font-size: 13px;
  font-weight: bold;
  letter-spacing: 4px;
  font-family: "Nunito", "NanumSquareRound", sans-serif;
}
.custom-subtitle-md {
  font-size: 15px;
  font-family: "Nunito", "NanumSquareRound", sans-serif;
}
.custom-subtitle-lg {
  font-size: 16px;
  font-family: "Nunito", "NanumSquareRound", sans-serif;
}

.custom-text {
  font-size: 18px;
  font-family: "Nunito", "NanumSquareRound", sans-serif;
}
.custom-text-md {
  font-size: 20px;
}
.custom-text-lg {
  font-size: 24px;
}
</style>
