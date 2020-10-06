import { mapGetters, mapActions } from "vuex";

import * as firebase from "firebase/app";
import "firebase/auth";
import "firebase/database";

export const mixinJoinChat = {
  data() {
    return {
      chat: {},
      loading: false,
    };
  },
  computed: {
    ...mapGetters("auth", ["USER"]),
    user() {
      return this.USER;
    },
    chats() {
      return this.loadedChats;
    },
  },
  methods: {
    ...mapActions("chat", ["loadUserChats"]),
    enterChat(chat) {
      if (chat.isAlreadyJoined) {
        return;
      }

      let chatId = chat.key;
      let time = new Date().valueOf();

      let updates = {};
      updates["/chat_members/" + chatId + "/users/" + this.user.id] = {
        timestamp: time,
      };
      updates["users/" + this.user.id + "/chats/" + chatId] = {
        timestamp: time,
      };

      firebase
        .database()
        .ref()
        .update(updates)
        .then(() => {});
    
      this.loadUserChats();
      this.chat.isAlreadyJoined = !this.chat.isAlreadyJoined;
    },
    getChat(id) {
      let that = this;
      firebase
        .database()
        .ref()
        .child("chats")
        .child(id)
        .once("value")
        .then(function(snapshot) {
          let chat = snapshot.val();
          chat.key = snapshot.key;
          that.chat = chat;
          that.getUserForChat(chat);
        });
    },
    getUserForChat(chat) {
      let that = this;
      firebase
        .database()
        .ref("chat_members")
        .child(chat.key)
        .child("users")
        .once("value", function(snapshot) {
          snapshot.forEach((user) => {
            if (user.key == that.user.id) {
              that.$set(chat, "isAlreadyJoined", true);
            }
          });
        });
    },
  },
};
