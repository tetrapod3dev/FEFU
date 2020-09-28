<template>
  <div id="market-list">
    <section id="section-hero">
      <v-img
        id="about-hero"
        style="position: absolute"
        position="top"
        :height="$vuetify.breakpoint.smAndDown ? '24vh' : '49vh'"
        src="@/assets/images/market-hero.jpg"
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
        :height="$vuetify.breakpoint.smAndDown ? '25vh' : '50vh'"
        src="@/assets/illust/market-hero.svg"
      />
    </section>

    <v-container>
      <v-row>
        <v-col cols="12" sm="3">
          <div :class="$vuetify.breakpoint.smAndDown ? '' : 'fixed-bar'">
            <market-search />
            <market-category class="custom-category" />
          </div>
        </v-col>

        <v-col cols="12" sm="9" class="pt-0">
          <div class="market-section">
            <h1 class="market-title text-left ml-3">
              {{ $route.params.mainCategory }} >
              {{ $route.params.mediumCategory }}
            </h1>
            <v-row>
              <v-col
                v-for="(product, index) in products"
                :key="index"
                cols="6"
                sm="4"
                justify="center"
                align="center"
              >
                <v-card
                  class="custom-card"
                  :height="1.6 * cardWidth"
                  :width="cardWidth"
                  :to="{
                    name: 'MarketDetailView',
                    params: { productNo: product.no },
                  }"
                >
                  <v-img
                    :height="1.1 * cardWidth"
                    :src="
                      'http://j3a402.p.ssafy.io:8801/images/download/' +
                      product.photo
                    "
                    lazy-src="@/assets/images/lazy-loading.jpg"
                  >
                    <template v-slot:placeholder>
                      <v-row
                        class="fill-height ma-0"
                        align="center"
                        justify="center"
                      >
                        <v-progress-circular
                          indeterminate
                          color="grey lighten-5"
                        ></v-progress-circular>
                      </v-row>
                    </template>
                  </v-img>

                  <v-card-text class="text-left text--primary">
                    <div>{{ product.title }}</div>
                    <div>{{ product.price }}</div>
                    <div>{{ product.eco_point }}</div>
                  </v-card-text>
                </v-card>
              </v-col>
            </v-row>
            <v-pagination
              :pageLinkClass="'custom-pagination'"
              v-model="page"
              :length="5"
              :page="page"
              :total-visible="5"
            ></v-pagination>
          </div>
        </v-col>
      </v-row>
    </v-container>

    <section>
      <div class="py-12"></div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import SERVER from "@/api/api";

import MarketCategory from "@/components/market/Category";
import MarketSearch from "@/components/market/Search";

