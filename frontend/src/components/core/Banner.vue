<template>
  <v-row justify="center" align="stretch">
    <slot name="content">
      <v-col
        cols="8"
        md="10"
        class="c-txt text-left px-15 py-6 c-banner ma-0"
        :class="'c-banner-' + $vuetify.breakpoint.name"
      >
        {{ content }}
      </v-col>
    </slot>
    <v-col
      cols="4"
      md="10"
      class="c-banner ma-0 py-6"
      :class="'c-banner-' + $vuetify.breakpoint.name"
    >
      <router-link
        tag="a"
        :to="to"
        class="c-btn--text"
        :class="'c-btn--text-' + $vuetify.breakpoint.name"
      >
        {{ btnText }}
        <v-img
          style="cursor: pointer; margin-top: 3px"
          :width="$vuetify.breakpoint.smAndDown ? 15 : 17"
          :height="$vuetify.breakpoint.smAndDown ? 15 : 17"
          class="c-btn--text-icon"
          contain
          :src="require('@/assets/illust/arrow-right.svg')"
        />
      </router-link>
    </v-col>
  </v-row>
</template>

<script>
export default {
  props: ["content", "btnText", "to"],
};
</script>

<style lang="scss" scoped>
.c-txt {
  font-size: 16px;
  word-break: keep-all;
  font-weight: bold;
  color: black;
  font-family: "Nunito", "NanumSquareRound", sans-serif;

  &-md {
    font-size: 18px;
  }
  &-lg,
  &-xl {
    font-size: 20px;
  }
}

.c-banner {
  border-radius: 5px;
  background-color: var(--primary-color);

  &-xs:first-child,
  &-sm:first-child {
    border-top-right-radius: 0;
    border-bottom-right-radius: 0;
  }

  &-xs:last-child,
  &-sm:last-child {
    border-top-left-radius: 0;
    border-bottom-left-radius: 0;
  }

  &-md:first-child,
  &-lg:first-child,
  &-xl:first-child {
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
  }
  &-md:last-child,
  &-lg:last-child,
  &-xl:last-child {
    border-top-left-radius: 0;
    border-top-right-radius: 0;
  }
}

.c-btn--text {
  display: inline-block;
  text-decoration: none;
  border-bottom: 2px solid #000000;
  padding: 2px 0;
  font-family: "Nunito", "NanumSquareRound", sans-serif;
  font-size: 16px;
  color: #000000;
  transition: 0.3s;

  &-md,
  &-lg,
  &-xl {
    font-size: 18px;
    line-height: 1.5;
  }
}

.c-btn--text-icon {
  display: inline-block;
}
</style>