<template>
  <div class="market-main">
    <!-- market hero start -->
    <section id="market-hero">
      <v-img
        style="position: absolute"
        position="top"
        :height="$vuetify.breakpoint.smAndDown ? '24vh' : '49vh'"
        src="@/assets/images/market-hero.jpg"
        lazy-src="@/assets/images/lazy-loading.jpg"
      >
        <template v-slot:placeholder>
          <lazy-loading />
        </template>
      </v-img>
      <v-img
        style="position: relative; z-index: 3"
        position="bottom"
        :height="$vuetify.breakpoint.smAndDown ? '25vh' : '50vh'"
        src="@/assets/illust/market-hero.svg"
      />
    </section>
    <!-- market hero end -->

    <!-- market content start -->
    <v-row justify="center">
      <v-col cols="12" xl="8">
        <v-container>
          <v-row>
            <!-- side bar start -->
            <v-col v-if="sidebar" cols="12" sm="3">
              <market-search />
              <market-category class="custom-category" />
            </v-col>
            <!-- side bar end -->

            <router-view />
          </v-row>
        </v-container>
      </v-col>
    </v-row>
    <!-- market content end -->
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
  props: {
    sidebar: {
      type: Boolean,
      default: true,
    },
  },
};
</script>

<style lang="scss" scoped>
</style>