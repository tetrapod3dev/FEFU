<template>
  <div class="c-img-group">
    <p class="c-img-caption">{{ caption }}</p>
    <v-img
      class="c-img"
      :style="'height: ' + height"
      :src="src"
      aspect-ratio="1"
      lazy-src="@/assets/images/lazy-loading.jpg"
    >
      <template v-slot:placeholder>
        <lazy-loading />
      </template>
    </v-img>
  </div>
</template>

<script>
export default {
  name: "CardWithCaption",
  props: {
    caption: String,
    src: String,
    height: { type: String, default: "260px" },
  },
};
</script>

<style lang="scss" scoped>
.c-img {
  border: 2px solid black;
  border-radius: 5px;
  height: 260px;
}

.c-img-group {
  padding: 6px;

  .c-img-caption {
    position: relative;
    display: inline-block;
    border: 2px solid black;
    border-radius: 5px;
    padding: 15px 20px;
    background-color: #ffffff;
    min-width: 120px;
    font-family: "S-CoreDream-7ExtraBold";
    transition: 0.3s;
    z-index: 2;
  }
  .c-img {
    position: relative;
    margin-top: -45px;
    overflow: hidden;
    z-index: 1;
  }
}
</style>