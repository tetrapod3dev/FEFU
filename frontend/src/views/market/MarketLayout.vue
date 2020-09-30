<template>
  <div class="market-main">
    <section id="section-hero">
      <v-img
        id="market-hero"
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

    <v-row justify="center">
      <v-col cols="12" xl="8">
        <v-container>
          <v-row>
            <v-col cols="12" sm="3">
              <market-search />
              <market-category class="custom-category" />
            </v-col>

            <router-view />
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
  name: "MarketLayout",
  components: {
    MarketCategory,
    MarketSearch,
  },
};
</script>

<style lang="scss" scoped>
</style>