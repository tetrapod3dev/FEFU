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

    <core-section :centerPadding="false" :endPadding="false">
      <template slot="title">
        <span class="c-highlight">ZERO WASTE</span>
        <br />
        5가지 컨셉
      </template>
      <template slot="text">
        쓰레기를 줄이는 생활 습관! Zero Waste 5가지 컨셉을 알아보세요
      </template>
      <template slot="content"></template>
    </core-section>
    <v-container>
      <v-row align="center">
        <v-col cols="12" md="4" class="ml-auto" align="center">
          <v-img
            class="c-sheet"
            :class="'c-sheet-' + $vuetify.breakpoint.name"
            src="@/assets/images/refuse.png"
            lazy-src="@/assets/images/lazy-loading.jpg"
          >
            <template v-slot:placeholder>
              <lazy-loading />
            </template>
          </v-img>
        </v-col>
        <v-col cols="12" md="4" align="center">
          <h2
            class="c-title mb-3"
            :class="'c-title-' + $vuetify.breakpoint.name"
          >
            REFUSE
          </h2>
          <p
            class="mx-auto mb-8 c-txt"
            :class="'c-txt-' + $vuetify.breakpoint.name"
          >
            필요하지 않은 것은 거절하기
          </p>
        </v-col>
      </v-row>
      <v-row align="center">
        <v-col
          cols="12"
          md="4"
          align="center"
          :order="$vuetify.breakpoint.smAndDown ? 2 : 1"
        >
          <h2
            class="c-title mb-3"
            :class="'c-title-' + $vuetify.breakpoint.name"
          >
            REDUCE
          </h2>
          <p
            class="mx-auto mb-8 c-txt"
            :class="'c-txt-' + $vuetify.breakpoint.name"
          >
            필요하며 거절할 수 없는 것은 줄이기
          </p>
        </v-col>
        <v-col
          cols="12"
          md="4"
          class="mr-auto"
          align="center"
          :order="$vuetify.breakpoint.smAndDown ? 1 : 2"
        >
          <v-img
            class="c-sheet"
            :class="'c-sheet-' + $vuetify.breakpoint.name"
            src="@/assets/images/reduce.png"
            lazy-src="@/assets/images/lazy-loading.jpg"
          >
            <template v-slot:placeholder>
              <lazy-loading />
            </template>
          </v-img>
        </v-col>
      </v-row>
      <v-row align="center">
        <v-col cols="12" md="4" class="ml-auto" align="center">
          <v-img
            class="c-sheet"
            :class="'c-sheet-' + $vuetify.breakpoint.name"
            src="@/assets/images/reuse.png"
            lazy-src="@/assets/images/lazy-loading.jpg"
          >
            <template v-slot:placeholder>
              <lazy-loading />
            </template>
          </v-img>
        </v-col>
        <v-col cols="12" md="4" align="center">
          <h2
            class="c-title mb-3"
            :class="'c-title-' + $vuetify.breakpoint.name"
          >
            REUSE
          </h2>
          <p
            class="mx-auto mb-8 c-txt"
            :class="'c-txt-' + $vuetify.breakpoint.name"
          >
            소비하면서 거절하거나 줄일 수 없는 것은 재사용하기
          </p>
        </v-col>
      </v-row>
      <v-row align="center">
        <v-col
          cols="12"
          md="4"
          align="center"
          :order="$vuetify.breakpoint.smAndDown ? 2 : 1"
        >
          <h2
            class="c-title mb-3"
            :class="'c-title-' + $vuetify.breakpoint.name"
          >
            RECYCLE
          </h2>
          <p
            class="mx-auto mb-8 c-txt"
            :class="'c-txt-' + $vuetify.breakpoint.name"
          >
            거절하거나 줄이거나 재사용할 수 없는 것은 재활용하기
          </p>
        </v-col>
        <v-col
          cols="12"
          md="4"
          class="mr-auto"
          align="center"
          :order="$vuetify.breakpoint.smAndDown ? 1 : 2"
        >
          <v-img
            class="c-sheet"
            :class="'c-sheet-' + $vuetify.breakpoint.name"
            src="@/assets/images/recycle.png"
            lazy-src="@/assets/images/lazy-loading.jpg"
          >
            <template v-slot:placeholder>
              <lazy-loading />
            </template>
          </v-img>
        </v-col>
      </v-row>
      <v-row align="center">
        <v-col cols="12" md="4" class="ml-auto" align="center">
          <v-img
            class="c-sheet"
            :class="'c-sheet-' + $vuetify.breakpoint.name"
            src="@/assets/images/rot.png"
            lazy-src="@/assets/images/lazy-loading.jpg"
          >
            <template v-slot:placeholder>
              <lazy-loading />
            </template>
          </v-img>
        </v-col>
        <v-col cols="12" md="4" align="center">
          <h2
            class="c-title mb-3"
            :class="'c-title-' + $vuetify.breakpoint.name"
          >
            ROT
          </h2>
          <p
            class="mx-auto mb-8 c-txt"
            :class="'c-txt-' + $vuetify.breakpoint.name"
          >
            나머지는 썩히기
          </p>
        </v-col>
      </v-row>
    </v-container>
    <v-container>
      <core-banner
        content="For Earth For Us의 일원이 되고 싶지 않나요? 환경 보호를 위해 한번
          시작해 보지 않을래요? 그럼 바로 여기예요! 당장의 한번의 활동도
          환경보호에 큰 도움이 된답니다. 얼른 가입해 보세요!🚀"
        btn-text="회원가입하러 가기"
        :to="{ name: 'SignupView' }"
      />
    </v-container>

    <core-section subtitle="NEWS" :centerPadding="false" :endPadding="false">
      <template slot="title">
        <span class="c-highlight"> 환경 관련 뉴스</span>
      </template>
      <template slot="text"> '환경이슈신문'의 환경 뉴스예요 </template>
      <template slot="content"></template>
    </core-section>
    <v-container>
      <v-row>
        <v-col v-for="i in 6" :key="i" cols="12" sm="6" md="4">
          <v-card class="c-card ma-4">
            <a :href="'//' + news[i - 1].href" target="_blank">
              <v-img
                class="c-news"
                :class="'c-news-' + $vuetify.breakpoint.name"
                style="
                  border: 2px solid #000000;
                  border-top-left-radius: 10px;
                  border-top-right-radius: 10px;
                "
                :src="news[i - 1]"
                lazy-src="@/assets/images/lazy-loading.jpg"
              >
                <template v-slot:placeholder>
                  <lazy-loading />
                </template>
              </v-img>
            </a>
            <v-card-title>
              <a
                style="
                  text-decoration: none;
                  color: #000000;
                  text-overflow: ellipsis;
                  overflow: hidden;
                  white-space: nowrap;
                "
                :href="'//' + news[i - 1].href"
                target="_blank"
                class="text-left"
                >{{ news[i - 1].title }}
              </a>
            </v-card-title>
            <v-card-subtitle class="text-left">
              <a
                style="text-decoration: none; color: #000000"
                :href="'//' + news[i - 1].href"
                target="_blank"
              >
                {{ news[i - 1].writer }} {{ news[i - 1].regtime }}
              </a>
            </v-card-subtitle>
          </v-card>
        </v-col>

        <v-col v-if="!pulsNews" cols="12" class="py-12">
          <v-btn class="c-btn pa-4" text @click="pulsNews = true">
            펼치기
          </v-btn>
        </v-col>
      </v-row>
      <v-row v-if="pulsNews">
        <v-col v-for="i in 6" :key="i" cols="12" sm="6" md="4">
          <v-card class="c-card ma-4">
            <a :href="'//' + news[i + 5].href" target="_blank">
              <v-img
                class="c-news"
                :class="'c-news-' + $vuetify.breakpoint.name"
                style="
                  border: 2px solid #000000;
                  border-top-left-radius: 10px;
                  border-top-right-radius: 10px;
                "
                :src="news[i + 5]"
                lazy-src="@/assets/images/lazy-loading.jpg"
              >
                <template v-slot:placeholder>
                  <lazy-loading />
                </template>
              </v-img>
            </a>
            <v-card-title>
              <a
                style="
                  text-decoration: none;
                  color: #000000;
                  text-overflow: ellipsis;
                  overflow: hidden;
                  white-space: nowrap;
                "
                :href="'//' + news[i + 5].href"
                target="_blank"
                class="text-left"
                >{{ news[i + 5].title }}
              </a>
            </v-card-title>
            <v-card-subtitle class="text-left">
              <a
                style="text-decoration: none; color: #000000"
                :href="'//' + news[i + 5].href"
                target="_blank"
              >
                {{ news[i + 5].writer }} {{ news[i + 5].regtime }}
              </a>
            </v-card-subtitle>
          </v-card>
        </v-col>
        <v-col cols="12" class="py-12">
          <v-btn
            class="c-btn pa-4"
            text
            style="color: #000000"
            :href="'//www.hkisnews.com/'"
            target="_blank"
          >
            더 보러가기
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import CoreBanner from "@/components/core/Banner";
import CoreSection from "@/components/core/Section";
import CardWithCaption from "@/components/home/CardWithCaption";

