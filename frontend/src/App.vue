<template>
  <div id="app">
    <v-app id="inspire">
      <core-header />
      <v-main>
        <router-view />
      </v-main>
      <core-footer />
    </v-app>
  </div>
</template>

<script>
export default {
  components: {
    CoreFooter: () => import("./components/core/Footer"),
    CoreHeader: () => import("./components/core/Header"),
  },
};
</script>>

<style lang="scss">
:root {
  --primary-color: #37cdc2;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
