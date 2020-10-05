<template>
  <v-list subheader>
    <v-subheader>Your Chats</v-subheader>
    <v-list-item
      v-for="(chat, index) in chats"
      v-bind:key="chat.name"
      :to="'/chat/chats/' + index"
    >
      <v-list-item-content>
        <v-list-item-title v-html="chat.name"></v-list-item-title>
      </v-list-item-content>
      <v-list-item-action>
        <v-icon>mdi-chat</v-icon>
      </v-list-item-action>
    </v-list-item>
  </v-list>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  created() {
    this.loadUserChats();
  },
  computed: {
    ...mapGetters("chat", ["CHATS"]),
    chats() {
      return this.CHATS;
    },
  },
  methods: {
    ...mapActions("chat", ["loadUserChats"]),
  },
};
</script>

<style lang="scss" scoped>
</style>