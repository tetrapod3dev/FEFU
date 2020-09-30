<template>
  <v-container class="my-7">
    <h2 class="text-left">멤버 인증 게시글</h2>
    <v-container>
      <v-row>
        <v-col
          v-for="(post, index) in posts"
          :key="index"
          cols="12"
          sm="6"
          md="4"
          lg="4"
          no-gutter
        >
          <v-card
            style="border: 2px solid #777777"
            contain
            class="dailyquest-item d-flex align-center justify-center"
            ><v-img
              v-if="post.photo"
              :src="imageSrc(post.photo)"
              class="white--text align-end"
              height="200px"
            ></v-img
            ><v-img
              v-else
              :src="require('@/assets/images/noimage.jpg')"
              class="white--text align-end"
              height="200px"
            ></v-img>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-container>
</template>

<script>
import axios from "axios";
import SERVER from "@/api/api";

export default {
  props: ["campaignNo"],
  data() {
    return {
      pagination: {
        curPage: 1,
        endPage: 0,
        next: false,
        perPageNum: 0,
        displayPageNum: 0,
        prev: false,
        startIndex: 0,
        startPage: 0,
        totalCount: 0,
      },
      posts: [],
    };
  },
  created() {
    this.getProof();
  },
  methods: {
    imageSrc(filename) {
      return SERVER.IMAGE_URL + filename;
    },
    getProof() {
      axios
        .get(
          SERVER.URL +
            SERVER.ROUTES.campaigns.proof +
            "/" +
            this.campaignNo +
            "/1"
        )
        .then((res) => {
          console.log(res);
          this.pagination = res.data.page;
          this.posts = res.data.list;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style></style>
