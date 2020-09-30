<template>
  <div id="campaign-list">
    <v-col class="py-12"></v-col>
    <v-container>
      <v-row>
        <v-col cols="12" sm="3">
          <!-- 사이드바 -->

          <div>
            <v-img
              class="c-sidebar c-sidebar__img mr-auto ml-auto"
              height="200px"
              width="200px"
              :src="
                !!userinfo.photo
                  ? imageSrc(userinfo.photo)
                  : require(`@/assets/images/${userinfo.gender}.png`)
              "
              lazy-src="@/assets/images/lazy-loading.jpg"
            >
              <template v-slot:placeholder>
                <lazy-loading />
              </template>
            </v-img>

            <div class="[ c-sidebar c-sidebar__name c-sidebar--font ] mt-5">
              <div>{{ userinfo.username }}</div>
              <div>{{ userinfo.nickname }}</div>
            </div>
            <v-list class="c-list">
              <v-list-item :to="{ name: 'MypageInfo' }" class="c-list-item">
                <v-list-item-content>
                  <v-list-item-title>내정보</v-list-item-title>
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

          <button class="c-btn">회원 탈퇴</button>
        </v-col>

        <v-col cols="12" md="9" class="pt-0">
          <router-view />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import { mixinGetUserInfo } from "@/components/mixin/mixinGetUserInfo";
import { mapGetters } from "vuex";
import SERVER from "@/api/api";

export default {
  name: "Mypage",
  mixins: [mixinGetUserInfo],
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
  created() {
    this.getUserInfo()
      .then((res) => {
        this.userinfo = res.data;
      })
      .catch((err) => console.log(err));
  },
  computed: {
    ...mapGetters("accounts", ["config", "USERNAME"]),
  },
  methods: {
    imageSrc(filename) {
      return SERVER.IMAGE_URL + filename;
    },
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
  }
}

.c-card__content {
  border: 2px solid black;
  border-radius: 5px;
  padding: 10px 20px;
  margin: 10px 0;
}
.c-txt,
.c-title {
  font-family: "NanumBarunpen";
}

.c-title {
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
