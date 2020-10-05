<template>
  <div id="c-header">
    <img
      :src="
        $vuetify.breakpoint.smAndDown
          ? require('@/assets/images/logo64.png')
          : require('@/assets/images/logo128.png')
      "
      class="rotating"
      style="z-index: 10; position: fixed; cursor: pointer"
      :style="
        $vuetify.breakpoint.smAndDown
          ? 'height: 64px;width: 64px;top: 0px;left: 0px;'
          : 'height: 128px;width: 128px;top: 5px;left: 5px;'
      "
      @click="
        moveToPage({
          name: 'Home',
        })
      "
    />
    <v-navigation-drawer
      v-model="drawer"
      app
      right
      :disable-resize-watcher="true"
      :temporary="true"
    >
      <v-list dense>
        <v-list-item
          v-for="(link, index) in links"
          :key="index"
          :to="{ name: link.href }"
        >
          <v-list-item-content>
            <v-list-item-title class="text-left c-drawer"
              >{{ link.textKr }} {{ link.textEn }}</v-list-item-title
            >
          </v-list-item-content>
        </v-list-item>
        <v-list-item v-if="!isLoggedIn" :to="{ name: 'LoginView' }">
          <v-list-item-content>
            <v-list-item-title class="text-left c-drawer"
              >로그인 LOGIN</v-list-item-title
            >
          </v-list-item-content>
        </v-list-item>
        <v-list-item v-if="isLoggedIn" :to="{ name: 'MypageInfo' }">
          <v-list-item-content>
            <v-list-item-title class="text-left c-drawer"
              >마이페이지 MYPAGE</v-list-item-title
            >
          </v-list-item-content>
        </v-list-item>
        <v-list-item v-if="isLoggedIn" @click="preLogout">
          <v-list-item-content>
            <v-list-item-title class="text-left c-drawer"
              >로그아웃 LOGOUT</v-list-item-title
            >
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar fixed flat color="transparent">
      <!-- <v-toolbar-title
        class="nav-logo text-left"
        @click="$router.push({ name: 'Home' })"
      >
        For
        <span class="js-nametag">Earth</span>
        <span class="js-nametag">Us</span>
      </v-toolbar-title> -->
      <v-spacer></v-spacer>
      <router-link
        tag="button"
        v-for="(link, index) in links"
        :key="index"
        :to="{ name: link.href }"
        class="hidden-sm-and-down custom-button mx-1"
        >{{ link.textKr }}</router-link
      >
      <router-link
        v-if="!isLoggedIn"
        tag="button"
        to="/user/login"
        class="hidden-sm-and-down custom-button mx-1"
        >로그인</router-link
      >
      <router-link
        v-if="isLoggedIn"
        tag="button"
        to="/mypage/info"
        class="hidden-sm-and-down custom-button mx-1"
      >
        마이페이지
      </router-link>
      <button
        v-if="isLoggedIn"
        @click="preLogout"
        class="hidden-sm-and-down custom-button mx-1"
      >
        로그아웃
      </button>
      <v-app-bar-nav-icon
        class="hidden-md-and-up custom-button"
        @click.stop="drawer = !drawer"
      ></v-app-bar-nav-icon>
    </v-app-bar>
  </div>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from "vuex";
// config
export default {
  name: "CoreHeader",
  data() {
    return {
      drawer: null,
      links: [
        {
          textKr: "소개",
          textEn: "ABOUT",
          href: "About",
        },
        {
          textKr: "캠페인",
          textEn: "CAMPAIGN",
          href: "CampaignMain",
        },
        {
          textKr: "중고마켓",
          textEn: "MARKET",
          href: "MarketMainView",
        },
      ],
    };
  },
  computed: {
    ...mapGetters("accounts", ["isLoggedIn"]),
  },
  methods: {
    ...mapActions("accounts", ["logout"]),
    ...mapMutations("auth", ["clearUser"]),
    preLogout() {
      this.logout();
      this.clearUser();
    },
    moveToPage(_url) {
      this.$router.push(_url).catch((error) => {
        if (error.name === "NavigationDuplicated") {
          location.reload();
        }
      });
    },
  },
};
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap");
@font-face {
  font-family: "S-CoreDream-7ExtraBold";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/S-CoreDream-7ExtraBold.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}

.nav-logo {
  font-family: "Patrick Hand", cursive;
  font-size: 32px;
  cursor: pointer;
}

.js-nametag {
  position: absolute;

  &:nth-child(1) {
    animation-name: fade;
    animation-fill-mode: both;
    animation-iteration-count: infinite;
    animation-duration: 8s;
    animation-direction: alternate-reverse;
  }

  &:nth-child(2) {
    animation-name: fade;
    animation-fill-mode: both;
    animation-iteration-count: infinite;
    animation-duration: 8s;
    animation-direction: alternate;
  }
}

@keyframes fade {
  0%,
  50% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

.c-drawer {
  font-family: "S-CoreDream-7ExtraBold";
}

#c-header .custom-button {
  border: 2px solid black;
  border-radius: 5px;
  padding: 10px 20px !important;
  background-color: #ffffff;
  font-family: "S-CoreDream-7ExtraBold";
  letter-spacing: 0px;
  transition: 0.3s;

  &:hover {
    box-shadow: 2px 2px 0px 0px rgba(0, 0, 0, 1);
    transform: translate3d(0px, -5px, -5px);
    background-color: var(--primary-color);
    transition: 0.3s;
    cursor: pointer;
  }
  &:focus {
    outline: 0;
  }
}

.rotating:hover {
  -webkit-animation: rotating 10s linear infinite;
  -moz-animation: rotating 10s linear infinite;
  -ms-animation: rotating 10s linear infinite;
  -o-animation: rotating 10s linear infinite;
  animation: rotating 10s linear infinite;
}
@-webkit-keyframes rotating /* Safari and Chrome */ {
  from {
    -webkit-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  to {
    -webkit-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@keyframes rotating {
  from {
    -ms-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -webkit-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  to {
    -ms-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -webkit-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
</style>
