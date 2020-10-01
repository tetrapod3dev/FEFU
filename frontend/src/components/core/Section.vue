<template>
  <section :id="id">
    <v-container
      class="text-center pa-0"
      :style="minHeight ? 'min-height: ' + minHeight : ''"
      fill-height
    >
      <v-col class="py-12"></v-col>
      <v-row justify="center" class="ma-0">
        <v-col
          class="black--text c-subtitle"
          :class="'c-subtitle-' + $vuetify.breakpoint.name"
          cols="12"
        >
          <slot name="subtitle">{{ subtitle }}</slot>
        </v-col>
        <v-col cols="12">
          <h2
            class="c-title mb-3"
            :class="'c-title-' + $vuetify.breakpoint.name"
          >
            <slot name="title">{{ title }}</slot>
          </h2>
        </v-col>
        <v-col cols="12">
          <v-responsive class="mb-8"></v-responsive>
          <v-responsive
            class="mx-auto mb-8 c-txt"
            :class="'c-txt-' + $vuetify.breakpoint.name"
            max-width="650"
          >
            <p>
              <slot name="text">{{ text }}</slot>
            </p>
          </v-responsive>
        </v-col>
        <slot></slot>
        <v-col cols="12" class="py-12" v-if="centerPadding"></v-col>
        <slot name="content"></slot>
        <v-col cols="12" class="py-12" v-if="endPadding"></v-col>
      </v-row>
    </v-container>
  </section>
</template>

<script>
export default {
  name: "CoreSection",
  props: {
    id: String,
    minHeight: String,
    subtitle: String,
    title: String,
    text: String,
    centerPadding: { type: Boolean, default: true },
    endPadding: { type: Boolean, default: true },
  },
};
</script>

<style lang="scss" scoped>
.c-title {
  font-family: "Nunito", "NanumBarunpen", sans-serif;
  font-size: 35px;
  font-weight: 700;
  letter-spacing: -2px;
  line-height: 1.3;

  &-md {
    font-size: 52px;
    letter-spacing: -2.5px;
    line-height: 1.2;
  }
  &-lg,
  &-xl {
    font-size: 64px;
    letter-spacing: -3px;
    line-height: 1.2;
  }
}

.c-subtitle {
  font-family: "Nunito", "NanumSquareRound", sans-serif;
  font-size: 13px;
  font-weight: bold;
  letter-spacing: 4px;

  &-md {
    font-size: 15px;
  }
  &-lg,
  &-xl {
    font-size: 16px;
  }
}

.c-txt {
  font-family: "Nunito", "NanumSquareRound", sans-serif;
  font-size: 16px;
  font-weight: bold;
  word-break: keep-all;
  color: black;
  max-width: 650px;

  &-md {
    font-size: 18px;
  }
  &-lg,
  &-xl {
    font-size: 20px;
  }
}
</style>