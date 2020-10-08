<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <!-- signup card start -->
      <v-col class="my-12" cols="12" sm="8" md="6" lg="4">
        <!-- signup card title -->
        <div class="c-card__title c-title">어서와요, 반가워요🙌!</div>
        <!-- signup card content start -->
        <v-card class="c-card__content c-txt">
          <v-card-text>
            <div class="c-title mb-5">회원가입 해주세요</div>

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
                    /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$/.test(v) ||
                    '올바른 양식의 이메일을 입력해주세요',
                  checkEmailRule,
                ]"
              />

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
              />

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
              />

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
              />

              <v-row no-gutters>
                <v-col cols="5">
                  <v-text-field
                    v-model="birthday"
                    label="주민번호"
                    name="age"
                    type="text"
                    filled
                    color="#37cdc2"
                    maxlength="6"
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

                <!-- modal start -->
                <v-card style="border: 3px solid #000000">
                  <v-tabs v-model="tab" color="var(--primary-color)">
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
                    <v-btn class="c-btn" text @click="dialog = false"
                      >취소</v-btn
                    >
                    <v-btn class="c-btn" text @click="agreeTerms">동의</v-btn>
                  </v-card-actions>
                </v-card>
                <!-- modal end -->
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
              >
                로그인
              </router-link>
            </v-col>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              class="c-btn"
              width="100%"
              large
              @click="preSignup(signupData)"
            >
              회원가입
            </v-btn>
          </v-card-actions>
        </v-card>
        <!-- signup card content end -->
      </v-col>
      <!-- signup card end -->
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
import SERVER from "@/api/api";
import { mapActions, mapGetters } from "vuex";
import router from "@/router";

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
      genderRules: [(v) => !!v || "", (v) => /[1-4]/.test(v) || ""],
      ageRules: [(v) => !!v || "", (v) => /([0-9]{2}(0[1-9]|1[0-2])(0[1-9]|[1,2][0-9]|3[0,1]))/.test(v) || ""],
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
    ...mapGetters("accounts", ["isLoggedIn"]),
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
  mounted() {
    if (this.isLoggedIn) {
      alert("이미 로그인한 유저입니다!")
      this.$router.push({ name: "Home" });
    }
  },
  methods: {
    ...mapActions("accounts", ["signup"]),
    ...mapActions("auth", ["signUserUp"]),
    agreeTerms() {
      this.dialog = false;
      this.checkbox = true;
    },
    preSignup(data) {
      if (this.$refs.form.validate()) {
        data.gender = this.parseGender;
        data.age = this.parseAge;
        this.signup(data).then(() => router.push({ name: "LoginView" }));
        this.signUserUp({
          email: this.signupData.username,
          password: this.signupData.password,
          username: this.signupData.nickname,
        });
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
  font-family: "S-CoreDream-7ExtraBold";
  border: 2px solid black;
  border-radius: 10px;
}
</style>
