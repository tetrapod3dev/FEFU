<template>
  <div>
    <v-container justify="start">
      <v-col cols="12" class="c-title c-card__content"> 내 정보 </v-col>

      <v-row
        class="c-card__content c-txt pa-5"
        :style="$vuetify.breakpoint.smAndDown ? '' : 'min-height=600px;'"
        no-gutters
      >
        <v-col class="align-stretch" cols="12">
          <v-form ref="form">
            <v-row>
              <v-col cols="12" md="6" class="py-0">
                <v-text-field
                  :value="userinfo.username"
                  label="이메일"
                  filled
                  disabled
                  color="#37cdc2"
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="6" class="py-0">
                <v-text-field
                  v-model="userinfo.nickname"
                  label="닉네임"
                  filled
                  disabled
                  color="#37cdc2"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" md="6" class="py-0">
                <v-text-field
                  :value="userinfo.age"
                  label="나이"
                  filled
                  disabled
                  color="#37cdc2"
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="6" class="py-0">
                <v-text-field
                  :value="userinfo.gender"
                  label="성별"
                  filled
                  disabled
                  color="#37cdc2"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" class="py-0">
                <v-textarea
                  filled
                  name="유저"
                  label="간단한 자기소개"
                  disabled
                  color="#37cdc2"
                  :value="userinfo.introduce"
                ></v-textarea>
              </v-col>
            </v-row>
          </v-form>

          <v-btn
            class="c-btn"
            large
            @click="$router.push({ name: 'MypageInfoUpdate' })"
          >
            회원정보 수정
          </v-btn>
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
  name: "MypageInfo",
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
        introduce: "",
        profileImage: "",
      },
    };
  },
  created() {
    this.getUserInfo()
      .then((res) => (this.userinfo = res.data))
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
    height: 48px;
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
