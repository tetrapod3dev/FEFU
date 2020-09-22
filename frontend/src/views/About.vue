<template>
  <div class="about">
    <section id="section-hero">
      <v-container
        :style="'height: calc(100vh - ' + $vuetify.application.top + 'px)'"
        class="about-hero"
        fill-height
      >
        <v-img :src="require('@/assets/images/about-hero.jpg')" />
      </v-container>
    </section>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
</style>