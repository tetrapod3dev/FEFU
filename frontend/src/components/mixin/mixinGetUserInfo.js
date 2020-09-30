import axios from "axios";
import SERVER from "@/api/api";
import { mapGetters } from "vuex";

export const mixinGetUserInfo = {
  computed: {
    ...mapGetters("accounts", ["config", "USERNAME"]),
  },
  methods: {
    async getUserInfo() {
      let configs = {
        headers: {
          Authorization: this.config,
        },
      };
      return await axios.get(
        SERVER.URL + SERVER.ROUTES.accounts.URL + "/" + this.USERNAME,
        configs
      );
    },
  },
};
