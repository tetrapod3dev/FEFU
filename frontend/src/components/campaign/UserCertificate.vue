<template>
  <v-container class="my-7">
    <h2 class="text-left">멤버별 인증현황</h2>
    <v-row v-for="i in 3" :key="i">
      <v-col cols="1">
        <v-avatar>
          <img src="https://cdn.vuetifyjs.com/images/john.jpg" alt="John" />
        </v-avatar>
      </v-col>
      <v-col cols="10">
        <p class="text-left mb-0">박싸피</p>
        <v-progress-linear
          v-model="valueDeterminate"
          color="indigo darken-2"
          height="15"
        ></v-progress-linear>
      </v-col>
      <v-col cols="1">
        <p class="mb-0">{{ valueDeterminate }} %</p>
        <p class="mb-0">90일</p>
      </v-col>
    </v-row>
  </v-container>
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

<style></style>
