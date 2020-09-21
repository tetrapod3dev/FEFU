<template>
  <section :id="id">
    <v-container class="text-center" :style="'min-height: ' + minHeight " fill-height>
      <v-col class="py-12"></v-col>
      <v-row align="center">
        <v-col
          class="black--text custom-subtitle"
          :class="'custom-subtitle-'+$vuetify.breakpoint.name"
          cols="12"
        >
          <slot name="subtitle">{{subtitle}}</slot>
        </v-col>
        <v-col cols="12">
          <h2 class="custom-title mb-3" :class="'custom-title-'+$vuetify.breakpoint.name">
            <slot name="title">{{title}}</slot>
          </h2>
        </v-col>
        <v-col cols="12">
          <v-responsive class="mb-8"></v-responsive>
          <v-responsive
            class="mx-auto mb-8 custom-text"
            :class="'custom-text-'+$vuetify.breakpoint.name"
            max-width="650"
          >
            <p>
              <slot name="text">{{text}}</slot>
            </p>
          </v-responsive>
        </v-col>
        <slot></slot>
        <v-col cols="12" class="py-12"></v-col>
        <slot name="content"></slot>
        <v-col cols="12" class="py-12"></v-col>
      </v-row>
    </v-container>
  </section>
</template>

<script>
export default {
  name: "CoreSection",
  props: ["id", "minHeight", "subtitle", "title", "text"],
};
</script>

<style lang="scss" scoped>
.custom-title {
  font-size: 35px;
  letter-spacing: -2px;
  line-height: 1.3;
  font-weight: 700;
  font-family: "Nunito", "NanumBarunpen", sans-serif;

  &-md {
    font-size: 52px;
    letter-spacing: -2.5px;
    line-height: 1.2;
  }
  &-lg {
    font-size: 64px;
    letter-spacing: -3px;
    line-height: 1.2;
  }
}

.custom-subtitle {
  font-size: 13px;
  font-weight: bold;
  letter-spacing: 4px;
  font-family: "Nunito", "NanumSquareRound", sans-serif;

  &-md {
    font-size: 15px;
  }
  &-lg {
    font-size: 16px;
  }
}

.custom-text {
  font-size: 16px;
  word-break: keep-all;
  font-weight: bold;
  color: black;
  font-family: "Nunito", "NanumSquareRound", sans-serif;
  max-width: 650px;

  &-md {
    font-size: 18px;
  }
  &-lg {
    font-size: 20px;
  }
}
</style>