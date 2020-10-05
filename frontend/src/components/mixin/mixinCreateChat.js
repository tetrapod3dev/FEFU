import { mapGetters } from "vuex";

import * as firebase from "firebase/app";
import "firebase/auth";
import "firebase/database";

export const mixinCreateChat = {
  data() {
    return {
      chatName: "",
      loading: false,
    };
  },
  computed: {
    ...mapGetters("auth", ["USER"]),
    user() {
      return this.USER;
    },
  },
  methods: {
    async createChat(key) {
      if (this.chatName == "" || this.loading) {
        return;
      }

      this.loading = true;

      let time = new Date().valueOf();

      await firebase
        .database()
        .ref()
        .child("chats/" + key)
        .set({ name: this.chatName });
      await firebase
        .database()
        .ref()
        .child("chat_members/" + key)
        .child("users/" + this.user.id)
        .set({
          timestamp: time,
        });
      await firebase
        .database()
        .ref()
        .child("users/" + this.user.id)
        .child("chats/" + key)
        .set({
          timestamp: time,
        })
        .then(() => (this.loading = false));
    },
  },
};
