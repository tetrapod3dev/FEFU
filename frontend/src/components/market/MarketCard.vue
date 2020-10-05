<template>
  <v-card
    class="c-card ma-4"
    :height="1.6 * cardWidth"
    :width="cardWidth"
    :to="{
      name: 'MarketDetailView',
      params: { productNo: product.no },
    }"
  >
    <v-img
      :height="1.1 * cardWidth"
      :src="imageSrc(product.photo)"
      lazy-src="@/assets/images/lazy-loading.jpg"
    >
      <template v-slot:placeholder>
        <lazy-loading />
      </template>
    </v-img>

    <v-card-text class="text-left text--primary">
      <div class="c-product__title my-1">
        {{ product.title }}
      </div>
      <div class="c-product__price ml-1 mt-2">
        {{ commaNumber(product.price) }}원
      </div>
      <div class="c-product__eco ml-1 mt-1">
        {{ commaNumber(product.eco_point) }}p
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
import SERVER from "@/api/api";

export default {
  props: ["product"],
  computed: {
    cardWidth() {
      let resultWidth;
      switch (this.$vuetify.breakpoint.name) {
        case "xs":
          resultWidth = 220;
          break;
        case "sm":
          resultWidth = 220;
          break;
        case "md":
          resultWidth = 220;
          break;
        case "lg":
          resultWidth = 280;
          break;
        case "xl":
          resultWidth = 280;
          break;
      }
      return resultWidth;
    },
  },
  methods: {
    commaNumber(number) {
      if (number) {
        return number.toLocaleString();
      }
      return 0;
    },
    imageSrc(filename) {
      return SERVER.IMAGE_URL + filename;
    },
  },
};
</script>

<style lang="scss" scoped>
.c-card {
  border: 2px solid black;
  border-radius: 15px;
  font-family: "NanumBarunpen";

  &:hover {
    transform: translate3d(0px, -5px, -5px);
    box-shadow: 3px 3px black;
    transition: 0.4s;
    cursor: pointer;
  }
}

.c-txt--overflow {
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
}
.c-product__title {
  @extend .c-txt--overflow;
  font-size: 24px;
  color: #000000;
}
.c-product__price {
  @extend .c-txt--overflow;
  font-size: 18px;
  color: #000000;
}
.c-product__eco {
  @extend .c-txt--overflow;
  font-size: 16px;
  color: var(--primary-color);
}
</style>