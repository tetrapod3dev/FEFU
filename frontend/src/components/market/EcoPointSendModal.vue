<template>
  <v-dialog v-model="dialog" persistent max-width="300px">
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        v-if="product.status == 0"
        class="product-state"
        outlined
        tile
        v-bind="attrs"
        v-on="on"
      >
        판매 중
      </v-btn>
      <v-btn
        v-else
        class="product-state"
        outlined
        tile
        disabled
        v-bind="attrs"
        v-on="on"
      >
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
        에코 포인트를 전송하시겠습니까?
      </v-card-title>
      <v-card-text class="py-0">
        <v-container class="pb-0">
          <v-row>
            <v-col cols="12" class="text-left">
              전송할 에코포인트를 입력해주세요!
            </v-col>
            <v-col cols="12">
              <div>
                <v-text-field
                  v-model="point"
                  label="에코 포인트"
                  name="에코 포인트"
                  type="number"
                  required
                  filled
                  autofocus
                  autocapitalize="off"
                  autocorrect="off"
                  autocomplete="off"
                  color="#37cdc2"
                  :rules="[(v) => !!v || '에코 포인트를 입력해주세요']"
                  @keydown.enter="sendEcoPoint"
                ></v-text-field>
              </div>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions class="px-5">
        <v-spacer></v-spacer>
        <v-btn class="c-btn" text @click="dialog = false"> 취소 </v-btn>
        <v-btn class="c-btn" text @click="sendEcoPoint"> 제출 </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
  <!-- <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">

          <div class="modal-header">
            <slot name="header">
              에코 포인트를 전송하시겠습니까?
            </slot>
          </div>

          <div class="modal-body">
            <slot name="body">
              전송할 에코포인트를 입력해주세요!
							<input v-model="point"/>
            </slot>
          </div>

          <div class="modal-footer">
            <slot name="footer">
							<button class="modal-default-button" @click="sendEcoPoint">
                제출
              </button>
              <button class="modal-default-button" @click="$emit('close')">
                취소
              </button>
            </slot>
          </div>
        </div>
      </div>
    </div>
  </transition> -->
</template>

<script>
import axios from "axios";
import SERVER from "@/api/api";
import { mapGetters } from "vuex";

export default {
  name: "EcoPointSendModal",
  props: {
    writer: {
      type: String,
    },
    product: {
      type: Object,
    },
  },
  data() {
    return {
      dialog: false,
      point: null,
    };
  },
  computed: {
    ...mapGetters("accounts", ["config", "USERNAME"]),
  },
  methods: {
    sendEcoPoint() {
      if (this.point < 0) {
        alert('전송 가능한 최소 에코포인트는 1포인트입니다.');
        this.point = null;
        return
      } else if (this.point > this.product.eco_point) {
        alert('최대 전송 가능한 에코포인트는' + this.product.eco_point + '입니다.');
        this.point = null;
        return
      }

      axios
        .patch(
          SERVER.URL + SERVER.ROUTES.accounts.ecopoint,
          {
            point: Number(this.point),
            receiver: this.writer,
          },
          {
            headers: {
              Authorization: this.config,
            },
          }
        )
        .then((res) => {
          this.dialog = false;
          if (res.data == "전송실패") {
            alert("보유중인 에코포인트보다 많은 에코포인트를 입력하셨습니다.");
          } else {
            alert("에코포인트 전송에 성공했습니다!\n\n유저 아이디: " + this.writer + " / 에코포인트: " + this.point);
          }
          this.point = null;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style lang="scss" scoped>
.product-state {
  border: 2px solid black;
  border-radius: 10px;
  padding: 5px 10px;
}

.c-btn {
  font-family: "S-CoreDream-7ExtraBold";
  border: 2px solid black;
  border-radius: 10px;
}
</style>