<template>
  <div class="section">
    <div>{{ selected }}</div>
    <v-card max-width="900" class="mx-auto px-3" flat>
      <v-container class="pa-1">
        <v-item-group v-model="selected" multiple>
          <v-row>
            <v-col
              v-for="(item, idex) in items"
              :key="idex"
              cols="6"
              sm="6"
              md="3"
              lg="3"
              no-gutter
            >
              <v-item v-slot:default="{ active, toggle }">
                <v-hover v-slot:default="{ hover }" open-delay="200">
                  <v-card
                    :color="active ? 'primary' : ''"
                    :img="active ? null : item.src"
                    contain
                    class="dailyquest-item d-flex align-center justify-center"
                    height="200"
                  >
                    <!-- <v-scroll-y-transition> -->
                    <div v-if="active" class="display-1 flex-grow-1 text-center">완료</div>
                    <div v-else>
                      <div v-if="hover">
                        <div>{{item.name}}</div>
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
          name: "카테고리",
          content: "내용",
          src: require("@/assets/dailyquest/01-ecology.png"),
        },
        {
          id: 2,
          name: "카테고리",
          content: "내용",
          src: require("@/assets/dailyquest/05-water hourglass.png"),
        },
        {
          id: 3,
          name: "카테고리",
          content: "내용",
          src: require("@/assets/dailyquest/10-bag.png"),
        },
        {
          id: 4,
          name: "카테고리",
          content: "내용",
          src: require("@/assets/dailyquest/16-reuse bag.png"),
        },
        {
          id: 5,
          name: "카테고리",
          content: "내용",
          src: require("@/assets/dailyquest/15-eco fuel.png"),
        },
        {
          id: 6,
          name: "카테고리",
          content: "내용",
          src: require("@/assets/dailyquest/24-solar.png"),
        },
        {
          id: 7,
          name: "카테고리",
          content: "내용",
          src: require("@/assets/dailyquest/21-recycle.png"),
        },
        {
          id: 8,
          name: "카테고리",
          content: "내용",
          src: require("@/assets/dailyquest/22-eco fuel.png"),
        },
        {
          id: 9,
          name: "카테고리",
          content: "내용",
          src: require("@/assets/dailyquest/20-reuse.png"),
        },
        {
          id: 10,
          name: "카테고리",
          content: "내용",
          src: require("@/assets/dailyquest/19-bicycle.png"),
        },
        {
          id: 11,
          name: "카테고리",
          content: "내용",
          src: require("@/assets/dailyquest/09-water.png"),
        },
        {
          id: 12,
          name: "카테고리",
          content: "내용",
          src: require("@/assets/dailyquest/26-paper reuse.png"),
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

.dailyquest-item {
  border: 3px solid black;
  border-radius: 15px;
}
</style>