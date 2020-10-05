import * as firebase from "firebase/app";
import "firebase/auth";
import "firebase/database";

export default {
  namespaced: true,
  state: {
    chats: {},
  },
  mutations: {
    setChats(state, payload) {
      payload["0"] = { name: "Default" };
      state.chats = payload;
    },
  },
  getters: {
    CHATS(state) {
      return state.chats;
    },
  },
  actions: {
    sendMessage(context, payload) {
      let chatID = payload.chatID;
      const message = {
        user: payload.username,
        content: payload.content,
        date: payload.date,
      };
      firebase
        .database()
        .ref("messages")
        .child(chatID)
        .child("messages")
        .push(message)
        .then(() => {})
        .catch((error) => {
          console.log(error);
        });
    },
    loadUserChats(context) {
      let user = context.rootGetters["auth/USER"];
      console.log(user);
      firebase
        .database()
        .ref("users")
        .child(user.id)
        .child("chats")
        .orderByChild("timestamp")
        .once("value", function(snapshot) {
          let chats = snapshot.val();
          if (chats == null) {
            chats = {};
          }

          for (let chatId in chats) {
            chats[chatId].name = "로딩 중...";
            firebase
              .database()
              .ref("chats")
              .child(chatId)
              .once("value", function(snapshot) {
                chats[chatId].name = snapshot.val().name;
                context.commit("setChats", chats);
              });
          }
        });
    },
  },
};
