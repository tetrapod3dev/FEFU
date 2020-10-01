<template>
  <v-container class="my-7">
    <h2 class="text-left">멤버별 인증현황</h2>
    <v-row v-for="(user, index) in userList" :key="index">
      <v-col cols="1">
        <v-avatar>
          <img src="https://cdn.vuetifyjs.com/images/john.jpg" alt="John" />
        </v-avatar>
      </v-col>
      <v-col cols="10">
        <p class="text-left mb-0">{{ user.writer }}</p>
        <v-progress-linear
          v-model="user.progress"
          color="indigo darken-2"
          height="15"
        ></v-progress-linear>
      </v-col>
      <v-col cols="1">
        <p class="mb-0">{{ user.progress }}일</p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mixinGetUserInfo } from "@/components/mixin/mixinGetUserInfo";

export default {
  mixins: [mixinGetUserInfo],
  data() {
    return {
      valueDeterminate: 50,
    };
  },
  props: ["userList"],
  computed: {
    getPercentValueDeterminate(count) {
      return count * 100;
    },
    // getUserImage(username) {
    //   let imgSrc = "";
    //   this.getInfo(username)
    //     .then((res) => {
    //       console.log(res);
    //     })
    //     .catch((err) => {
    //       console.log(err.response);
    //     });

    //   return imgSrc;
    // },
  },
};
</script>

<style></style>
