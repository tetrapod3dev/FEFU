<template>
  <v-footer :padless="true">
    <v-card flat tile width="100%" class="secondary white--text text-center">
      <v-card-text>
        <v-btn class="mx-4 white--text" icon>
          <v-icon size="24px">mdi-home</v-icon>
        </v-btn>
        <v-btn class="mx-4 white--text" icon>
          <v-icon size="24px">mdi-email</v-icon>
        </v-btn>
        <v-btn class="mx-4 white--text" icon>
          <v-icon size="24px">mdi-calendar</v-icon>
        </v-btn>
        <v-btn class="mx-4 white--text" icon>
          <v-icon size="24px">mdi-delete</v-icon>
        </v-btn>
      </v-card-text>

      <v-card-text class="white--text pt-0">Footer 텍스트</v-card-text>

      <v-divider></v-divider>

      <v-card-text class="white--text">
        {{ new Date().getFullYear() }} —
        <strong>사이트 이름</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
export default {};
</script>

<style>
</style>