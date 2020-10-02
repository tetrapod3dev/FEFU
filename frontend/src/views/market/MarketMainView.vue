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
            :src="imageSrc(product.photo)"
            lazy-src="@/assets/images/lazy-loading.jpg"
          >
            <template v-slot:placeholder>
              <lazy-loading />
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
            params: { productNo: product.no },
          }"
        >
          <v-img
            :height="1.1 * cardWidth"
            :src="imageSrc(product.photo)"
            lazy-src="@/assets/images/lazy-loading.jpg"
          >
            <template v-slot:placeholder>
              <lazy-loading />
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
            params: { productNo: product.no },
          }"
        >
          <v-img
            :height="1.1 * cardWidth"
            :src="imageSrc(product.photo)"
            lazy-src="@/assets/images/lazy-loading.jpg"
          >
            <template v-slot:placeholder>
              <lazy-loading />
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
  </v-col>
</template>

<script>
import axios from "axios";
import SERVER from "@/api/api";


export default {
  name: "MarketMainView",
  created() {
    this.getRecommendProducts(),
    this.getNewProducts(),
    this.getPopularProducts()
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
    imageSrc(filename) {
      return SERVER.IMAGE_URL + filename;
    },
    getRecommendProducts() {
      axios
        .get(
          SERVER.URL + 
          SERVER.ROUTES.products.recommendation,
          {
            headers: {
              Authorization: this.config,
            },
          }
        )
        .then((res) => {
        // console.log(res.data);
        this.products.recommend = res.data})
        .catch((err) => console.log(err))
    },
    getNewProducts() {
      axios
        .get(
          SERVER.URL + SERVER.ROUTES.products.get_latest_products
        )
        .then((res) => {
          // console.log(res.data)
          this.products.new = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getPopularProducts() {
      axios
        .get(
          SERVER.URL + SERVER.ROUTES.products.top_three_viewed_today
        )
        .then((res) => {
          // console.log(res.data)
          this.products.popular = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
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
