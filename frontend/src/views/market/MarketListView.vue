<template>
  <div id="market-list">
    <market-hero />

    <section id="product-list">
      <v-container class="text-center">
        <v-row justify="center">
          <v-col cols="12" md="8">
            <market-navbar />
          </v-col>
        </v-row>

        <v-row justify="center">
          <v-col cols="12" md="8">
            <v-row>
              <v-col v-for="(product, index) in products" :key="index" cols="12" md="4">
                <v-item v-slot:default="{ active, toggle }">
                  <v-card
                    href="/market/detail/1"
                    :color="active ? 'primary' : ''"
                    class="ma-4"
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
                </v-item>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-container>

      <div class="py-12"></div>
    </section>
  </div>
</template>

<script>
import MarketHero from "@/components/market/Hero";
import MarketNavbar from "@/components/market/Navbar";

export default {
  name: "MarketListView",
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