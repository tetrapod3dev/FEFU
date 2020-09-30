<template>
  <div id="campaign-list">
    <v-col class="py-12"></v-col>
    <v-container>
      <v-row>
        <v-col cols="12" sm="3">
          <!-- 사이드바 -->

          <div>
            <v-img
              class="custom-header-img mr-auto ml-auto"
              height="200px"
              width="200px"
              :src="imageSrc('')"
              lazy-src="@/assets/images/lazy-loading.jpg"
            >
              <template v-slot:placeholder>
                <v-row class="fill-height ma-0" align="center" justify="center">
                  <v-progress-circular
                    indeterminate
                    color="grey lighten-5"
                  ></v-progress-circular>
                </v-row>
              </template>
            </v-img>

            <v-list class="custom-list">
              <v-list-item class="custom-list-item">
                <v-list-item-content
                  >test2 test2
                  <v-list-item-title></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-list-item class="custom-list-item">
                <v-list-item-content>
                  <v-list-item-title>참여 캠페인</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-list-item class="custom-list-item">
                <v-list-item-content>
                  <v-list-item-title>등록 캠페인</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-list-item class="custom-list-item">
                <v-list-item-content>
                  <v-list-item-title>등록 물건</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-list-item class="custom-list-item">
                <v-list-item-content>
                  <v-list-item-title>회원정보수정</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </div>

          <button class="custom-make-btn">회원 탈퇴</button>
        </v-col>

        <v-col cols="12" md="9" class="pt-0">
          <v-container justify="start">
            <div class="campaign-welcome">
              <span class="campaign-title">등록 캠페인</span>
            </div>

            <div class="campaign-info d-flex flex-column">
              <router-view />
            </div>
          </v-container>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import SERVER from "@/api/api";

export default {
  name: "Mypage",
  created() {},
  data() {
    return {
      isJoined: false,
      listColorName: [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "purple",
      ],
      userinfo: {
        no: 16,
        username: "sdf7575@naver.com",
        password: null,
        nickname: "박태록",
        age: 28,
        gender: "남자",
        ecoPoint: 0,
        exp: 0,
        profileImage: null,
      },
    };
  },
  computed: {
    ...mapGetters("accounts", ["config"]),
  },
  methods: {
    imageSrc(filename) {
      return SERVER.IMAGE_URL + filename;
    },
  },
};
</script>

<style lang="scss" scoped>
.custom-header-img {
  border: 2px solid black;
  border-radius: 50%;
}

.campaign-welcome {
  border: 2px solid black;
  border-radius: 5px;
  padding: 10px 20px;
  margin: 10px 0;
  text-align: start;
}

.campaign-title {
  font-size: 1.5rem;
  font-family: "NanumBarunpen";
}

.campaign-info {
  font-family: "NanumBarunpen";
  border: 2px solid black;
  border-radius: 5px;
  padding: 10px 20px;
  margin: 10px 0;
}

.campaign-info-list {
  margin: 10px 0;
  background-color: rgba(55, 205, 194, 0.09);
  border-radius: 10px;
  font-family: "S-CoreDream-7ExtraBold";
}

.custom-white {
  background: var(--white-color);
}

.custom-make-btn {
  font-family: "S-CoreDream-7ExtraBold";
  font-size: 1rem;
  width: 100%;
  height: 48px;
  margin-top: 20px;
  background-color: var(--primary-color);
  border: 2px solid black;
  border-radius: 10px;
  text-align: center;
}

.capmaign-info {
  font-family: "NanumBarunpen";
}

.custom-list {
  margin-top: 20px;
  font-family: "S-CoreDream-7ExtraBold";
}

.campaign-info-list {
  font-family: "S-CoreDream-7ExtraBold";
  border: 2px solid black;
  border-radius: 10px;
  padding: 5px 0;
}

.custom-list-item {
  border: 2px solid black;
  &:first-child {
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
  }
  &:last-child {
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
  }

  &:not(:last-child) {
    // border-bottom: 2px solid black;
    margin-bottom: -2px;
  }

  &-red.v-list-group--active,
  &-red:hover {
    background: #cf6a87;
  }

  &-orange.v-list-group--active,
  &-orange:hover {
    background: #f19066;
  }

  &-yellow.v-list-group--active,
  &-yellow:hover {
    background: #fdcb6e;
  }

  &-green.v-list-group--active,
  &-green:hover {
    background: #b8e994;
  }

  &-blue.v-list-group--active,
  &-blue:hover {
    background: #82ccdd;
  }

  &-indigo.v-list-group--active,
  &-indigo:hover {
    background: #60a3bc;
  }

  &-purple.v-list-group--active,
  &-purple:hover {
    background: #786fa6;
  }
}
</style>