export default {
  name: "Home",
  data() {
    return {
      pulsNews: false,
      items: [
        { name: "권경은", src: "권경은.png" },
        { name: "김현수", src: "김현수.jpg" },
        { name: "박지윤", src: "박지윤.jpg" },
        { name: "박태록", src: "박태록.jpg" },
        { name: "이동혁", src: "이동혁.png" },
      ],
      news: [
        {
          title: "환경부, 지심도 마을지구 지정 신청 관련 거제시 방문",
          writer: "허재현기자",
          regtime: "2020.10.05 16:18",
          src:
            "http://www.hkisnews.com/imgdata/hkisnews_com/202010/2020100519191915.jpg",
          href: "www.hkisnews.com/43760",
        },
        {
          title: "‘우주의 눈’천리안위성 2B호 해양위성영상 제공 개시",
          writer: "환경이슈신문",
          regtime: "2020.10.05 08:57",
          src:
            "http://tr.xza.kr/imgdata/tr_xza_kr/202010/20201004204008-47974.png",
          href: "www.hkisnews.com/43674",
        },

        {
          title: "국립공원 사진공모전, 권영덕씨 설악산 ‘승천’ 대상",
          writer: "권병창기자",
          regtime: "2020.10.04 14:43",
          src: "http://www.ecobs.co.kr/news/photo/202010/26659_23700_257.jpg",
          href: "www.hkisnews.com/43648",
        },

        {
          title: "페트병 등 포장재, 재활용 쉽게 제작된다",
          writer: "환경이슈신문",
          regtime: "2020.09.28 08:58",
          src:
            "http://tr.xza.kr/imgdata/tr_xza_kr/202009/20200927215250-17119.png",
          href: "www.hkisnews.com/43337",
        },

        {
          title: "“비오는 밤에도 차선이 잘 보이는 안전한 도로” 관리 · 강화",
          writer: "환경이슈신문",
          regtime: "2020.09.28 08:57",
          src:
            "http://tr.xza.kr/imgdata/tr_xza_kr/202009/20200927214518-68164.png",
          href: "www.hkisnews.com/43336",
        },

        {
          title: "노후 어업지도선, 친환경·다목적 관공선으로 새단장",
          writer: "환경이슈신문",
          regtime: "2020.09.22 20:01",
          src:
            "http://tr.xza.kr/imgdata/tr_xza_kr/202009/20200922200104-59632.png",
          href: "www.hkisnews.com/42827",
        },

        {
          title: "환경교육과 기후행동, 종교인이 앞장선다",
          writer: "환경이슈신문",
          regtime: "2020.09.22 08:12",
          src:
            "http://tr.xza.kr/imgdata/tr_xza_kr/202009/20200922081204-62596.png",
          href: "www.hkisnews.com/42676",
        },

        {
          title: "가습기살균제 특별구제 대상자 16명 추가 인정, 총 2,255명 인정",
          writer: "환경이슈신문",
          regtime: "2020.09.18 18:25",
          src:
            "http://tr.xza.kr/imgdata/tr_xza_kr/202009/20200918182522-30982.png",
          href: "www.hkisnews.com/42423",
        },

        {
          title: "2020년 대한민국 건축행정 평가 결과 발표",
          writer: "환경이슈신문",
          regtime: "2020.09.17 07:44",
          src:
            "http://tr.xza.kr/imgdata/tr_xza_kr/202009/20200917074409-11325.png",
          href: "www.hkisnews.com/42156",
        },
        {
          title: "조류인플루엔자, 겨울철새 도래 전에 미리 대비한다",
          writer: "환경이슈신문",
          regtime: "2020.09.17 07:43",
          src:
            "http://tr.xza.kr/imgdata/tr_xza_kr/202009/20200917074225-7246.png",
          href: "www.hkisnews.com/42155",
        },

        {
          title: "한·중 양국, 불법조업 중국어선 꼼짝마",
          writer: "환경이슈신문",
          regtime: "2020.09.11 09:34",
          src:
            "http://tr.xza.kr/imgdata/tr_xza_kr/202009/20200911093419-27265.png",
          href: "www.hkisnews.com/41556",
        },

        {
          title: "그린뉴딜 시대, 깨끗하고 6안전한 물관리 체계 조성",
          writer: "환경이슈신문",
          regtime: "2020.09.09 13:35",
          src:
            "http://tr.xza.kr/imgdata/tr_xza_kr/202009/20200909133531-59235.png",
          href: "www.hkisnews.com/41319",
        },
      ],
    };
  },
  components: {
    CoreSection,
    CardWithCaption,
    CoreBanner,
  },
};
</script>

