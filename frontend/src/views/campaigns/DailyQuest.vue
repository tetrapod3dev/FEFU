<template>
  <div class="section">
    <div>{{ selected }}</div>
    <v-card max-width="900" class="mx-auto px-3">
      <v-container class="pa-1">
        <v-item-group v-model="selected" multiple>
          <v-row>
            <v-col v-for="(item, idex) in items" :key="idex" cols="12" sm="6" md="3" lg="3">
              <v-item v-slot:default="{ active, toggle }">
                <v-hover v-slot:default="{ hover }" open-delay="200">
                  <v-card
                    :color="active ? 'primary' : 'grey'"
                    :img="active ? null : item.src"
                    class="d-flex align-center justify-center"
                    height="200"
                  >
                    <!-- <v-scroll-y-transition> -->
                    <div v-if="active" class="display-1 flex-grow-1 text-center">완료</div>
                    <div v-else>
                      <div v-if="!hover">{{item.name}}</div>
                      <div v-else>
                        <div>{{item.content}}</div>
                        <v-btn @click="toggle" color="primary">act now</v-btn>
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
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [
        {
          id: 1,
          name: "물",
          content: "양치할 땐 양치컵",
          src: require("@/assets/dailyquest/water.jpg"),
        },
        {
          id: 2,
          name: "콘센트 뽑기",
          content: "나가기 전 콘센트 확인",
          src: require("@/assets/dailyquest/electronic.jpg"),
        },
        {
          id: 3,
          name: "전기",
          content: "냉방 이용을 1시간 줄이기",
          src: require("@/assets/logo.png"),
        },
        {
          id: 4,
          name: "장바구니 이용",
          content: "장 볼 땐 장바구니",
          src: require("@/assets/logo.png"),
        },
        {
          id: 5,
          name: "텀블러 사용",
          content: "텀블러로 페트병 사용 줄이기",
          src: require("@/assets/logo.png"),
        },
        {
          id: 6,
          name: "통근길엔",
          content: "버스 또는 전철, 자전거 이용하기",
          src: require("@/assets/logo.png"),
        },
        {
          id: 7,
          name: "물",
          content: "양치할 땐 양치컵",
          src: require("@/assets/logo.png"),
        },
        {
          id: 8,
          name: "물",
          content: "양치할 땐 양치컵",
          src: require("@/assets/logo.png"),
        },
        {
          id: 9,
          name: "물",
          content: "양치할 땐 양치컵",
          src: require("@/assets/logo.png"),
        },
        {
          id: 10,
          name: "물",
          content: "양치할 땐 양치컵",
          src: require("@/assets/logo.png"),
        },
        {
          id: 11,
          name: "물",
          content: "양치할 땐 양치컵",
          src: require("@/assets/logo.png"),
        },
        {
          id: 12,
          name: "물",
          content: "양치할 땐 양치컵",
          src: require("@/assets/logo.png"),
        },
      ],
      selected: [],
    };
  },
  methods: {
    addDoneList() {
      localStorage.setItem(this.selected, this.selected);
    },
  },
};
</script>

<style scoped>
.section {
  margin-top: 30px;
  margin-bottom: 70px;
}
</style>