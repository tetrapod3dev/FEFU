<template>
  <v-app id="inspire">
    <v-main>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="4">
            <v-card class="elevation-12">
              <v-toolbar color="primary" dark flat>
                <v-toolbar-title>Login form</v-toolbar-title>
                <v-spacer></v-spacer>
                <v-tooltip bottom>
                  <span>Source</span>
                </v-tooltip>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field
                    label="Login"
                    name="login"
                    prepend-icon="mdi-account"
                    type="text"
                    v-model="loginData.username"
                    required
                    autofocus
                    autocapitalize="off"
                    autocorrect="off"
                    autocomplete="off"
                  ></v-text-field>

                  <v-text-field
                    id="password"
                    label="Password"
                    name="password"
                    prepend-icon="mdi-lock"
                    append-outer-icon
                    :append-icon="isShowPW ? 'mdi-eye' : 'mdi-eye-off'"
                    @click:append="isShowPW = !isShowPW"
                    :type="isShowPW ? 'text' : 'password'"
                    autocomplete="off"
                    required
                    v-model="loginData.password"
                    @keydown.enter.prevent="login(loginData)"
                  ></v-text-field>
                </v-form>
                <v-col>
                  <span>아직 회원이 아니신가요?</span>
                  <router-link to="/user/signup" tag="span">회원 가입</router-link>
                </v-col>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" @click="login(loginData)">로그인</v-btn>
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

<style>
</style>