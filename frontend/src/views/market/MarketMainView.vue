<template>
  <div>
    <market-hero />

    <v-container>
      <v-row justify="center">
        <v-col cols="12" xl="10">
          <market-navbar />
        </v-col>
      </v-row>
      <h1 class="market-title">
        <span class="title-point">이 상품</span> 어때요
      </h1>
      <v-row justify="center">
        <v-col cols="12" xl="10">
          <v-slide-group center-active v-model="cardSlide1" show-arrows>
            <v-slide-item v-for="(product, index) in products" :key="index">
              <v-card class="custom-card ma-4" :height="1.6 * cardWidth" :width="cardWidth">
                <v-img
                  :height="1.2 * cardWidth"
                  src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
                ></v-img>

                <v-card-text class="text-left text--primary">
                  <div>{{product.name}}</div>
                  <div>{{product.price}}</div>
                  <div>{{product.price}}</div>
                </v-card-text>
              </v-card>
            </v-slide-item>
          </v-slide-group>
        </v-col>
      </v-row>

      <h1 class="market-title">
        지금 바로
        <span class="title-point">신상품</span>
      </h1>

      <v-row justify="center">
        <v-col cols="12" xl="10">
          <v-slide-group v-model="cardSlide2" center-active show-arrows>
            <v-slide-item
              v-for="(product, index) in products"
              :key="index"
              v-slot:default="{ active, toggle }"
            >
              <v-card
                :color="active ? 'primary' : ''"
                class="custom-card ma-4"
                :height="1.6 * cardWidth"
                :width="cardWidth"
                @click="toggle"
              >
                <v-img
                  :height="1.2 * cardWidth"
                  src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
                ></v-img>

                <v-card-text class="text-left text--primary">
                  <div>{{product.name}}</div>
                  <div>{{product.price}}</div>
                  <div>{{product.price}}</div>
                </v-card-text>
              </v-card>
            </v-slide-item>
          </v-slide-group>
        </v-col>
      </v-row>
      <h1 class="market-title">
        <span class="title-point">지금 인기</span> 상품
      </h1>

      <v-row justify="center">
        <v-col cols="12" xl="10">
          <v-slide-group v-model="cardSlide3" center-active show-arrows>
            <v-slide-item
              v-for="(product, index) in products"
              :key="index"
              v-slot:default="{ active, toggle }"
              href="/market/detail/1"
            >
              <v-card
                :color="active ? 'primary' : ''"
                class="custom-card ma-4"
                :height="1.6 * cardWidth"
                :width="cardWidth"
                @click="toggle"
              >
                <v-img
                  :height="1.2 * cardWidth"
                  src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
                ></v-img>

                <v-card-text class="text-left text--primary">
                  <div>{{product.name}}</div>
                  <div>{{product.price}}</div>
                  <div>{{product.price}}</div>
                </v-card-text>
              </v-card>
            </v-slide-item>
          </v-slide-group>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import MarketHero from "@/components/market/Hero";
import MarketNavbar from "@/components/market/Navbar";

export default {
  name: "MarketMainView",
  components: {
    MarketHero,
    MarketNavbar,
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
        {
          id: 4,
          name: "SKULL TEE",
          price: "30.00",
          src: require("@/assets/logo.png"),
        },
        {
          id: 5,
          name: "MANGO WINTER",
          price: "50.00",
          src: require("@/assets/logo.png"),
        },
        {
          id: 6,
          name: "SHIRT",
          price: "34.00",
          src: require("@/assets/logo.png"),
        },
        {
          id: 7,
          name: "TRUCKER JACKET",
          price: "38.00",
          src: require("@/assets/logo.png"),
        },
        {
          id: 8,
          name: "COATS",
          price: "25.00",
          src: require("@/assets/logo.png"),
        },
        {
          id: 9,
          name: "MANGO WINTER",
          price: "50.00",
          src: require("@/assets/logo.png"),
        },
        {
          id: 10,
          name: "SHIRT",
          price: "34.00",
          src: require("@/assets/logo.png"),
        },
        {
          id: 11,
          name: "TRUCKER JACKET",
          price: "38.00",
          src: require("@/assets/logo.png"),
        },
        {
          id: 12,
          name: "COATS",
          price: "25.00",
          src: require("@/assets/logo.png"),
        },
      ],
    };
  },
};
</script>

<style scoped>
.custom-card {
  border: 2px solid black;
  border-radius: 15px;
  top: 0px;
  font-family: "NanumBarunpen";
}

.custom-card:hover {
  transform: translate3d(0px, -5px, -5px);
  box-shadow: 3px 3px black;
  top: -5px;
  transition: 0.4s;
  cursor: pointer;
}

.market-title {
  margin-top: 30px;
  font-family: "NanumBarunpen";
}

.title-point {
  color: var(--primary-color);
}
</style>
