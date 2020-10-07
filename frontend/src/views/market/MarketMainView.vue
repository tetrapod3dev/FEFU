<template>
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
        <market-card :product="product"> </market-card>
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
        <market-card :product="product"> </market-card>
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
        <market-card :product="product"> </market-card>
      </v-col>
    </v-row>
  </v-col>
</template>

<script>
import axios from "axios";
import SERVER from "@/api/api";

import MarketCard from "@/components/market/MarketCard.vue";

export default {
  name: "MarketMainView",
  created() {
    this.getRecommendProducts(),
    this.getNewProducts(),
    this.getPopularProducts();
  },
  components: {
    MarketCard,
  },
  data() {
    return {
      page: 1,
      products: {
        recommend: [
          {
            no: 0,
            title: "",
            price: "",
            eco_point: "",
            photo: "a9e5bb88-bbc2-485d-800a-26908a539ba2.png",
          },
          {
            no: 0,
            title: "",
            price: "",
            eco_point: "",
            photo: "a9e5bb88-bbc2-485d-800a-26908a539ba2.png",
          },
          {
            no: 0,
            title: "",
            price: "",
            eco_point: "",
            photo: "a9e5bb88-bbc2-485d-800a-26908a539ba2.png",
          },
        ],
        new: [
          {
            no: 0,
            title: "",
            price: "",
            eco_point: "",
            photo: "a9e5bb88-bbc2-485d-800a-26908a539ba2.png",
          },
          {
            no: 0,
            title: "",
            price: "",
            eco_point: "",
            photo: "a9e5bb88-bbc2-485d-800a-26908a539ba2.png",
          },
          {
            no: 0,
            title: "",
            price: "",
            eco_point: "",
            photo: "a9e5bb88-bbc2-485d-800a-26908a539ba2.png",
          },
        ],
        popular: [
          {
            no: 0,
            title: "",
            price: "",
            eco_point: "",
            photo: "a9e5bb88-bbc2-485d-800a-26908a539ba2.png",
          },
          {
            no: 0,
            title: "",
            price: "",
            eco_point: "",
            photo: "a9e5bb88-bbc2-485d-800a-26908a539ba2.png",
          },
          {
            no: 0,
            title: "",
            price: "",
            eco_point: "",
            photo: "a9e5bb88-bbc2-485d-800a-26908a539ba2.png",
          },
        ],
      },
    };
  },
  methods: {
    getRecommendProducts() {
      axios
        .get(SERVER.URL + SERVER.ROUTES.products.recommendation, {
          headers: {
            Authorization: this.config,
          },
        })
        .then((res) => {
          // console.log(res.data);
          this.products.recommend = res.data;
        })
        .catch((err) => console.log(err));
    },
    getNewProducts() {
      axios
        .get(SERVER.URL + SERVER.ROUTES.products.get_latest_products)
        .then((res) => {
          // console.log(res.data)
          this.products.new = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getPopularProducts() {
      axios
        .get(SERVER.URL + SERVER.ROUTES.products.top_three_viewed_today)
        .then((res) => {
          // console.log(res.data)
          this.products.popular = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style lang="scss" scoped>
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
