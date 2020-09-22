<template>
  <v-card darkclass="mx-auto" max-width="400" outlined class="custom-card">
    <v-img
      class="campaign-img"
      height="200px"
      src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
    ></v-img>

    <v-card-text class="text--primary text-left">
      <h3>캠페인 제목</h3>
      <div>주최</div>
      <div class="mt-2">
        <v-progress-linear v-model="valueDeterminate" color="#23EFB8"></v-progress-linear>
        <div class="mt-1">인증률 %</div>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      valueDeterminate: 50,
    };
  },
};
</script>

<style scoped>
.custom-card {
  border: 2px solid black;
  border-radius: 15px;
  top: 0px;
}

.custom-card:hover {
  box-shadow: 3px 3px black;
  top: -10px;
  transition: 0.4s;
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