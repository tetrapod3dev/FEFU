<template>
  <div class="custom-img-group">
    <p class="custom-img-caption">{{caption}}</p>
    <v-img class="custom-img" :src="src" />
  </div>
</template>

<script>
export default {
  name: "CardWithCaption",
  props: ["caption", "src"],
};
</script>

<style lang="scss" scoped>
.custom-img {
  border: 2px solid black;
  border-radius: 5px;
  height: 260px;
}

.custom-img-group {
  padding: 6px;

  .custom-img-caption {
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
  .custom-img {
    position: relative;
    margin-top: -45px;
    overflow: hidden;
    z-index: 1;
  }
}
</style>