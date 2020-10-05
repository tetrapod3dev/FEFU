<template>
  <div>
    <v-dialog
      v-if="product.status == 0"
      v-model="dialog"
      persistent
      max-width="300px"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn class="product-state" outlined tile v-bind="attrs" v-on="on">
          판매 중
        </v-btn>
      </template>
      <v-card style="border: 3px solid #000000">
        <v-card-title
          style="
            background-color: var(--primary-color);
            border-bottom: 2px solid #000000;
          "
          class="justify-center headline"
        >
          판매 처리
        </v-card-title>
        <v-card-text class="py-0">
          <v-container class="pb-0">
            <v-row>
              <v-col cols="12" class="text-left"> 구매자를 알려주세요 </v-col>
              <v-col cols="12">
                <v-form ref="form">
                  <v-text-field
                    v-model="buyer"
                    label="제품 구매자"
                    name="제품 구매자"
                    type="text"
                    required
                    filled
                    autofocus
                    autocapitalize="off"
                    autocorrect="off"
                    autocomplete="off"
                    color="#37cdc2"
                    :rules="[(v) => !!v || '구매자를 넣어주세요']"
                  ></v-text-field>
                </v-form>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions class="px-5">
          <v-spacer></v-spacer>
          <v-btn class="c-btn" text @click="dialog = false"> 취소 </v-btn>
          <v-btn class="c-btn" text @click="changeProductStatus"> 제출 </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-else v-model="dialog" persistent max-width="300px">
      <template v-slot:activator="{ on, attrs }">
        <v-btn class="product-state" outlined tile v-bind="attrs" v-on="on">
          판매 완료
        </v-btn>
      </template>
      <v-card style="border: 3px solid #000000">
        <v-card-title
          style="
            background-color: var(--primary-color);
            border-bottom: 2px solid #000000;
          "
          class="justify-center headline"
        >
          판매상태 변경
        </v-card-title>
        <v-card-text class="py-0">
          <v-col cols="12" class="text-left">
            다시 판매중으로 바꾸실 건가요?
          </v-col>
        </v-card-text>
        <v-card-actions class="px-5">
          <v-spacer></v-spacer>
          <v-btn class="c-btn" text @click="dialog = false"> 취소 </v-btn>
          <v-btn class="c-btn" text @click="changeProductStatus"> 제출 </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from "axios";
import SERVER from "@/api/api";
import { mapGetters } from "vuex";

export default {
  name: "SoldModal",
  props: {
    product: {
      type: Object,
    },
  },
  data() {
    return {
      buyer: "",
      dialog: false,
    };
  },
  computed: {
    ...mapGetters("accounts", ["config", "USERNAME"]),
  },
  methods: {
    changeProductStatus() {
      axios
        .patch(
          SERVER.URL + "/products/" + this.product.no + "/sold/",
          {
            buyer: this.buyer,
          },
          {
            headers: {
              Authorization: this.config,
            },
          }
        )
        .then(() => {
          // console.log(res.data)
          this.$router.go();
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>
.c-btn {
  font-family: "S-CoreDream-7ExtraBold";
  border: 2px solid black;
  border-radius: 10px;
}

.product-state {
  border: 2px solid black;
  border-radius: 10px;
  padding: 5px 10px;
}
</style>