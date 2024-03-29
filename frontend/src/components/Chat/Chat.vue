<template>
  <v-col cols="10" style="position: relative">
    <div
      :style="
        $vuetify.breakpoint.smAndDown ? 'height: 460px;' : 'height: 550px;'
      "
      class="chat-container"
      v-on:scroll="onScroll"
      ref="chatContainer"
    >
      <message :messages="messages" @imageLoad="scrollToEnd"></message>
    </div>
    <emoji-picker
      :show="emojiPanel"
      @close="toggleEmojiPanel"
      @click="addEmojiToMessage"
    ></emoji-picker>
    <div class="typer">
      <input
        type="text"
        placeholder="채팅 입력"
        v-on:keyup.enter="preCheckSendMessage"
        v-model="content"
      />
      <v-btn
        icon
        color="var(--primary-color)"
        class="emoji-panel"
        @click="toggleEmojiPanel"
      >
        <v-icon>mdi-emoticon-outline</v-icon>
      </v-btn>
    </div>
  </v-col>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

import Message from "./part/Message.vue";
import EmojiPicker from "./part/EmojiPicker.vue";
// import Chats from "./part/Chats.vue";

import * as firebase from "firebase/app";
import "firebase/auth";
import "firebase/database";

export default {
  data() {
    return {
      content: "",
      chatMessages: [],
      emojiPanel: false,
      currentRef: {},
      loading: false,
      totalChatHeight: 0,
    };
  },
  props: ["id"],
  created() {
    this.loadUserChats();
  },
  mounted() {
    this.loadChat();
  },
  components: {
    message: Message,
    "emoji-picker": EmojiPicker,
    // chats: Chats,
  },
  computed: {
    ...mapGetters("auth", ["USER"]),
    ...mapGetters("chat", ["CHATS"]),
    chats() {
      return this.CHATS;
    },
    messages() {
      return this.chatMessages;
    },
    username() {
      return this.USER.username;
    },
    onNewMessageAdded() {
      const that = this;
      let onNewMessageAdded = function (snapshot, newMessage = true) {
        let message = snapshot.val();
        message.key = snapshot.key;
        /*eslint-disable */
        var urlPattern = /(\b(https?|ftp|file):\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|])/gi;
        /*eslint-enable */
        message.content = message.content
          .replace(/&/g, "&amp;")
          .replace(/</g, "&lt;")
          .replace(/>/g, "&gt;")
          .replace(/"/g, "&quot;")
          .replace(/'/g, "&#039;");
        message.content = message.content.replace(
          urlPattern,
          "<a href='$1'>$1</a>"
        );
        if (!newMessage) {
          that.chatMessages.unshift(that.processMessage(message));
          that.scrollTo();
        } else {
          that.chatMessages.push(that.processMessage(message));
          that.scrollToEnd();
        }
      };
      return onNewMessageAdded;
    },
  },
  watch: {
    id() {
      this.currentRef.off("child_added", this.onNewMessageAdded);
      this.loadChat();
    },
  },
  methods: {
    ...mapActions("chat", ["sendMessage"]),
    ...mapActions("chat", ["loadUserChats"]),
    loadChat() {
      this.totalChatHeight = this.$refs.chatContainer.scrollHeight;
      this.loading = false;
      if (this.id !== undefined) {
        this.chatMessages = [];
        let chatID = this.id;
        this.currentRef = firebase
          .database()
          .ref("messages")
          .child(chatID)
          .child("messages")
          .limitToLast(20);
        this.currentRef.on("child_added", this.onNewMessageAdded);
      }
    },
    onScroll() {
      this.$nextTick(() => {
        let self = this;
        let scrollValue = self.$refs.chatContainer.scrollTop;
        const that = this;
        if (scrollValue < 100 && !this.loading) {
          this.totalChatHeight = self.$refs.chatContainer.scrollHeight;
          this.loading = true;
          let chatID = this.id;
          let currentTopMessage = this.chatMessages[0];
          if (currentTopMessage === undefined) {
            this.loading = false;
            return;
          }
          firebase
            .database()
            .ref("messages")
            .child(chatID)
            .child("messages")
            .orderByKey()
            .endAt(currentTopMessage.key)
            .limitToLast(20)
            .once("value")
            .then(function (snapshot) {
              let tempArray = [];
              snapshot.forEach(function (item) {
                tempArray.push(item);
              });
              if (tempArray[0].key === tempArray[1].key) return;
              tempArray.reverse();
              tempArray.forEach(function (child) {
                that.onNewMessageAdded(child, false);
              });
              that.loading = false;
            });
        }
      });
    },
    processMessage(message) {
      /*eslint-disable */
      var imageRegex = /([^\s\']+).(?:jpg|jpeg|gif|png)/i;
      /*eslint-enable */
      if (imageRegex.test(message.content)) {
        message.image = imageRegex.exec(message.content)[0];
      }
      var emojiRegex = /([\u{1f300}-\u{1f5ff}\u{1f900}-\u{1f9ff}\u{1f600}-\u{1f64f}\u{1f680}-\u{1f6ff}\u{2600}-\u{26ff}\u{2700}-\u{27bf}\u{1f1e6}-\u{1f1ff}\u{1f191}-\u{1f251}\u{2934}-\u{1f18e}])/gu;
      if (emojiRegex.test(message.content)) {
        message.content = message.content.replace(
          emojiRegex,
          '<span class="emoji">$1</span>'
        );
      }
      return message;
    },
    preCheckSendMessage() {
      if (this.content !== "") {
        this.sendMessage({
          username: this.username,
          content: this.content,
          date: new Date().toString(),
          chatID: this.id,
        });
        this.content = "";
      }
    },
    scrollToEnd() {
      this.$nextTick(() => {
        var container = this.$el.querySelector(".chat-container");
        container.scrollTop = container.scrollHeight;
      });
    },
    scrollTo() {
      this.$nextTick(() => {
        let currentHeight = this.$refs.chatContainer.scrollHeight;
        let difference = currentHeight - this.totalChatHeight;
        var container = this.$el.querySelector(".chat-container");
        container.scrollTop = difference;
      });
    },
    addEmojiToMessage(emoji) {
      this.content += emoji.value;
    },
    toggleEmojiPanel() {
      this.emojiPanel = !this.emojiPanel;
    },
  },
};
</script>

<style lang="scss" scoped>
.scrollable {
  overflow-y: auto;
  height: 100%;
}
.typer {
  box-sizing: border-box;
  display: flex;
  align-items: center;
  bottom: 0;
  height: 4.9rem;
  width: 100%;
  background-color: #fff;
  box-shadow: 0 -5px 10px -5px rgba(0, 0, 0, 0.2);
}
.typer input[type="text"] {
  position: absolute;
  left: 2.5rem;
  padding: 1rem;
  width: 80%;
  background-color: transparent;
  border: none;
  outline: none;
  font-size: 1.25rem;
}
.chat-container {
  box-sizing: border-box;
  overflow-y: auto;
  padding: 10px;
  background-color: #f2f2f2;
}

@media (max-width: 480px) {
  .chat-container .content {
    max-width: 60%;
  }
}
</style>
