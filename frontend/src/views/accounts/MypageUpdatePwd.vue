<template>
  <div>
    <v-container class="pa-0" fill-height>
      <v-col cols="12" class="c-title c-card__content mb-3">
        비밀번호변경
      </v-col>

      <v-row
        class="c-card__content c-txt pa-3"
        :style="$vuetify.breakpoint.smAndDown ? '' : 'min-height=600px;'"
        no-gutters
      >
        <v-col cols="12">
          <div class="c-title mb-5">새로운 비밀번호를 입력하세요</div>
        </v-col>
        <v-col class="align-stretch" cols="12">
          <v-form ref="form">
            <v-text-field
              id="password"
              v-model="newPW"
              label="비밀번호"
              name="password"
              filled
              color="#37cdc2"
              append-outer-icon
              :append-icon="isShowPW ? 'mdi-eye' : 'mdi-eye-off'"
              @click:append="isShowPW = !isShowPW"
              :type="isShowPW ? 'text' : 'password'"
              :rules="[rules.required, rules.min]"
            />

            <v-text-field
              id="passwordConfirm"
              v-model="newPW2"
              label="비밀번호 확인"
              name="passwordConfirm"
              filled
              color="#37cdc2"
              append-outer-icon
              :append-icon="isShowPW2 ? 'mdi-eye' : 'mdi-eye-off'"
              @click:append="isShowPW2 = !isShowPW2"
              :type="isShowPW2 ? 'text' : 'password'"
              :rules="[
                (v) => !!v || '비밀번호를 다시 한번 입력해주세요.',
                passwordConfirmationRule,
              ]"
            />
          </v-form>

          <v-btn class="c-btn" large> 비밀번호 변경 </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import { mixinGetUserInfo } from "@/components/mixin/mixinGetUserInfo";
import { mapGetters } from "vuex";
// import SERVER from "@/api/api";

export default {
  name: "MypageUpdatePwd",
  mixins: [mixinGetUserInfo],
  data() {
    return {
      isShowPW: false,
      isShowPW2: false,
      newPW: null,
      newPW2: null,
      listColorName: [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "purple",
      ],
      rules: {
        required: (value) => !!value || "비밀번호를 입력해주세요.",
        min: (v) =>
          (v && v.length >= 8) || "비밀번호는 8글자 이상 입력해주세요",
      },
    };
  },
  computed: {
    ...mapGetters("accounts", ["config", "USERNAME"]),
    passwordConfirmationRule() {
      return this.newPW === this.newPW2 || "비밀번호가 일치하지 않습니다.";
    },
  },
  methods: {},
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
