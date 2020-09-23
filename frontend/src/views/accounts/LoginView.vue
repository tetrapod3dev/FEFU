<template>
  <v-app id="inspire">
    <v-main>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="6" lg="4">
            <div class="login-welcome">환영합니다😏!</div>
            <v-card class="custom-login-card">
              <v-card-text>
                <div class="login-title">로그인해주세요</div>
                <v-form>
                  <v-text-field
                    label="아이디"
                    name="email"
                    type="text"
                    v-model="loginData.username"
                    :rules="emailRules"
                    required
                    filled
                    autofocus
                    autocapitalize="off"
                    autocorrect="off"
                    autocomplete="off"
                    color="#37cdc2"
                  ></v-text-field>

                  <v-text-field
                    id="password"
                    label="비밀번호"
                    name="password"
                    filled
                    append-outer-icon
                    :append-icon="isShowPW ? 'mdi-eye' : 'mdi-eye-off'"
                    @click:append="isShowPW = !isShowPW"
                    :type="isShowPW ? 'text' : 'password'"
                    autocomplete="off"
                    required
                    :rules="[rules.required, rules.min]"
                    v-model="loginData.password"
                    @keydown.enter.prevent="login(loginData)"
                    color="#37cdc2"
                  ></v-text-field>
                </v-form>
                <v-col class="py-0 px-0">
                  <span>아직 회원이 아니신가요? </span>
                  <router-link
                    to="/user/signup"
                    tag="span"
                    style="cursor:pointer; color:black;"
                    >회원 가입</router-link
                  >
                </v-col>
              </v-card-text>

              <v-card-actions>
                <v-btn
                  class="custom-login-btn"
                  width="100%"
                  large
                  @click="login(loginData)"
                  >로그인
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
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
      emailRules: [
        (v) => !!v || "가입하신 이메일 계정을 입력해주세요",
        (v) => /.+@.+\..+/.test(v) || "올바른 양식의 이메일을 입력해주세요",
      ],
      rules: {
        required: (value) => !!value || "비밀번호를 입력해주세요.",
        min: (v) =>
          (v && v.length >= 8) || "비밀번호는 8글자 이상 입력해주세요",
      },
      valid: true,
    };
  },

  methods: {
    ...mapActions("accounts", ["login"]),
    moveToSignup() {
      this.$router.push({ name: "Signup" });
    },
  },
};
</script>

<style scoped>
.login-welcome {
  border: 2px solid black;
  border-radius: 5px;
  padding: 10px 20px;
  margin: 10px 0;
  text-align: start;
  font-size: 1.3rem;
  font-family: "NanumBarunpen";
}

.login-title {
  text-align: start;
  font-size: 1.3rem;
  font-family: "NanumBarunpen";
  margin-bottom: 20px;
}

.custom-login-card {
  font-family: "NanumBarunpen";
  border: 2px solid black;
  padding: 10px 5px;
}

.custom-login-btn {
  border: 2px solid black;
  background: var(--primary-color);
}
</style>
