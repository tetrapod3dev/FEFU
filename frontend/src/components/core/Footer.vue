<template>
  <v-footer id="custom-footer" :padless="true">
    <v-container>
      <v-col class="py-3"></v-col>
      <v-row>
        <v-col cols="12" sm="6" md="3" class="custom-footer-logo text-left align-self-start">
          FE For Earth
          <br />FU For Us
        </v-col>
        <v-col
          cols="12"
          sm="6"
          md="3"
          class="custom-footer-text text-left align-self-start"
          align="start"
        >
          SSAFY 3기 A402
          <br />Team. Among Earth
        </v-col>
        <v-col cols="12" sm="6" md="3" class="custom-footer-text text-left align-self-start">
          <p>권경은[팀장 / 백엔드]</p>
          <p>김현수[백엔드]</p>
          <p>박태록[프론트]</p>
          <p>박지윤[프론트]</p>
          <p>이동혁[데이터분석]</p>
        </v-col>
        <v-col
          cols="12"
          sm="6"
          md="3"
          class="custom-footer-text text-left align-self-start"
        >Copyright@{{ new Date().getFullYear() }} - FEFU</v-col>
      </v-row>
    </v-container>
  </v-footer>
</template>

<script>
export default {
  name: "CoreFooter",
};
</script>

<style lang="scss" scoped>
@font-face {
  font-family: "S-CoreDream-7ExtraBold";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/S-CoreDream-7ExtraBold.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
@import url("https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap");
@font-face {
  font-family: "NanumSquareRound";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_two@1.0/NanumSquareRound.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}

#custom-footer {
  border-top: 2px solid #000000;
  background-color: #fcfcfc;
}

.custom-footer-logo {
  font-family: "S-CoreDream-7ExtraBold";
  font-size: 24px;
  line-height: 24px;
}

.custom-footer-text {
  font-family: "Nunito", "NanumSquareRound", sans-serif;
  font-size: 16px;
  line-height: 16px;
}
</style>