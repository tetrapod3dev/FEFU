<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col class="my-12" cols="12" sm="8" md="6" lg="4">
        <div class="login-welcome">어서와요, 반가워요🙌!</div>
        <v-card class="custom-login-card">
          <v-card-text>
            <div class="login-title">회원가입 해주세요</div>
            <v-form ref="form">
              <v-text-field
                v-model="signupData.username"
                label="아이디"
                name="email"
                type="text"
                filled
                color="#37cdc2"
                @blur="checkEmail"
                :rules="[
                  (v) => !!v || '아이디로 사용하실 이메일을 입력해주세요',
                  (v) =>
                    /.+@.+\..+/.test(v) ||
                    '올바른 양식의 이메일을 입력해주세요',
                  checkEmailRule,
                ]"
              ></v-text-field>
              <v-text-field
                v-model="signupData.nickname"
                label="닉네임"
                name="nickname"
                type="text"
                filled
                color="#37cdc2"
                @blur="checkNickname"
                :rules="[
                  (v) => !!v || '닉네임을 입력해주세요',
                  (v) =>
                    /^[\w\Wㄱ-ㅎㅏ-ㅣ가-힣]{2,8}$/.test(v) ||
                    '2~8글자로 입력해주세요',
                  checkNicknameRule,
                ]"
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
              <v-row no-gutters>
                <v-col cols="5">
                  <v-text-field
                    v-model="birthday"
                    label="주민번호"
                    name="age"
                    type="text"
                    filled
                    color="#37cdc2"
                    :rules="ageRules"
                  ></v-text-field>
                </v-col>
                <v-col cols="1"
                  ><v-text-field
                    label="-"
                    :disabled="true"
                    filled
                    color="#37cdc2"
                  ></v-text-field
                ></v-col>
                <v-col cols="2"
                  ><v-text-field
                    v-model="genderNum"
                    label="뒷자리"
                    name="gender"
                    type="text"
                    filled
                    color="#37cdc2"
                    :rules="genderRules"
                  ></v-text-field
                ></v-col>
                <v-col cols="4">
                  <v-text-field
                    label="******"
                    :disabled="true"
                    type="text"
                    filled
                    color="#37cdc2"
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-dialog v-model="dialog" width="600px">
                <template v-slot:activator="{ on, attrs }">
                  <p class="mb-0 text-left">
                    ✋ 잠깐!
                    <br />회원 가입 버튼을 클릭하면, FEFU의
                    <a v-bind="attrs" v-on="on" @click="tab = 'terms'"
                      >회원약관</a
                    >에 동의하며 쿠키 사용을 포함한
                    <a v-bind="attrs" v-on="on" @click="tab = 'privacy-policy'"
                      >개인정보처리방침</a
                    >을 읽었음을 인정하게 됩니다.
                  </p>
                </template>
                <v-card>
                  <v-tabs v-model="tab">
                    <v-tab href="#terms">
                      <v-card-title>
                        <span class="login-title">FEFU 이용 약관</span>
                      </v-card-title>
                    </v-tab>
                    <v-tab href="#privacy-policy">
                      <v-card-title>
                        <span class="login-title">개인정보 처리방침</span>
                      </v-card-title>
                    </v-tab>
                  </v-tabs>

                  <v-tabs-items v-model="tab">
                    <v-tab-item id="terms">
                      <v-card-text>
                        <terms />
                      </v-card-text>
                    </v-tab-item>
                    <v-tab-item id="privacy-policy">
                      <v-card-text>
                        <privacy-policy />
                      </v-card-text>
                    </v-tab-item>
                  </v-tabs-items>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                      color="var(--primary-color)"
                      text
                      @click="dialog = false"
                      >취소</v-btn
                    >
                    <v-btn color="var(--primary-color)" text @click="agreeTerms"
                      >동의</v-btn
                    >
                  </v-card-actions>
                </v-card>
              </v-dialog>
              <v-checkbox
                v-model="checkbox"
                label="동의합니다."
                required
                color="#37cdc2"
                :rules="[checkboxRule]"
              ></v-checkbox>
            </v-form>
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
              @click="preSignup(signupData)"
              >회원가입
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
import SERVER from "@/api/api";
import { mapActions } from "vuex";

import Terms from "@/components/Terms";
import PrivacyPolicy from "@/components/PrivacyPolicy";

export default {
  name: "SignupView",
  data() {
    return {
      tab: null,
      dialog: false,
      isShowPW: false,
      isShowPW2: false,
      checkbox: false,
      genderNum: "",
      birthday: "",
      isValidEmail: true,
      isValidNickname: true,
      signupData: {
        username: null,
        password: null,
        passwordConfirm: null,
        nickname: "",
        age: this.age,
        gender: this.parseGender,
      },
      genderRules: [(v) => !!v || "", (v) => /^\d{1}$/.test(v) || ""],
      ageRules: [(v) => !!v || "", (v) => /^\d{6}$/.test(v) || ""],
      rules: {
        required: (value) => !!value || "비밀번호를 입력해주세요.",
        min: (v) =>
          (v && v.length >= 8) || "비밀번호는 8글자 이상 입력해주세요",
      },

      valid: true,
    };
  },
  components: {
    Terms,
    PrivacyPolicy,
  },
  computed: {
    parseGender() {
      return this.genderNum % 2 ? "남자" : "여자";
    },
    parseAge() {
      return (
        new Date().getFullYear() +
        1 -
        parseInt(this.birthday / 10000) -
        (this.genderNum > 2 ? 2000 : 1900)
      );
    },
    passwordConfirmationRule() {
      return (
        this.signupData.password === this.signupData.passwordConfirm ||
        "비밀번호가 일치하지 않습니다."
      );
    },
    checkEmailRule() {
      return this.isValidEmail || "이미 있는 이메일 입니다.";
    },
    checkNicknameRule() {
      return this.isValidNickname || "이미 있는 닉네임 입니다.";
    },
    checkboxRule() {
      return this.checkbox || "약관에 동의해주세요";
    },
  },
  methods: {
    ...mapActions("accounts", ["signup"]),
    agreeTerms() {
      this.dialog = false;
      this.checkbox = true;
    },
    preSignup(data) {
      if (this.$refs.form.validate()) {
        data.gender = this.parseGender;
        data.age = this.parseAge;
        this.signup(data);
      }
    },
    checkEmail() {
      axios
        .get(
          SERVER.URL +
            SERVER.ROUTES.accounts.checkEmail +
            this.signupData.username
        )
        .then((res) => {
          this.isValidEmail = res.data == "사용가능";
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
    checkNickname() {
      axios
        .get(
          SERVER.URL +
            SERVER.ROUTES.accounts.checkNickname +
            this.signupData.nickname
        )
        .then((res) => {
          console.log(res);
          this.isValidNickname = res.data == "사용가능";
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
  },
};
</script>

<style lang="scss" scoped>
.custom-title {
  font-family: "NanumBarunpen";
  text-align: start;
  font-size: 1.3rem;
}

.login-welcome {
  @extend .custom-title;
  border: 2px solid black;
  border-radius: 5px;
  padding: 10px 20px;
  margin: 10px 0;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.16), 0 1px 5px rgba(0, 0, 0, 0.23);
}

.login-title {
  @extend .custom-title;
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