<style lang="scss" scoped>
.c-card {
  border: 2px solid black;
  border-radius: 15px;
  font-family: "NanumBarunpen";

  &:hover {
    transform: translate3d(0px, -5px, -5px);
    box-shadow: 3px 3px black;
    transition: 0.4s;
    cursor: pointer;
  }
}

.c-highlight {
  background: url("~@/assets/illust/one-line-highlight.svg") no-repeat center;
  background-size: 100%;
}

.c-sheet {
  border: 2px solid black;
  border-radius: 5px;
  &-md,
  &-lg,
  &-xl {
    height: 290px;
    width: 290px;
  }
  &-sm {
    height: 200px;
    width: 200px;
  }
  &-xs {
    height: 160px;
    width: 160px;
  }
}

.c-news {
  font-size: 35px;
  font-weight: 700;
  letter-spacing: -2px;
  line-height: 1.3;
  &-md,
  &-lg,
  &-xl {
    height: 280px;
    font-size: 52px;
    letter-spacing: -2.5px;
    line-height: 1.2;
  }
  &-sm {
    height: 240px;
  }
  &-xs {
    height: 200px;
  }
}

#section-hero {
  z-index: 3;
}

.c-title {
  font-family: "Nunito", "NanumBarunpen", sans-serif;
  font-size: 35px;
  font-weight: 700;
  letter-spacing: -2px;
  line-height: 1.3;

  &-md {
    font-size: 52px;
    letter-spacing: -2.5px;
    line-height: 1.2;
  }
  &-lg,
  &-xl {
    font-size: 64px;
    letter-spacing: -3px;
    line-height: 1.2;
  }
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

.c-btn {
  font-family: "S-CoreDream-7ExtraBold";
  border: 2px solid black;
  border-radius: 10px;
}
</style>
