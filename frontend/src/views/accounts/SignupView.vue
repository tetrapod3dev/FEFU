<template>
  <v-app id="inspire">
    <v-main>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="6" lg="4">
            <div class="login-welcome">어서와요, 반가워요🙌!</div>
            <v-card class="custom-login-card">
              <v-card-text>
                <div class="login-title">회원가입 해주세요</div>
                <v-form>
                  <v-text-field
                    v-model="signupData.username"
                    label="아이디"
                    name="email"
                    type="text"
                    filled
                    color="#37cdc2"
                    :rules="emailRules"
                  ></v-text-field>

                  <v-text-field
                    id="password"
                    v-model="signupData.password"
                    label="비밀번호"
                    name="password"
                    filled
                    color="#37cdc2"
                    append-outer-icon
                    :append-icon="isShowPW ? 'mdi-eye' : 'mdi-eye-off'"
                    @click:append="isShowPW = !isShowPW"
                    :type="isShowPW ? 'text' : 'password'"
                    :rules="[rules.required, rules.min]"
                  ></v-text-field>
                  <v-text-field
                    id="passwordConfirm"
                    v-model="signupData.passwordConfirm"
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
                  ></v-text-field>
                </v-form>
                <p class="mb-0 text-left">
                  ✋ 잠깐!
                  <br />회원 가입 버튼을 클릭하면, FEFU의 <a>회원약관</a>에
                  동의하며 쿠키 사용을 포함한 <a>개인정보처리방침</a>을 읽었음을
                  인정하게 됩니다.
                </p>
                <v-checkbox
                  v-model="checkbox"
                  label="동의합니다."
                  required
                  color="#37cdc2"
                ></v-checkbox>
                <v-col class="py-0 px-0">
                  <span>이미 회원이신가요? </span>
                  <router-link
                    to="/user/login"
                    tag="span"
                    style="cursor: pointer; color: black"
                    >로그인</router-link
                  >
                </v-col>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  class="custom-login-btn"
                  width="100%"
                  large
                  @click="signup(signupData)"
                  >회원가입
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
  name: "SignupView",
  data() {
    return {
      isShowPW: false,
      isShowPW2: false,
      checkbox: false,
      signupData: {
        username: null,
        password: null,
        passwordConfirm: null,
        nickname: "지구용사",
        age: 23,
        gender: "남자",
      },
      emailRules: [
        (v) => !!v || "아이디로 사용하실 이메일을 입력해주세요",
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
  computed: {
    passwordConfirmationRule() {
      return (
        this.signupData.password === this.signupData.passwordConfirm ||
        "비밀번호가 일치하지 않습니다."
      );
    },
  },
  methods: {
    ...mapActions("accounts", ["signup"]),
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
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.16), 0 1px 5px rgba(0, 0, 0, 0.23);
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
