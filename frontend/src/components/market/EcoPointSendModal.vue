<template>
  <transition name="modal">
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
  </transition>
</template>

<script>
import axios from "axios";
import SERVER from "@/api/api";
import { mapGetters } from "vuex";

export default {
	name: "EcoPointSendModal",
	props: {
		writer: {
			type: String
		}
	},
	data() {
		return {
			point: null,
		}
	},
	computed: {
		...mapGetters("accounts", ["config", "USERNAME"]),
	},
	methods: {
		sendEcoPoint() {
			axios.
				patch(
					SERVER.URL +
						SERVER.ROUTES.accounts.ecopoint,
						{
							"point": Number(this.point),
							"receiver": this.writer,
						},
						{ 
							headers: {
								Authorization: this.config,
							}
						}
				)
				.then(() => {
					this.$emit('close')
				})
				.catch((err) => {console.log(err)})
		}
	}
}
</script>

<style>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  transition: opacity .3s ease;
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
  box-shadow: 0 2px 8px rgba(0, 0, 0, .33);
  transition: all .3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}
</style>