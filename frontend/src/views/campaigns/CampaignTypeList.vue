<template>
  <div>
    <section id="section-hero">
      <v-img
        id="about-hero"
        style="position: absolute"
        position="top"
        :height="$vuetify.breakpoint.smAndDown ? '24vh' : '49vh'"
        src="@/assets/images/campaign-hero.jpg"
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
        src="@/assets/illust/campaign-hero.svg"
      />
    </section>

    <h1>{{ campaignType }}</h1>
    <h1>{{ pageNum }}</h1>

  </div>
</template>

<script>
export default {
  name: 'CampaignTypeList',
  data() {
      return {
          campaignType: this.$route.params.campaign_type,
          pageNum: this.$route.params.page_num,
      }
  }
}
</script>

<style>

</style>