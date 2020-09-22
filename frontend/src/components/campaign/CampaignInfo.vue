<template>
  <v-container justify="start">
    <div class="campaign-manager d-flex">
      <v-avatar color="teal" size="60"></v-avatar>
      <div class="d-flex flex-column justify-center text-left ml-3">
        <span class="manager-badge">매니저</span>
        <span class="mb-0">캠페인</span>
      </div>
    </div>
    <div class="campaign-info d-flex flex-column">
      <p class="text-left">캠페인 상세내용</p>
      <v-list class="custom-list">
        <v-row>
          <v-list-item class="custom-list-item" v-for="(item, i) in items" :key="i">
            <v-col cols="2">
              <v-list-item-content>
                <v-list-item-title v-text="item.title"></v-list-item-title>
              </v-list-item-content>
            </v-col>
            <v-col cols="10">
              <v-list-item-content class="text-left">
                <v-list-item-title v-text="item.text"></v-list-item-title>
              </v-list-item-content>
            </v-col>
          </v-list-item>
        </v-row>
      </v-list>
    </div>
    <v-divider class="my-5"></v-divider>
    <v-chip-group>
      <v-chip class="ma-2" color="#37cdc2" large outlined v-for="tag in tags" :key="tag">{{ tag }}</v-chip>
    </v-chip-group>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    items: [
      {
        title: "인증미션",
        text: "안쓰는 콘센트 뽑기",
      },
      {
        title: "인증방법",
        text: "아무것도 안꼽혀있는 멀티탭 사진 찍어 올리기",
      },
      {
        title: "인증시간",
        text: "출근/등교 시간",
      },
      {
        title: "목표인원",
        text: "30",
      },
      {
        title: "멤버조건",
        text: "환경보호에 관심있는 누구나",
      },
    ],
    tags: [
      "전기절약",
      "환경보호",
      "매일캠페인",
      "같이해요",
      "하루한장",
      "사진인증",
    ],
    model: 1,
  }),
};
</script>

<style scoped>
.campaign-manager {
  margin: 20px 0;
}

.campaign-info {
  margin: 40px 0;
}

.manager-badge {
  border: 1px solid var(--primary-color);
  color: var(--primary-color);
  border-radius: 15px;
  padding: 2px 5px;
  margin-bottom: 3px;
  font-size: 0.8rem;
}

.custom-list {
  background: #fcfcfc;
}

/* .custom-list-item {
  background: #ececec;
} */
</style>