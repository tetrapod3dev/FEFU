<template>
  <div class="home">
    <section id="hero">
      <v-row no-gutters>
        <v-img
          :min-height="'calc(100vh - ' + $vuetify.application.top + 'px)'"
          src="https://www.netclipart.com/pp/m/389-3896024_transparent-save-earth-png-famous-people-born-in.png"
        >
          <v-theme-provider dark>
            <v-container fill-height>
              <v-row align="center" class="black--text mx-auto" justify="center">
                <v-col class="black--text text-center" cols="12" tag="h1">
                  <span
                    :class="[$vuetify.breakpoint.smAndDown ? 'display-3': 'display-4']"
                    class="font-weight-black"
                  >SAVE THE EARTH</span>
                </v-col>
              </v-row>
              <v-row align="end">
                <v-col align-self="center">
                  <v-btn class="black" fab outlined @click="$vuetify.goTo('#about-me')">
                    <v-icon>mdi-chevron-double-down</v-icon>
                  </v-btn>
                </v-col>
              </v-row>
            </v-container>
          </v-theme-provider>
        </v-img>
      </v-row>
    </section>

    <section id="about-me">
      <div class="py-12"></div>

      <v-container class="text-center">
        <v-row>
          <v-col cols="12" md="8">
            <h2 class="display-2 font-weight-bold mb-3">왜 캠페인과 중고거래인가?</h2>

            <v-responsive class="mx-auto mb-8" width="56">
              <v-divider class="mb-1"></v-divider>

              <v-divider></v-divider>
            </v-responsive>
            <v-responsive class="mx-auto title font-weight-light mb-8" max-width="720">
              <p>환경보호는 의외로 실천하기에는 막막합니다.</p>
              <p>지구 온난화로 인해 지구가 아파하고 있는것은 누구나 알고 있습니다.</p>
              <p>지구와 사람은 뗄 수 없는 사이입니다.</p>
              <p>지구 용사가 되어 지구를 지켜보세요.</p>
            </v-responsive>
            <v-btn color="grey" href="https://vuetifyjs.com" outlined large>
              <span class="grey--text text--darken-1 font-weight-bold">더 알아보기</span>
            </v-btn>
          </v-col>
          <v-col cols="12" md="4">
            <v-img
              src="https://cindybriggs.com/wp-content/uploads/2019/12/7-Unique-Watercolor-Painting-Ideas-for-Beginners-1.jpg"
            ></v-img>
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

        <v-theme-provider light>
          <v-row>
            <v-col cols="12">
              <v-text-field flat label="이메일" solo></v-text-field>
            </v-col>

            <v-col class="mx-auto" cols="auto">
              <v-btn color="accent" x-large>Submit</v-btn>
            </v-col>
          </v-row>
        </v-theme-provider>
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
@import url("https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap");

.display-3 {
  font-family: "Patrick Hand", cursive !important;
}
.display-4 {
  font-family: "Patrick Hand", cursive !important;
}
</style>
