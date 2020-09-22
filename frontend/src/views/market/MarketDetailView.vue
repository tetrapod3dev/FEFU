<template>
  <div id="market-detail">
    <market-hero />

    <section id="product-list">
      <v-container class="text-center">
        <v-row justify="center">
          <v-col cols="12" md="10">
            <market-navbar />
          </v-col>
        </v-row>
      </v-container>
      <div>
        <v-container>
          <v-row justify="center">
            <v-col cols="12" md="10">
              <div class="row">
                <div class="col-md-5 col-sm-5 col-xs-12">
                  <v-carousel>
                    <v-carousel-item v-for="(slide, i) in slides" :key="i">
                      <v-sheet :color="colors[i]" height="100%">
                        <v-row class="fill-height" align="center" justify="center">
                          <div class="display-3">{{ slide }} Slide</div>
                        </v-row>
                      </v-sheet>
                    </v-carousel-item>
                  </v-carousel>
                </div>
                <div class="col-md-7 col-sm-7 col-xs-12">
                  <div class="text-left pl-6">
                    <p class="display-1 mb-0">상품명</p>
                    <p class="headline font-weight-light pt-3">10,000원</p>
                    <p class="headline font-weight-light">1,000p</p>
                    <p class="subtitle-1 font-weight-thin">상품 설명 부분입니다. 이 상품은 무슨 상품 일까요?</p>
                    <p class="title">판매자 정보</p>
                    <p class="subtitle-1 font-weight-thin">지구용사</p>
                    <p class="subtitle-1 font-weight-thin">080-519-1004</p>
                    <v-btn class="ml-4" outlined tile>판매 중</v-btn>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-sm-12 col-xs-12 col-md-12">
                  <v-card-text class="pa-0 pt-4" tile outlined>
                    <p class="subtitle-1 font-weight-light pt-3 text-center">둘러볼 상품</p>
                    <v-divider></v-divider>
                    <div class="row text-center">
                      <v-slide-group v-model="cardSlide1" center-active show-arrows>
                        <v-slide-item
                          v-for="(product, index) in products"
                          :key="index"
                          v-slot:default="{ active, toggle }"
                          href="/market/detail/1"
                        >
                          <v-card
                            :color="active ? 'primary' : ''"
                            class="ma-4"
                            :height="1.6 * cardWidth"
                            :width="cardWidth"
                            @click="toggle"
                          >
                            <v-img
                              :height="cardWidth"
                              src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
                            ></v-img>

                            <v-card-text class="text--primary text-left">
                              <div>{{product.name}}</div>
                              <div>{{product.price}}</div>
                              <div>{{product.price}}</div>
                            </v-card-text>
                          </v-card>
                        </v-slide-item>
                      </v-slide-group>
                    </div>
                  </v-card-text>
                </div>
              </div>
            </v-col>
          </v-row>
        </v-container>
      </div>
      <div class="py-12"></div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import SERVER from "@/api/api";

import MarketHero from "@/components/market/Hero";
import MarketNavbar from "@/components/market/Navbar";

export default {
  name: "MarketDetailView",
  components: {
    MarketHero,
    MarketNavbar,
  },
  created() {
    console.log("test market product detail rest api");
    console.log(SERVER.URL + SERVER.ROUTES.products.URL + "/1");
    axios
      .get(SERVER.URL + SERVER.ROUTES.products.URL + "/1")
      .then((res) => {
        console.log(res);
      })
      .catch((err) => {
        console.log(err);
      });
  },
  computed: {
    cardWidth() {
      let resultWidth;
      switch (this.$vuetify.breakpoint.name) {
        case "xs":
          resultWidth = 160;
          break;
        case "sm":
          resultWidth = 160;
          break;
        case "md":
          resultWidth = 160;
          break;
        case "lg":
          resultWidth = 240;
          break;
        case "xl":
          resultWidth = 240;
          break;
      }
      return resultWidth;
    },
  },
  data() {
    return {
      cardSlide1: null,
      colors: ["indigo", "warning", "pink darken-2"],
      slides: ["First", "Second", "Third"],
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

<style>
</style>