export default {
  name: "MarketListView",
  components: {
    MarketCategory,
    MarketSearch,
  },
  created() {
    this.getProducts();
  },
  computed: {
    cardWidth() {
      let resultWidth;
      switch (this.$vuetify.breakpoint.name) {
        case "xs":
          resultWidth = 220;
          break;
        case "sm":
          resultWidth = 220;
          break;
        case "md":
          resultWidth = 220;
          break;
        case "lg":
          resultWidth = 280;
          break;
        case "xl":
          resultWidth = 280;
          break;
      }
      return resultWidth;
    },
  },
  methods: {
    getProducts() {
      axios
        .get(SERVER.URL + SERVER.ROUTES.products.URL, {
          params: {
            pageNum: this.$route.params.pageNum,
            mainCategory: 1,
            mediumCategory: 1,
            content: this.$route.params.content,
          },
        })
        .then((res) => {
          console.log(res);
          this.products = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  data() {
    return {
      page: 1,
      products: [
        // {
        //   id: 1,
        //   name: "위즈 2단 독서대 60cm(오른팔용)",
        //   price: "20,000",
        //   eco: "5,000",
        //   src:
        //     "https://dnvefa72aowie.cloudfront.net/origin/article/202009/4F9A716A18F20012DF757BD380AEE17B476263E20DE23F07395ED7692C547F56.jpg?q=95&s=1440x1440&t=inside",
        // },
        // {
        //   id: 2,
        //   name: "200km 주행 샤오미 전기자전거",
        //   price: "560,000",
        //   eco: "60,000",
        //   src:
        //     "https://dnvefa72aowie.cloudfront.net/origin/article/202009/24637A81F60C69C9B086CF1ADD0DCEADD400DAFE11F53C8C4A6F55E666CE1DEC.jpg?q=95&s=1440x1440&t=inside",
        // },
        // {
        //   id: 3,
        //   name: "(정품) 발렌티노 히든 스니커즈",
        //   price: "200,000",
        //   eco: "10,000",
        //   src:
        //     "https://dnvefa72aowie.cloudfront.net/origin/article/202009/9ED5BC30D37442E3D598BB842AC003165FE3B2B5E99BCFE0EF52EEC9E845928A.jpg?q=95&s=1440x1440&t=inside",
        // },
        // {
        //   id: 4,
        //   name: "헤이 클로쉐 테이블 스탠드 HAY CLOCHE TABLE LAMP",
        //   price: "250,000",
        //   eco: "50,000",
        //   src:
        //     "https://dnvefa72aowie.cloudfront.net/origin/article/202009/A8FBF37CCD0F318438B4038EE88E55A0678E67A154FA3208B080D1F4D1CC22EF.jpg?q=95&s=1440x1440&t=inside",
        // },
        // {
        //   id: 5,
        //   name: "긴급처분)의자",
        //   price: "12,000",
        //   eco: "2,000",
        //   src:
        //     "https://dnvefa72aowie.cloudfront.net/origin/article/202009/A5AE64A79B6A986825AE405A5955D062C65881B28B1F574534CCF85078E9E016.jpg?q=95&s=1440x1440&t=inside",
        // },
        // {
        //   id: 6,
        //   name: "의류 쇼룸 매장 집기 일괄 판매합니다!",
        //   price: "150,000",
        //   eco: "10,000",
        //   src:
        //     "https://dnvefa72aowie.cloudfront.net/origin/article/202009/902CFB62081E669CE8FEEB66F4C91FFA1D67FA2068011933651004A021249BF8.jpg?q=95&s=1440x1440&t=inside",
        // },
        // {
        //   id: 7,
        //   name: "빈티지 책장식 ✩ 무배 ✩ 종류많아요",
        //   price: "20,000",
        //   eco: "2,000",
        //   src:
        //     "https://dnvefa72aowie.cloudfront.net/origin/article/202009/4F9A716A18F20012DF757BD380AEE17B476263E20DE23F07395ED7692C547F56.jpg?q=95&s=1440x1440&t=inside",
        // },
        // {
        //   id: 8,
        //   name:
        //     "아이패드 에어 3세대 (256GB, S급, 케이스/아이패드 충전기/에어팟/애플펜슬까지 일괄로 한번에 급처 합니다.",
        //   price: "550,000",
        //   eco: "50,000",
        //   src:
        //     "https://dnvefa72aowie.cloudfront.net/origin/article/202009/3D5A32C58C62CD9BD5D56D3803B6FE27B230FDEA2D31D76D89F81615493DE480.jpg?q=95&s=1440x1440&t=inside",
        // },
        // {
        //   id: 9,
        //   name: "원목다용도선반 판매합니다",
        //   price: "5,000",
        //   eco: "5,000",
        //   src:
        //     "https://dnvefa72aowie.cloudfront.net/origin/article/202009/b98f44be90258602e79e83e2030fac6c877eb3822848cc7ea7c8518a46b6fbe1.webp?q=95&s=1440x1440&t=inside",
        // },
      ],
    };
  },
};
</script>

<style lang="scss" scoped>
.custom-card {
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

.market-section {
  margin-bottom: 0px;
}

.market-title {
  margin-top: 10px;
  font-family: "NanumBarunpen";
}

.title-point {
  color: var(--primary-color);
}

.custom-pagination .v-pagination {
  .v-pagination__navigation,
  .v-pagination_item {
    border: 2px solid #000000 !important;
    &--active {
      background-color: var(--primary-color);
    }
  }
}

.fixed-bar {
  position: -webkit-sticky;
  position: sticky;
  top: 4rem;
  z-index: 2;
}
</style>
