<template>
  <v-hover v-slot:default="{ hover }" open-delay="200">
    <v-card darkclass="mx-auto" max-width="400" outlined :elevation="hover ? 10 : 0">
      <v-img height="200px" src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"></v-img>
      <v-card-text class="text--primary text-left">
        <h3>캠페인 제목</h3>
        <div>주최</div>
        <div class="mt-2">
          <v-progress-linear v-model="valueDeterminate" color="indigo darken-2"></v-progress-linear>
          <div class="mt-1">인증률 %</div>
        </div>
      </v-card-text>
    </v-card>
  </v-hover>
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

<style>
</style>