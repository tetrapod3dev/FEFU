<template>
  <v-hover v-slot:default="{ hover }" open-delay="200">
    <v-card
      darkclass="mx-auto"
      max-width="400"
      outlined
      :elevation="hover ? 10 : 0"
      class="custom-card"
    >
      <v-img
        class="campaign-img"
        height="200px"
        src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
      >
        <span class="campaign-state">진행여부</span>
      </v-img>

      <v-card-text class="text--primary text-left">
        <h3>캠페인 제목</h3>
        <div>주최</div>
        <div class="mt-2">
          <v-progress-linear v-model="valueDeterminate" color="#5AFF9A"></v-progress-linear>
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

<style scoped>
.custom-card {
  border: 2px solid black;
  border-radius: 15px;
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