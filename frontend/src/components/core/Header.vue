<template>
  <div>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title @click="$router.push({name: 'Home'})">Application</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-menu class="hidden-md-and-up" offset-y="true" v-model="menu">
        <template v-slot:activator="{ on, attrs }">
          <v-app-bar-nav-icon dark v-bind="attrs" v-on="on"></v-app-bar-nav-icon>
        </template>
        <v-list>
          <v-list-item v-for="(link, index) in links" :key="index" :href="link.href">
            <v-list-item-title>{{ link.text }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
  </div>
</template>

<script>
export default {
  data() {
    return {
      menu: false,
      links: [
        {
          text: "Home",
          href: "/",
        },
        {
          text: "login",
          href: "/user/login",
        },
      ],
    };
  },
};
</script>

<style>
</style>