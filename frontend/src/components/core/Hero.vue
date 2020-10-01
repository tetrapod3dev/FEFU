<template>
  <section id="section-hero">
    <v-container
      :style="'min-height: calc(100vh - ' + $vuetify.application.top + 'px)'"
      fill-height
    >
      <slot name="header">
        <v-row align="start"></v-row>
      </slot>
      <slot>
        <v-row
          align="center"
          class="mx-auto"
          justify="center"
          style="position: relative"
        >
          <v-img :src="backimage" />
          <v-overlay :absolute="true" opacity="0" z-index="0">
            <v-container fill-height>
              <v-col
                class="black--text c-txt"
                :class="'c-txt-' + $vuetify.breakpoint.name"
                cols="12"
                >{{ subtitle }}</v-col
              >
              <v-col>
                <v-img :max-height="maxHeight" contain :src="mainimage" />
              </v-col>
            </v-container>
          </v-overlay>
        </v-row>
      </slot>
      <slot name="footer"></slot>
    </v-container>
  </section>
</template>

<script>
export default {
  name: "CoreHero",
  props: {
    backimage: String,
    subtitle: String,
    mainimage: String,
    maxHeight: {
      type: String,
      default: "260",
    },
  },
};
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap");
@font-face {
  font-family: "NanumSquareRound";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_two@1.0/NanumSquareRound.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}

.c-txt {
  font-size: 18px;
  font-family: "Nunito", "NanumSquareRound", sans-serif;

  &-md {
    font-size: 20px;
  }
  &-lg {
    font-size: 24px;
  }
}
</style>