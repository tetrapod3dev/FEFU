<template>
  <div>
    <!-- <campaign hero start -->
    <section id="section-hero">
      <v-img
        style="position: absolute"
        position="top"
        :height="$vuetify.breakpoint.smAndDown ? '24vh' : '49vh'"
        src="@/assets/images/campaign-hero.jpg"
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
        src="@/assets/illust/campaign-hero.svg"
      />
    </section>
    <!-- campaign hero end -->

    <!-- campaign content start -->
    <v-row justify="center">
      <v-col cols="12" xl="8">
        <router-view />
      </v-col>
    </v-row>
    <!-- campaign content end -->
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
};
</script>

<style lang="scss" scoped>
</style>
