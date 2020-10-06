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
          sm="6"
          md="3"
          class="c-footer-text text-left align-self-start"
          align="start"
        >
          <p>SSAFY 3기 A402</p>
          <p>Team. Among Earth</p>
        </v-col>
        <v-col
          cols="10"
          sm="6"
          md="3"
          class="c-footer-text text-left align-self-start"
        >
          <p v-for="(team, index) in teams" :key="index">
            {{ team.name }}[{{ team.part }}]
            <a
              :href="gitlabUrl(team.gitlab)"
              target="_blank"
              style="text-decoration: none; color: black"
            >
              <v-icon
                style="
                  border: 1px solid #000000;
                  border-radius: 50%;
                  color: #f46a25;
                "
                >mdi-gitlab</v-icon
              >
            </a>
          </p>
        </v-col>
        <v-col
          cols="10"
          sm="6"
          md="3"
          class="c-footer-text text-left align-self-start"
        >
          <v-dialog v-model="dialog" width="600px">
            <template v-slot:activator="{ on, attrs }">
              <p>
                <a v-bind="attrs" v-on="on" @click="tab = 'terms'">회원약관</a>
                |
                <a v-bind="attrs" v-on="on" @click="tab = 'privacy-policy'">
                  개인정보처리방침
                </a>
              </p>
            </template>

            <!-- modal start -->
            <v-card style="border: 3px solid #000000">
              <v-tabs v-model="tab" color="var(--primary-color)">
                <v-tab href="#terms">
                  <v-card-title>
                    <span class="login-title">FEFU 이용 약관</span>
                  </v-card-title>
                </v-tab>
                <v-tab href="#privacy-policy">
                  <v-card-title>
                    <span class="login-title">개인정보 처리방침</span>
                  </v-card-title>
                </v-tab>
              </v-tabs>

              <v-tabs-items v-model="tab">
                <v-tab-item id="terms">
                  <v-card-text>
                    <terms />
                  </v-card-text>
                </v-tab-item>
                <v-tab-item id="privacy-policy">
                  <v-card-text>
                    <privacy-policy />
                  </v-card-text>
                </v-tab-item>
              </v-tabs-items>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn class="c-btn" text @click="dialog = false">닫기</v-btn>
              </v-card-actions>
            </v-card>
            <!-- modal end -->
          </v-dialog>
          <p>Copyright@{{ new Date().getFullYear() }} - FEFU</p>
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
import Terms from "@/components/Terms";
import PrivacyPolicy from "@/components/PrivacyPolicy";

export default {
  name: "CoreFooter",
  data() {
    return {
      tab: null,
      dialog: false,
      teams: [
        {
          name: "권경은",
          part: "팀장/백엔드",
          gitlab: "chriskwon96",
        },
        {
          name: "김현수",
          part: "백엔드",
          gitlab: "gustn16113",
        },
        {
          name: "박지윤",
          part: "프론트",
          gitlab: "bellnuite",
        },
        {
          name: "박태록",
          part: "프론트",
          gitlab: "sdf7575",
        },
        {
          name: "이동혁",
          part: "데이터분석",
          gitlab: "lee33843",
        },
      ],
    };
  },
  components: {
    Terms,
    PrivacyPolicy,
  },
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
  methods: {
    gitlabUrl(gitlab) {
      return 'https://lab.ssafy.com/' + gitlab
    }
  }
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