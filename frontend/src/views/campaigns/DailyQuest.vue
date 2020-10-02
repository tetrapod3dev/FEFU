<template>
  <div class="section">
    <v-container>
      <div class="campaign-title">
        <h1>일일퀘스트</h1>
      </div>
      <v-card max-width="900" class="mx-auto px-3" flat>
        <v-container class="pa-1">
          <v-item-group multiple>
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
                <v-item>
                  <v-hover v-slot:default="{ hover }" open-delay="200">
                    <v-card
                      :color="completed[idx-1] ? 'primary' : ''"
                      :img="completed[idx-1] ? null : images[idx-1]"
                      contain
                      class="dailyquest-item d-flex align-center justify-center"
                      height="200"
                    >
                      <!-- <v-scroll-y-transition> -->
                      <div
                        v-if="completed[idx-1]"
                        class="display-1 flex-grow-1 text-center"
                      >
                        완료
                      </div>
                      <div v-else>
                        <div v-if="hover">
                          <div>{{ dailyQuestInfo[idx-1].title }}</div>
                          <div>{{ dailyQuestInfo[idx-1].content }}</div>
                          <v-btn @click="actNow(idx)" color="primary">act now</v-btn>
                        </div>
                      </div>
                      <!-- </v-scroll-y-transition> -->
                    </v-card>
                  </v-hover>
                </v-item>
              </v-col>
            </v-row>
          </v-item-group>
        </v-container>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import axios from 'axios';
import SERVER from '@/api/api';

import { mapGetters} from 'vuex';

export default {
  props: {
    dailyQuestInfo: Array,
  },
  data() {
    return {
      // DB에 각 항목별 이미지가 없어서 그냥 별도의 이미지를 index에 대해 매칭시켜주는 방법으로 사용했습니다. (기존이미지 사용)
      images: [
        require("@/assets/dailyquest/01-ecology.png"),
        require("@/assets/dailyquest/05-water hourglass.png"),
        require("@/assets/dailyquest/10-bag.png"),
        require("@/assets/dailyquest/16-reuse bag.png"),
        require("@/assets/dailyquest/15-eco fuel.png"),
        require("@/assets/dailyquest/24-solar.png"),
        require("@/assets/dailyquest/21-recycle.png"),
        require("@/assets/dailyquest/22-eco fuel.png"),
        require("@/assets/dailyquest/20-reuse.png"),
        require("@/assets/dailyquest/19-bicycle.png"),
        require("@/assets/dailyquest/09-water.png"),
        require("@/assets/dailyquest/26-paper reuse.png")
      ],
      // 현재는 completed가 모두 false로 초기화되는데, 이걸 나중에 유저별 완료현황으로 만들어줘야됩니다.
      completed: [false, false, false, false, false, false, false, false, false, false, false, false],
    };
  },
  computed: {
    ...mapGetters("accounts", ["config"])
  },
  methods: {
    actNow(idx) {
    const self = this
    let configs = {
      headers: {
        Authorization: this.config,
      },
    };
    let body = {"quest_no": idx};
    axios
      .post(SERVER.URL + SERVER.ROUTES.campaigns.dailyQuest, body, configs)
      .then(() => {
        self.completed[idx-1] = true
        // 완료되면 해당 항목의 completed를 true로 바꿔서 완료 표시로 바뀌도록 해줍니다.
      })
      .catch(err => console.log(err))
    }
  }
};
</script>

<style scoped>
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
</style>