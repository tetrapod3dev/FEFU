<template>
  <v-card darkclass="mx-auto" max-width="400" outlined class="custom-card">
    <v-img class="campaign-img" height="200px" :src="src"></v-img>

    <v-card-text class="text--primary text-left">
      <h3>{{ campaign.title }}</h3>
      <div>{{ campaign.org }}</div>
      <div class="mt-2">
        <v-progress-linear
          class="custom-progress"
          v-model="campaign.valueDeterminate"
          color="#37CDC2"
        ></v-progress-linear>
        <div class="mt-1">{{ campaign.valueDeterminate }}%</div>
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
  props: ["campaign", "src"],
};
</script>

<style scoped>
.custom-card {
  border: 2px solid black;
  border-radius: 15px;
  font-family: "NanumBarunpen";
}

.custom-card:hover {
  transform: translate3d(0px, -5px, -5px);
  box-shadow: 3px 3px black;
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