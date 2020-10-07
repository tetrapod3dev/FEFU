<template>
  <v-row justify="center">
    <v-col cols="12" xl="8">
      <v-col class="py-10"></v-col>
      <v-container>
        <v-row>
          <v-col cols="12" md="3">
            <!-- 사이드바 -->
            <profile-photo :userinfo="userinfo" />

            <div>
              <div class="c-status py-6" style="background-color: #fcfcfc">
                <v-tooltip bottom>
                  <template v-slot:activator="{ on, attrs }">
                    <span class="mr-4" v-bind="attrs" v-on="on">
                      🧡 {{ userinfo.exp }}</span
                    >
                  </template>
                  <span>경험치</span>
                </v-tooltip>

                <v-tooltip bottom>
                  <template v-slot:activator="{ on, attrs }">
                    <span v-bind="attrs" v-on="on">
                      💚 {{ userinfo.ecoPoint }}
                    </span>
                  </template>
                  <span>에코포인트</span>
                </v-tooltip>
              </div>

              <v-list class="c-list">
                <v-list-item :to="{ name: 'MypageInfo' }" class="c-list-item">
                  <v-list-item-content>
                    <v-list-item-title>내정보</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item
                  :to="{ name: 'MypageEcoPoint' }"
                  class="c-list-item"
                >
                  <v-list-item-content>
                    <v-list-item-title>에코포인트 내역</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item
                  :to="{ name: 'MypageListCampaignJoin' }"
                  class="c-list-item"
                >
                  <v-list-item-content>
                    <v-list-item-title>참여 캠페인</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item
                  :to="{ name: 'MypageListCampaignAdmin' }"
                  class="c-list-item"
                >
                  <v-list-item-content>
                    <v-list-item-title>등록 캠페인</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item
                  :to="{ name: 'MypageListProduct' }"
                  class="c-list-item"
                >
                  <v-list-item-content>
                    <v-list-item-title>등록 물건</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item
                  :to="{ name: 'MypageUpdatePwd' }"
                  class="c-list-item"
                >
                  <v-list-item-content>
                    <v-list-item-title>비밀번호변경</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </div>
          </v-col>

          <v-col cols="12" md="9" class="pt-3">
            <v-col
              v-if="$vuetify.breakpoint.mdAndUp"
              cols="12"
              class="my-16 py-10"
            ></v-col>
            <router-view />
          </v-col>
        </v-row>
      </v-container>
    </v-col>
  </v-row>
</template>

<script>
import { mixinGetUserInfo } from "@/components/mixin/mixinGetUserInfo";
import { mapGetters } from "vuex";

import ProfilePhoto from "@/components/accounts/ProfilePhoto.vue";

export default {
  name: "Mypage",
  mixins: [mixinGetUserInfo],
  data() {
    return {
      isShowIcon: false,
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
        no: 0,
        username: "",
        password: null,
        nickname: "",
        age: 0,
        gender: "남자",
        ecoPoint: 0,
        exp: 0,
        profileImage: "",
      },
    };
  },
  components: { ProfilePhoto },
  created() {
    this.getUserInfo()
      .then((res) => {
        this.userinfo = res.data;
      })
      .catch((err) => console.log(err));
  },
  computed: {
    ...mapGetters("accounts", ["USERNAME"]),
  },
};
</script>

<style lang="scss" scoped>
.c-sidebar {
  border: 2px solid black;
  border-radius: 10px;
  &__img {
    border-radius: 50%;
  }
  &__name {
    font-size: 1rem;
    width: 100%;
    padding: 10px 20px;
  }
  &--font {
    font-family: "S-CoreDream-7ExtraBold";
    font-size: 1rem;
    word-break: break-all;
  }
}

.c-title {
  font-family: "NanumBarunpen";
  text-align: start;
  font-size: 1.5rem;
}

.c-btn {
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
.c-status {
  font-family: "S-CoreDream-7ExtraBold";
  font-size: 1rem;
  width: 100%;
  margin-top: 20px;
  background-color: var(--primary-color);
  border: 2px solid black;
  border-radius: 10px;
  text-align: center;
}

.c-list {
  margin-top: 20px;
  font-family: "S-CoreDream-7ExtraBold";
}

.c-list-item {
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
