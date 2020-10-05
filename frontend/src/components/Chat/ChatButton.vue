<template>
  <div class="text-xs-center">
    <v-menu
      min-width="100"
      top
      v-model="menu"
      :close-on-click="false"
      :close-on-content-click="false"
      :nudge-top="60"
      offset-x
    >
      <template v-slot:activator="{ on }">
        <v-fab-transition>
          <v-btn
            v-model="fab"
            v-on="on"
            color="var(--primary-color)"
            @click="
              fab = !fab;
              menu = false;
            "
            style="background-color: #fcfcfc; border: 2px solid #000000"
            fixed
            bottom
            right
            fab
            text
          >
            <v-icon v-if="fab">mdi-close</v-icon>
            <v-icon v-else>mdi-comment</v-icon>
          </v-btn>
        </v-fab-transition>
      </template>
      <v-card
        style="border: 3px solid #000000"
        :height="$vuetify.breakpoint.smAndDown ? '600px' : '700px'"
        :width="$vuetify.breakpoint.smAndDown ? '400px' : '500px'"
      >
        <v-toolbar
          style="border-bottom: 2px solid #000000"
          color="var(--primary-color)"
          flat
        >
          <v-toolbar-title>FEFU Chat</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn
            icon
            @click="
              fab = !fab;
              menu = false;
            "
          >
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-toolbar>

        <v-container fluid style="padding: 0">
          <v-row no-gutters>
            <v-col cols="2" class="scrollable">
              <!-- <chats></chats> -->
              <v-list subheader>
                <v-list-item
                  v-for="(chat, index) in chats"
                  v-bind:key="chat.name"
                  @click="changeChat(index)"
                >
                  <v-list-item-content>
                    <v-list-item-title
                      v-html="chat.name == 'Default' ? '전체' : chat.name"
                    ></v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-col>

            <chat :id="id"></chat>
          </v-row>
        </v-container>
      </v-card>
    </v-menu>
  </div>
</template>

<script>
import Chat from "@/components/Chat/Chat.vue";
import { mapActions, mapGetters } from "vuex";

export default {
  data() {
    return {
      menu: false,
      fab: false,
      id: "0",
    };
  },
  components: {
    Chat,
  },
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
    changeChat(id) {
      this.id = id;
    },
  },
};
</script>

<style lang="scss" scoped>
.chat-background {
  background-color: #ece5dd !important;
}
.chat-header {
  background-color: var(--primary-color) !important;
}
.chip-chat {
  background-color: #dcf8c6 !important;
}
</style>