<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container" v-if="this.product.status == 0">
          <div class="modal-header">
            <slot name="header"> 판매를 축하드려요!! </slot>
          </div>

          <div class="modal-body">
            <slot name="body">
              누가 구매했나요?
              <input v-model="buyer" />
            </slot>
          </div>

          <div class="modal-footer">
            <slot name="footer">
              <button class="modal-default-button" @click="changeProductStatus">
                제출
              </button>
              <button class="modal-default-button" @click="$emit('close')">
                취소
              </button>
            </slot>
          </div>
        </div>

        <div class="modal-container" v-if="this.product.status == 1">
          <div class="modal-header">
            <slot name="header"> 판매 상태를 변경하시겠어요? </slot>
          </div>

          <div class="modal-body">
            <slot name="body"> 판매글이 판매중으로 변경됩니다. </slot>
          </div>

          <div class="modal-footer">
            <slot name="footer">
              <button class="modal-default-button" @click="changeProductStatus">
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
  </transition>
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
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 300px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}



</style>