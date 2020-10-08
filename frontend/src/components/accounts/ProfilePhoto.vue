<template>
  <div>
    <v-dialog v-model="dialog" persistent max-width="300px">
      <template v-slot:activator="{ on, attrs }">
        <div
          class="mr-auto ml-auto"
          :class="$vuetify.breakpoint.smAndDown ? 'ml-auto' : ''"
          style="position: relative; width: 200px; height: 200px"
        >
          <!-- 사이드바 -->
          <v-img
            class="c-sidebar c-sidebar__img mr-auto mb-5"
            :class="$vuetify.breakpoint.smAndDown ? 'ml-auto' : ''"
            height="200px"
            width="200px"
            style="cursor: pointer"
            v-bind="attrs"
            v-on="on"
            @mouseenter="isShowIcon = true"
            @mouseleave="isShowIcon = false"
            :src="
              !!userinfo.profileImage
                ? imageSrc(userinfo.profileImage)
                : require(`@/assets/images/${userinfo.gender}.png`)
            "
            lazy-src="@/assets/images/lazy-loading.jpg"
          >
            <template v-slot:placeholder>
              <lazy-loading />
            </template>
          </v-img>

          <v-icon
            v-if="isShowIcon"
            style="
              position: absolute;
              right: 8%;
              bottom: 8%;
              background: var(--primary-color);
              height: 32px;
              width: 32px;
              border-radius: 50%;
            "
            color="#ffffff"
            >mdi-camera</v-icon
          >
        </div>
      </template>
      <v-card style="border: 3px solid #000000">
        <v-card-title
          style="
            background-color: var(--primary-color);
            border-bottom: 2px solid #000000;
          "
          class="justify-center headline"
        >
          프로필 사진 수정
        </v-card-title>
        <v-card-text class="py-0">
          <v-container class="pb-0">
            <v-row>
              <v-col cols="12" class="py-0">
                <v-form ref="form">
                  <v-img
                    @click="onClickImageUpload"
                    id="Preview_image_create"
                    class="c-sidebar c-sidebar__img mr-auto ml-auto"
                    height="200px"
                    width="200px"
                    :src="
                      !!url
                        ? url
                        : !!userinfo.profileImage
                        ? imageSrc(userinfo.profileImage)
                        : require(`@/assets/images/${userinfo.gender}.png`)
                    "
                    lazy-src="@/assets/images/lazy-loading.jpg"
                  >
                    <template v-slot:placeholder>
                      <lazy-loading />
                    </template>
                  </v-img>
                  <v-file-input
                    class="mt-5"
                    label="프로필 사진"
                    ref="imageInput"
                    v-model="images"
                    :rules="[(v) => !!v || '이미지를 등록해주세요']"
                    filled
                    prepend-icon=""
                    append-icon="mdi-camera"
                    color="#37cdc2"
                    accept="image/*"
                    @change="Preview_image"
                  />
                </v-form>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions class="px-5">
          <v-spacer></v-spacer>
          <v-btn class="c-btn" text @click="dialog = false"> 취소 </v-btn>
          <v-btn class="c-btn" text @click="updateProfile"> 수정 </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from "axios";
import SERVER from "@/api/api";
import router from "@/router";
import { mapGetters } from "vuex";
import { mixinUploadImage } from "@/components/mixin/mixinUploadImage";

export default {
  props: ["userinfo"],
  mixins: [mixinUploadImage],
  data() {
    return {
      isShowIcon: false,
      dialog: false,
      images: null,
      url: null,
      photo: "",
    };
  },
  computed: {
    ...mapGetters("accounts", ["config"]),
  },
  methods: {
    onClickImageUpload() {
      this.$refs.imageInput.$refs.input.click()
    },
    imageSrc(filename) {
      return SERVER.IMAGE_URL + filename;
    },
    Preview_image() {
      if (!this.images) {
        this.url = null;
      } else {
        this.url = URL.createObjectURL(this.images);
      }
      this.preUploadImage();
    },
    preUploadImage() {
      this.uploadImage(this.images)
        .then((res) => {
          this.photo = res.data.fileName;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async updateProfile() {
      if (this.$refs.form.validate()) {
        await axios
          .patch(
            SERVER.URL + SERVER.ROUTES.accounts.URL + "/",
            {
              nickname: this.userinfo.nickname,
              age: this.userinfo.age,
              gender: this.userinfo.gender,
              profileImage: this.photo,
              introduce: this.userinfo.introduce,
            },
            {
              headers: {
                Authorization: this.config,
              },
            }
          )
          .then(() => {
            this.dialog = false;
            router
              .push({ name: "MypageInfo" })
              .then(() => {
                location.reload();
              })
              .catch((error) => {
                if (error.name === "NavigationDuplicated") {
                  location.reload();
                }
              });
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.c-sidebar {
  border: 2px solid black;
  border-radius: 10px;
  &__img {
    border-radius: 50%;
  }
}

.c-btn {
  font-family: "S-CoreDream-7ExtraBold";
  border: 2px solid black;
  border-radius: 10px;
}

#Preview_image_create {
  cursor: pointer;
}
</style>
