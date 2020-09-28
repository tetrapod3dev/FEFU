<template>
  <v-container class="my-7">
    <h2 class="text-left">멤버 인증 게시글</h2>
    <v-container>
      <v-row>
        <v-col v-for="i in 6" :key="i" cols="12" sm="6" md="4" lg="4" no-gutter>
          <v-card
            style="border: 2px solid #777777"
            contain
            class="dailyquest-item d-flex align-center justify-center"
            height="300"
          ></v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-container>
</template>

<script>
export default {};
</script>

<style></style>
