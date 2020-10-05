<template>
  <v-container>
    <div>
      <h1 class="campaign-title text-left">일일퀘스트</h1>
    </div>
    <v-container v-if="isValid">
      <v-row>
        <v-col
          v-for="idx in 12"
          :key="idx"
          cols="6"
          sm="6"
          md="3"
          lg="3"
          no-gutter
        >
          <!-- <v-hover v-slot:default="{ hover }" open-delay="200">
          <v-card
            :color="completed[idx - 1] ? 'primary' : ''"
            :img="completed[idx - 1] ? null : images[idx - 1]"
            contain
            class="dailyquest-item d-flex align-center justify-center"
            :height="cardHeight"
          > -->
          <!-- <v-scroll-y-transition> -->
          <!-- <div
              v-if="completed[idx - 1]"
              class="display-1 flex-grow-1 text-center"
            >
              완료
            </div>
            <div v-else>
              <div v-if="hover">
                <div>{{ dailyQuestInfo[idx - 1].title }}</div>
                <div>{{ dailyQuestInfo[idx - 1].content }}</div>
                <v-btn @click="actNow(idx)" color="primary">act now</v-btn>
              </div>
            </div> -->
          <!-- </v-scroll-y-transition> -->
          <!-- </v-card>
        </v-hover> -->

          <v-dialog
            v-model="dialogs[dailyQuestInfo[idx - 1].no]"
            persistent
            max-width="600px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-card
                :img="getCompleted(idx - 1)"
                contain
                class="dailyquest-item d-flex align-center justify-center"
                :height="cardHeight"
                v-bind="attrs"
                v-on="on"
              ></v-card>
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">{{
                  dailyQuestInfo[idx - 1].title
                }}</span>
              </v-card-title>
              <v-card-text class="py-0">
                <v-container class="pb-0">
                  <v-row>
                    <v-col cols="12" class="py-12">
                      {{ dailyQuestInfo[idx - 1].description }}
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>
              <v-card-actions class="px-5">
                <v-spacer></v-spacer>
                <v-btn
                  class="custom-btn"
                  text
                  @click="$set(dialogs, dailyQuestInfo[idx - 1].no, false)"
                >
                  닫기
                </v-btn>
                <v-btn
                  v-if="!completed[idx - 1]"
                  class="custom-btn"
                  text
                  @click="actNow(idx)"
                >
                  완료
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-col>
      </v-row>
    </v-container>
    <v-container v-else>
      <div>
        😥 로그인을 하셔야 이용하실 수 있는 서비스입니다. <br />
        매일매일 퀘스트를 진행하며 지구를 지키고 경험치를 쌓아 매니저가
        되어보세요!
      </div>
      <v-row>
        <v-col>
          <router-link
            tag="a"
            :to="{ name: 'LoginView' }"
            class="c-btn--text"
            :class="'c-btn--text-' + $vuetify.breakpoint.name"
          >
            로그인하러 가기
            <v-img
              style="cursor: pointer; margin-top: 3px"
              :width="$vuetify.breakpoint.smAndDown ? 15 : 17"
              :height="$vuetify.breakpoint.smAndDown ? 15 : 17"
              class="c-btn--text-icon"
              contain
              :src="require('@/assets/illust/arrow-right.svg')"
            />
          </router-link>
        </v-col>
      </v-row>
    </v-container>
  </v-container>
</template>

<script>
import axios from "axios";
import SERVER from "@/api/api";

import { mapGetters } from "vuex";

export default {
  props: {
    dailyQuestInfo: Array,
    isValid: Boolean,
    completed: Array,
  },
  data() {
    return {
      dialogs: {},
      // DB에 각 항목별 이미지가 없어서 그냥 별도의 이미지를 index에 대해 매칭시켜주는 방법으로 사용했습니다. (기존이미지 사용)
      images: [
        require("@/assets/dailyquest/09-water.png"),
        require("@/assets/dailyquest/12-save energy.png"),
        require("@/assets/dailyquest/01-ecology.png"),
        require("@/assets/dailyquest/27-global warming.png"),
        require("@/assets/dailyquest/04-eco light.png"),
        require("@/assets/dailyquest/25-wastewater.png"),
        require("@/assets/dailyquest/23-garbage truck.png"),
        require("@/assets/dailyquest/20-reuse.png"),
        require("@/assets/dailyquest/16-reuse bag.png"),
        require("@/assets/dailyquest/21-recycle.png"),
        require("@/assets/dailyquest/31-food.png"),
        require("@/assets/dailyquest/19-bicycle.png"),
      ],
      outlineImages: [
        require("@/assets/dailyquest/outline/09-water.png"),
        require("@/assets/dailyquest/outline/12-save energy.png"),
        require("@/assets/dailyquest/outline/01-ecology.png"),
        require("@/assets/dailyquest/outline/27-global warming.png"),
        require("@/assets/dailyquest/outline/04-eco light.png"),
        require("@/assets/dailyquest/outline/25-wastewater.png"),
        require("@/assets/dailyquest/outline/23-garbage truck.png"),
        require("@/assets/dailyquest/outline/20-reuse.png"),
        require("@/assets/dailyquest/outline/16-reuse bag.png"),
        require("@/assets/dailyquest/outline/21-recycle.png"),
        require("@/assets/dailyquest/outline/31-food.png"),
        require("@/assets/dailyquest/outline/19-bicycle.png"),
      ],
      // 현재는 completed가 모두 false로 초기화되는데, 이걸 나중에 유저별 완료현황으로 만들어줘야됩니다.
    };
  },
  computed: {
    ...mapGetters("accounts", ["config", "isLoggedIn"]),
    cardHeight() {
      let resultWidth;
      switch (this.$vuetify.breakpoint.name) {
        case "xs":
          resultWidth = 220;
          break;
        case "sm":
          resultWidth = 220;
          break;
        case "md":
          resultWidth = 220;
          break;
        case "lg":
          resultWidth = 280;
          break;
        case "xl":
          resultWidth = 280;
          break;
      }
      return resultWidth;
    },
  },
  methods: {
    getCompleted(idx) {
      return this.completed[idx] ? this.images[idx] : this.outlineImages[idx];
    },
    actNow(idx) {
      this.$set(this.dialogs, this.dailyQuestInfo[idx - 1].no, false);
      let configs = {
        headers: {
          Authorization: this.config,
        },
      };
      let body = { quest_no: idx };
      axios
        .post(SERVER.URL + SERVER.ROUTES.campaigns.dailyQuest, body, configs)
        .then(() => {
          this.$set(this.completed, idx - 1, true);
          // 완료되면 해당 항목의 completed를 true로 바꿔서 완료 표시로 바뀌도록 해줍니다.
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style lang="scss" scoped>
.section {
  margin-top: 30px;
  margin-bottom: 100px;
  background: #fcfcfc;
}

.campaign-title {
  margin: 30px 0;
  font-family: "NanumBarunpen";
}

.dailyquest-item {
  border: 3px solid black;
  border-radius: 15px;
}

.c-btn--text {
  display: inline-block;
  text-decoration: none;
  border-bottom: 2px solid #000000;
  padding: 2px 0;
  font-family: "Nunito", "NanumSquareRound", sans-serif;
  font-size: 16px;
  color: #000000;
  transition: 0.3s;

  &-md,
  &-lg,
  &-xl {
    font-size: 18px;
    line-height: 1.5;
  }
}

.c-btn--text-icon {
  display: inline-block;
}
</style>