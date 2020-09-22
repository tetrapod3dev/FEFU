<template>
  <div id="custom-header">
    <v-navigation-drawer
      v-model="drawer"
      app
      right
      :disable-resize-watcher="true"
      :temporary="true"
    >
      <v-list dense>
        <v-list-item v-for="(link, index) in links" :key="index" :href="link.href">
          <v-list-item-content>
            <v-list-item-title class="text-left">{{link.textKr}} {{link.textEn}}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar fixed flat color="transparent">
      <v-toolbar-title class="nav-logo text-left" @click="$router.push({name: 'Home'})">
        For
        <span class="js-nametag">Earth</span>
        <span class="js-nametag">Us</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <router-link
        tag="button"
        v-for="(link, index) in links"
        :key="index"
        :to="link.href"
        class="hidden-sm-and-down custom-button mx-1"
      >{{ link.textKr }}</router-link>
      <v-app-bar-nav-icon class="hidden-md-and-up custom-button" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
    </v-app-bar>
  </div>
</template>

<script>
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
          href: "/about",
        },
        {
          textKr: "캠페인",
          textEn: "CAMPAIGN",
          href: "/campaigns",
        },
        {
          textKr: "중고마켓",
          textEn: "MARKET",
          href: "/market",
        },
        {
          textKr: "로그인",
          textEn: "LOGIN",
          href: "/user/login",
        },
      ],
    };
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

#custom-header .custom-button {
  border: 2px solid black;
  border-radius: 5px;
  padding: 10px 20px !important;
  background-color: #ffffff;
  top: 0px;
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
</style>