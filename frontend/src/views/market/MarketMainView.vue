<template>
  <div class="market-main">
    <section id="section-hero">
      <v-img
        id="about-hero"
        style="position: absolute"
        position="top"
        :height="$vuetify.breakpoint.smAndDown ? '25vh' : '50vh'"
        src="@/assets/images/market-hero.jpg"
      />
      <v-img
        style="position: relative; z-index: 3;"
        position="bottom"
        :height="$vuetify.breakpoint.smAndDown ? '25vh' : '50vh'"
        src="@/assets/illust/market-hero.svg"
      />
    </section>
    <v-container>
      <v-row>
        <v-col cols="3">
          <market-search />
          <market-category class="custom-category" />
        </v-col>

        <v-col cols="9" class="pt-0">
          <div class="market-section">
            <h1 class="market-title">
              <span class="title-point">이 상품</span> 어때요
            </h1>
            <v-row>
              <v-col v-for="(product, index) in products" :key="index" cols="4">
                <v-card
                  class="custom-card ma-4"
                  :height="1.6 * cardWidth"
                  :width="cardWidth"
                  cols="12"
                  md="4"
                >
                  <v-img
                    :height="1.2 * cardWidth"
                    src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
                  ></v-img>

                  <v-card-text class="text-left text--primary">
                    <div>{{ product.name }}</div>
                    <div>{{ product.price }}</div>
                    <div>{{ product.price }}</div>
                  </v-card-text>
                </v-card>
              </v-col>
            </v-row>
          </div>

          <div class="market-section">
            <h1 class="market-title">
              지금 바로
              <span class="title-point">신상품</span>
            </h1>
            <v-row>
              <v-col
                v-for="(product, index) in products"
                :key="index"
                cols="12"
                md="4"
              >
                <v-card
                  class="custom-card ma-4"
                  :height="1.6 * cardWidth"
                  :width="cardWidth"
                >
                  <v-img
                    :height="1.2 * cardWidth"
                    src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
                  ></v-img>

                  <v-card-text class="text-left text--primary">
                    <div>{{ product.name }}</div>
                    <div>{{ product.price }}</div>
                    <div>{{ product.price }}</div>
                  </v-card-text>
                </v-card>
              </v-col>
            </v-row>
          </div>

          <div class="market-section">
            <h1 class="market-title">
              <span class="title-point">지금 인기</span> 상품
            </h1>
            <v-row>
              <v-col
                v-for="(product, index) in products"
                :key="index"
                cols="12"
                md="4"
              >
                <v-card
                  class="custom-card ma-4"
                  :height="1.6 * cardWidth"
                  :width="cardWidth"
                >
                  <v-img
                    :height="1.2 * cardWidth"
                    src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
                  ></v-img>

                  <v-card-text class="text-left text--primary">
                    <div>{{ product.name }}</div>
                    <div>{{ product.price }}</div>
                    <div>{{ product.price }}</div>
                  </v-card-text>
                </v-card>
              </v-col>
            </v-row>
          </div>
        </v-col>
      </v-row>
    </v-container>
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
      cardSlide1: null,
      cardSlide2: null,
      cardSlide3: null,
      range: [0, 10000],
      select: "Popularity",
      options: [
        "Default",
        "Popularity",
        "Relevance",
        "Price: Low to High",
        "Price: High to Low",
      ],
      page: 1,
      breadcrums: [
        {
          text: "Home",
          disabled: false,
          href: "breadcrumbs_home",
        },
        {
          text: "Clothing",
          disabled: false,
          href: "breadcrumbs_clothing",
        },
        {
          text: "T-Shirts",
          disabled: true,
          href: "breadcrumbs_shirts",
        },
      ],
      min: 0,
      max: 10000,
      items: [
        {
          id: 2,
          name: "Shoes",
          children: [
            { id: 2, name: "Casuals" },
            { id: 3, name: "Formals" },
            { id: 4, name: "Sneakers" },
          ],
        },
        {
          id: 1,
          name: "Clothing",
          children: [
            { id: 5, name: "Shirts" },
            { id: 6, name: "Tops" },
            { id: 7, name: "Tunics" },
            { id: 8, name: "Bodysuit" },
          ],
        },
      ],
      products: [
        {
          id: 1,
          name: "BLACK TEE",
          price: "18.00",
          src: require("@/assets/logo.png"),
        },
        {
          id: 2,
          name: "WHITE TEE",
          price: "40.00",
          src: require("@/assets/logo.png"),
        },
        {
          id: 3,
          name: "Zara limited...",
          price: "25.00",
          src: require("@/assets/logo.png"),
        },
        // {
        //   id: 4,
        //   name: "SKULL TEE",
        //   price: "30.00",
        //   src: require("@/assets/logo.png"),
        // },
        // {
        //   id: 5,
        //   name: "MANGO WINTER",
        //   price: "50.00",
        //   src: require("@/assets/logo.png"),
        // },
        // {
        //   id: 6,
        //   name: "SHIRT",
        //   price: "34.00",
        //   src: require("@/assets/logo.png"),
        // },
        // {
        //   id: 7,
        //   name: "TRUCKER JACKET",
        //   price: "38.00",
        //   src: require("@/assets/logo.png"),
        // },
        // {
        //   id: 8,
        //   name: "COATS",
        //   price: "25.00",
        //   src: require("@/assets/logo.png"),
        // },
        // {
        //   id: 9,
        //   name: "MANGO WINTER",
        //   price: "50.00",
        //   src: require("@/assets/logo.png"),
        // },
        // {
        //   id: 10,
        //   name: "SHIRT",
        //   price: "34.00",
        //   src: require("@/assets/logo.png"),
        // },
        // {
        //   id: 11,
        //   name: "TRUCKER JACKET",
        //   price: "38.00",
        //   src: require("@/assets/logo.png"),
        // },
        // {
        //   id: 12,
        //   name: "COATS",
        //   price: "25.00",
        //   src: require("@/assets/logo.png"),
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
  top: 0px;
  font-family: "NanumBarunpen";

  &:hover {
    transform: translate3d(0px, -5px, -5px);
    box-shadow: 3px 3px black;
    top: -5px;
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
