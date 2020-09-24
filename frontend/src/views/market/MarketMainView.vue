<template>
  <div class="market-main">
    <section id="section-hero">
      <v-img
        id="about-hero"
        style="position: absolute"
        position="top"
        :height="$vuetify.breakpoint.smAndDown ? '24vh' : '49vh'"
        src="@/assets/images/market-hero.jpg"
      />
      <v-img
        style="position: relative; z-index: 3"
        position="bottom"
        :height="$vuetify.breakpoint.smAndDown ? '25vh' : '50vh'"
        src="@/assets/illust/market-hero.svg"
      />
    </section>
    <v-row justify="center">
      <v-col cols="12" xl="8">
        <v-container>
          <v-row>
            <v-col cols="12" sm="3">
              <market-search />
              <market-category class="custom-category" />
            </v-col>

            <v-col cols="12" sm="9" class="pt-0">
              <v-row justify="space-around">
                <v-col cols="12" class="market-section">
                  <h1 class="market-title">
                    <span class="title-point">이 상품</span> 어때요
                  </h1>
                </v-col>
                <v-col
                  v-for="(product, index) in products.recommend"
                  :key="index"
                  cols="12"
                  md="4"
                  align="center"
                >
                  <v-card
                    class="custom-card ma-4"
                    :height="1.6 * cardWidth"
                    :width="cardWidth"
                    :to="{
                      name: 'MarketDetailView',
                      params: { productNo: product.id },
                    }"
                  >
                    <v-img :height="1.1 * cardWidth" :src="product.src"></v-img>

                    <v-card-text class="text-left text--primary">
                      <div>{{ product.name }}</div>
                      <div>{{ product.price }}</div>
                      <div>{{ product.eco }}</div>
                    </v-card-text>
                  </v-card>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12" class="market-section">
                  <h1 class="market-title">
                    지금 바로
                    <span class="title-point">신상품</span>
                  </h1>
                </v-col>
                <v-col
                  v-for="(product, index) in products.new"
                  :key="index"
                  cols="12"
                  md="4"
                  align="center"
                >
                  <v-card
                    class="custom-card ma-4"
                    :height="1.6 * cardWidth"
                    :width="cardWidth"
                    :to="{
                      name: 'MarketDetailView',
                      params: { productNo: product.id },
                    }"
                  >
                    <v-img :height="1.1 * cardWidth" :src="product.src"></v-img>

                    <v-card-text class="text-left text--primary">
                      <div>{{ product.name }}</div>
                      <div>{{ product.price }}</div>
                      <div>{{ product.eco }}</div>
                    </v-card-text>
                  </v-card>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12" class="market-section">
                  <h1 class="market-title">
                    <span class="title-point">지금 인기</span> 상품
                  </h1>
                </v-col>
                <v-col
                  v-for="(product, index) in products.popular"
                  :key="index"
                  cols="12"
                  md="4"
                  align="center"
                >
                  <v-card
                    class="custom-card ma-4"
                    :height="1.6 * cardWidth"
                    :width="cardWidth"
                    :to="{
                      name: 'MarketDetailView',
                      params: { productNo: product.id },
                    }"
                  >
                    <v-img :height="1.1 * cardWidth" :src="product.src"></v-img>

                    <v-card-text class="text-left text--primary">
                      <div>{{ product.name }}</div>
                      <div>{{ product.price }}</div>
                      <div>{{ product.eco }}</div>
                    </v-card-text>
                  </v-card>
                </v-col>
              </v-row>
            </v-col>
          </v-row>
        </v-container>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import MarketCategory from "@/components/market/Category";
import MarketSearch from "@/components/market/Search";

export default {
  name: "MarketMainView",
  components: {
    MarketCategory,
    MarketSearch,
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
  data() {
    return {
      page: 1,
      products: {
        recommend: [
          {
            id: 1,
            name: "위즈 2단 독서대 60cm(오른팔용)",
            price: "20000",
            eco: "5000",
            src:
              "https://dnvefa72aowie.cloudfront.net/origin/article/202009/4F9A716A18F20012DF757BD380AEE17B476263E20DE23F07395ED7692C547F56.jpg?q=95&s=1440x1440&t=inside",
          },
          {
            id: 2,
            name: "200km 주행 샤오미 전기자전거",
            price: "560000",
            eco: "60000",
            src:
              "https://dnvefa72aowie.cloudfront.net/origin/article/202009/24637A81F60C69C9B086CF1ADD0DCEADD400DAFE11F53C8C4A6F55E666CE1DEC.jpg?q=95&s=1440x1440&t=inside",
          },
          {
            id: 3,
            name: "(정품) 발렌티노 히든 스니커즈",
            price: "200000",
            eco: "10000",
            src:
              "https://dnvefa72aowie.cloudfront.net/origin/article/202009/9ED5BC30D37442E3D598BB842AC003165FE3B2B5E99BCFE0EF52EEC9E845928A.jpg?q=95&s=1440x1440&t=inside",
          },
        ],
        new: [
          {
            id: 4,
            name: "헤이 클로쉐 테이블 스탠드 HAY CLOCHE TABLE LAMP",
            price: "250000",
            eco: "50000",
            src:
              "https://dnvefa72aowie.cloudfront.net/origin/article/202009/A8FBF37CCD0F318438B4038EE88E55A0678E67A154FA3208B080D1F4D1CC22EF.jpg?q=95&s=1440x1440&t=inside",
          },
          {
            id: 5,
            name: "긴급처분)의자",
            price: "12000",
            eco: "2000",
            src:
              "https://dnvefa72aowie.cloudfront.net/origin/article/202009/A5AE64A79B6A986825AE405A5955D062C65881B28B1F574534CCF85078E9E016.jpg?q=95&s=1440x1440&t=inside",
          },
          {
            id: 6,
            name: "의류 쇼룸 매장 집기 일괄 판매합니다!",
            price: "150000",
            eco: "10000",
            src:
              "https://dnvefa72aowie.cloudfront.net/origin/article/202009/902CFB62081E669CE8FEEB66F4C91FFA1D67FA2068011933651004A021249BF8.jpg?q=95&s=1440x1440&t=inside",
          },
        ],
        popular: [
          {
            id: 7,
            name: "빈티지 책장식 ✩ 무배 ✩ 종류많아요",
            price: "20000",
            eco: "2000",
            src:
              "https://dnvefa72aowie.cloudfront.net/origin/article/202009/4F9A716A18F20012DF757BD380AEE17B476263E20DE23F07395ED7692C547F56.jpg?q=95&s=1440x1440&t=inside",
          },
          {
            id: 8,
            name:
              "아이패드 에어 3세대 (256GB, S급, 케이스/아이패드 충전기/에어팟/애플펜슬까지 일괄로 한번에 급처 합니다.",
            price: "550000",
            eco: "50000",
            src:
              "https://dnvefa72aowie.cloudfront.net/origin/article/202009/3D5A32C58C62CD9BD5D56D3803B6FE27B230FDEA2D31D76D89F81615493DE480.jpg?q=95&s=1440x1440&t=inside",
          },
          {
            id: 9,
            name: "원목다용도선반 판매합니다",
            price: "5000",
            eco: "5000",
            src:
              "https://dnvefa72aowie.cloudfront.net/origin/article/202009/b98f44be90258602e79e83e2030fac6c877eb3822848cc7ea7c8518a46b6fbe1.webp?q=95&s=1440x1440&t=inside",
          },
        ],
      },
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
</style>
