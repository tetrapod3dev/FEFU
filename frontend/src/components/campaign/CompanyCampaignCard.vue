<template>
  <!-- <v-hover v-slot:default="{ hover }" open-delay="200"> -->
  <v-card class="custom-card mx-auto" max-width="400" outlined>
    <v-img
      class="campaign-img"
      height="200px"
      :src="src"
      lazy-src="@/assets/images/lazy-loading.jpg"
    >
      <!-- <span class="campaign-state">진행여부</span> -->
      <template v-slot:placeholder>
        <lazy-loading />
      </template>
    </v-img>

    <v-card-text class="text--primary text-left">
      <h3>{{ campaign.title }}</h3>
      <div>{{ campaign.org }}</div>
    </v-card-text>
  </v-card>
  <!-- </v-hover> -->
</template>

<script>
export default {
  data() {
    return {
      valueDeterminate: 50,
    };
  },
  props: ["campaign", "src"],
};
</script>

<style scoped>
.custom-card {
  border: 2px solid black;
  border-radius: 15px;
  top: 0px;
  font-family: "NanumBarunpen";
}
.custom-card:hover {
  transform: translate3d(0px, -5px, -5px);
  box-shadow: 3px 3px black;
  top: -5px;
  transition: 0.4s;
  cursor: pointer;
}

.campaign-img {
  border-bottom-right-radius: 15px;
  border-bottom-left-radius: 15px;
  position: relative;
}

.campaign-state {
  position: absolute;
  top: 0;
  right: 0;
  background-color: white;
  padding: 5px 20px;
  border: 2px solid black;
  border-radius: 15px;
}
</style>
