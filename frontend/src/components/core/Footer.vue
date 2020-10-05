<template>
  <v-footer class="c-footer" :padless="true">
    <v-container>
      <v-col class="py-3"></v-col>
      <v-row justify="center">
        <v-col cols="10" sm="6" md="3" class="text-left align-self-start">
          <img
            :src="require('@/assets/images/footerlogo.png')"
            class="ml-auto"
            :style="'height: 64px;width: 180px; cursor: pointer;'"
            @click="
              moveToPage({
                name: 'Home',
              })
            "
          />
        </v-col>
        <v-col
          cols="10"
          sm="3"
          md="3"
          class="c-footer-text text-left align-self-start"
          align="start"
        >
          <p>SSAFY 3기 A402</p>
          <p>Team. Among Earth</p>
        </v-col>
        <v-col
          cols="10"
          sm="3"
          md="3"
          class="c-footer-text text-left align-self-start"
        >
          <p>권경은[팀장 / 백엔드]</p>
          <p>김현수[백엔드]</p>
          <p>박태록[프론트]</p>
          <p>박지윤[프론트]</p>
          <p>이동혁[데이터분석]</p>
        </v-col>
        <v-col
          cols="10"
          sm="3"
          md="3"
          class="c-footer-text text-left align-self-start"
          ><p>Copyright@{{ new Date().getFullYear() }} - FEFU</p>
          <p>
            With
            <a
              href="http://edu.ssafy.com"
              style="color: #000000; text-decoration: none"
              >SSAFY</a
            >
          </p></v-col
        >
      </v-row>
    </v-container>
  </v-footer>
</template>

<script>
export default {
  name: "CoreFooter",

  moveToPage(_url) {
    this.$router
      .push(_url)
      .then(() => {
        location.reload();
      })
      .catch((error) => {
        if (error.name === "NavigationDuplicated") {
          location.reload();
        }
      });
  },
};
</script>

<style lang="scss" scoped>
.c-footer {
  border-top: 2px solid #000000;
  background-color: #fcfcfc;
  &-text {
    font-family: "Nunito", "NanumSquareRound", sans-serif;
    font-size: 16px;
    line-height: 16px;
  }
}
</style>