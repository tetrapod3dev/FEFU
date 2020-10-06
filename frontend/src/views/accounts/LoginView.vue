<template>
  <v-container fill-height fluid>
    <v-row justify="center">
      <!-- login card start -->
      <v-col class="my-12" cols="12" sm="8" md="6" lg="4">
        <!-- login card title -->
        <div class="c-card__title c-title">환영합니다😏!</div>
        <!-- login card content start -->
        <v-card class="c-card__content c-txt">
          <v-card-text>
            <div class="c-title mb-5">로그인해주세요</div>

            <v-form ref="form">
              <v-text-field
                label="아이디"
                name="email"
                type="text"
                v-model="loginData.username"
                :rules="emailRules"
                required
                autofocus
                autocapitalize="off"
                autocorrect="off"
                autocomplete="off"
                filled
                color="#37cdc2"
              />

              <v-text-field
                label="비밀번호"
                name="password"
                :type="isShowPW ? 'text' : 'password'"
                v-model="loginData.password"
                :rules="[
                  (value) => !!value || '비밀번호를 입력해주세요',
                  (v) =>
                    (v && v.length >= 8) ||
                    '비밀번호는 8글자 이상 입력해주세요',
                  !isWrong || '비밀번호를 틀렸습니다',
                ]"
                @keydown.enter.prevent="preTest"
                @click:append="isShowPW = !isShowPW"
                @focus="isWrong = false"
                required
                autocomplete="off"
                :append-icon="isShowPW ? 'mdi-eye' : 'mdi-eye-off'"
                append-outer-icon
                filled
                color="#37cdc2"
              />
            </v-form>

            <v-col class="pa-0">
              <span>아직 회원이 아니신가요? </span>
              <router-link
                :to="{ name: 'SignupView' }"
                tag="span"
                style="cursor: pointer; color: black"
              >
                회원 가입
              </router-link>
            </v-col>
          </v-card-text>

          <v-card-actions>
            <v-btn class="c-btn" width="100%" large @click="preTest"
              >로그인
            </v-btn>
          </v-card-actions>
        </v-card>
        <!-- login card content end -->
      </v-col>
      <!-- login card end -->
    </v-row>
  </v-container>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "LoginView",
  data() {
    return {
      loginData: {
        username: null,
        password: null,
      },
      isShowPW: false,
      isWrong: false,
      emailRules: [
        (v) => !!v || "가입하신 이메일 계정을 입력해주세요",
        (v) => /.+@.+\..+/.test(v) || "올바른 양식의 이메일을 입력해주세요",
      ],
      valid: true,
    };
  },

  methods: {
    ...mapActions("accounts", ["login"]),
    ...mapActions("auth", ["signUserIn"]),
    moveToSignup() {
      this.$router.push({ name: "Signup" });
    },
    preTest() {
      if (this.$refs.form.validate()) {
        this.login(this.loginData)
        this.signUserIn({
          email: this.loginData.username,
          password: this.loginData.password,
        });
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.c-txt,
.c-title {
  font-family: "NanumBarunpen";
}

.c-title {
  text-align: start;
  font-size: 1.3rem;
}

.c-card__title {
  border: 2px solid black;
  border-radius: 5px;
  padding: 10px 20px;
  margin: 10px 0;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.16), 0 1px 5px rgba(0, 0, 0, 0.23);
}

.c-card__content {
  border: 2px solid black;
  padding: 10px 5px;
}

.c-btn {
  border: 2px solid black;
  background: var(--primary-color);
}
</style>
