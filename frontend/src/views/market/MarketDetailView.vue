<template>
  <div id="market-detail">
    <market-hero />

    <section id="product-list">
      <v-container class="text-center">
        <v-row justify="center">
          <v-col cols="12" md="8">
            <market-navbar />
          </v-col>
        </v-row>

        <v-row justify="center">
          <v-col cols="12" md="8"></v-col>
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
  name: "MarketDetailView",
  components: {
    MarketHero,
    MarketNavbar,
  },
};
</script>

<style>
</style>