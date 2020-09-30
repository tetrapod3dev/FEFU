<template>
  <div id="campaign-list">
    <section id="section-hero">
      <v-img
        id="about-hero"
        style="position: absolute"
        position="top"
        :height="$vuetify.breakpoint.smAndDown ? '24vh' : '49vh'"
        src="@/assets/images/campaign-hero.jpg"
        lazy-src="@/assets/images/lazy-loading.jpg"
      >
        <template v-slot:placeholder>
          <v-row class="fill-height ma-0" align="center" justify="center">
            <v-progress-circular
              indeterminate
              color="grey lighten-5"
            ></v-progress-circular>
          </v-row>
        </template>
      </v-img>
      <v-img
        style="position: relative; z-index: 3"
        position="bottom"
        :height="$vuetify.breakpoint.smAndDown ? '25vh' : '50vh'"
        src="@/assets/illust/campaign-hero.svg"
      />
    </section>

    <v-container>
      <v-row>
        <v-col cols="12" sm="3">
          <div :class="$vuetify.breakpoint.smAndDown ? '' : 'fixed-bar'">
            <!-- 사이드바 -->
            <SideBar :campaign="campaign" />

            <v-dialog v-model="dialog" persistent max-width="600px">
              <template v-slot:activator="{ on, attrs }">
                <button class="custom-make-btn" v-bind="attrs" v-on="on">
                  인증글 작성
                </button>
              </template>
              <v-card>
                <v-card-title>
                  <span class="headline">인증글 작성</span>
                </v-card-title>
                <v-card-text class="py-0">
                  <v-container class="pb-0">
                    <v-row>
                      <v-col cols="12" class="py-0">
                        <v-img
                          id="Preview_image_create"
                          height="230px"
                          :style="
                            !url
                              ? 'border-bottom: 1px solid rgba(0, 0, 0, 0.42)'
                              : ''
                          "
                          :src="
                            !!url ? url : require('@/assets/images/noimage.jpg')
                          "
                        />
                        <v-file-input
                          class="mt-5"
                          label="오늘의 미션 인증 사진"
                          v-model="images"
                          :roules="imageRules"
                          filled
                          prepend-icon=""
                          append-icon="mdi-camera"
                          color="#37cdc2"
                          accept="image/*"
                          @change="Preview_image"
                        ></v-file-input>
                      </v-col>

                      <v-col cols="12" class="py-0">
                        <v-text-field
                          v-model="proofPost.title"
                          label="인증글 제목"
                          name="인증글 제목"
                          type="text"
                          required
                          filled
                          autofocus
                          autocapitalize="off"
                          autocorrect="off"
                          autocomplete="off"
                          color="#37cdc2"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" class="py-0">
                        <v-textarea
                          v-model="proofPost.content"
                          label="내용"
                          name="내용"
                          type="text"
                          required
                          filled
                          autocapitalize="off"
                          autocorrect="off"
                          autocomplete="off"
                          color="#37cdc2"
                        ></v-textarea>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-card-text>
                <v-card-actions class="px-5">
                  <v-btn color="blue darken-1" text @click="dialog = false">
                    취소
                  </v-btn>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" text @click="registProof">
                    등록
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </div>
        </v-col>

        <v-col cols="12" sm="9" class="pt-0">
          <v-container justify="start">
            <div class="campaign-welcome">
              <span class="campaign-title">{{ campaign.title }}</span>
              <small class="ml-3">
                {{ campaign.startDate }} - {{ campaign.endDate }}
              </small>
            </div>

            <div class="campaign-info d-flex flex-column">
              <UserCertificatePosts />
            </div>
          </v-container>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import UserCertificatePosts from "@/components/campaign/UserCertificatePosts.vue";
import SideBar from "@/components/campaign/SideBar.vue";

import axios from "axios";
import SERVER from "@/api/api";
import router from "@/router";
import { mapGetters } from "vuex";

export default {
  components: {
    UserCertificatePosts,
    SideBar,
  },
  created() {
    this.checkusername();
  },
  mounted() {
    this.getCampaign();
  },
  computed: { ...mapGetters("accounts", ["config"]) },
  data() {
    return {
      listColorName: [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "purple",
      ],
      items: [
        { name: "캠페인소개", link: "CampaignDetail" },
        { name: "인증현황", link: "CampaignCertifi" },
        { name: "인증게시판", link: "CampaignPostings" },
      ],
      campaign: {
        title: "",
        content: "",
        writer: "",
        startDate: "",
        endDate: "",
        photo: "",
        tag: [],
        type: "",
        no: 0,
      },
      campaignTypeInfo: {
        authEndTime: "",
        authProcess: "",
        authStartTime: "",
        campaignNo: null,
        headcount: null,
        mission: "",
        no: null,
        requirement: "",
      },
      url: null,
      images: null,
      imageRules: [
        (value) =>
          !value ||
          value.size < 2000000 ||
          "이미지 파일은 최대 2 MB까지 가능해요",
      ],
      proofPost: {
        campaignNo: null,
        title: "",
        content: "",
        photo: "",
        writer: "",
      },
      dialog: false,
      user: null,
    };
  },
  methods: {
    getUserInfo() {
      let configs = {
        headers: {
          Authorization: this.config,
        },
      };
      axios
        .get(SERVER.URL + SERVER.ROUTES.myPage, configs)
        .then((res) => {
          this.user = res.data.user;
        })
        .catch((err) => console.log(err.response));
    },
    Preview_image() {
      if (!this.images) {
        this.url = null;
      } else {
        this.url = URL.createObjectURL(this.images);
      }
    },
    imageSrc(filename) {
      return SERVER.IMAGE_URL + filename;
    },
    checkusername() {
      var base64Url = this.config.split(".")[1];
      var decodedValue = JSON.parse(window.atob(base64Url));
      this.proofPost.writer = decodedValue.sub;
      console.log(this.proofPost.writer);
      // this.authority = decodedValue.role[0]
    },

    registProof: async function() {
      await this.checkusername();
      await this.uploadImage();
      await axios
        .post(
          SERVER.URL + SERVER.ROUTES.campaigns.URL + "/proof/",
          this.proofPost,
          {
            headers: {
              Authorization: this.config,
            },
          }
        )
        .then(() => {
          alert("캠페인 등록 완료 되었습니다.");
          this.dialog = false;
          router
            .push({ name: "CampaignPostings" })
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
    },

    async uploadImage() {
      let configs = {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      };

      let file = this.images;
      let formData = new FormData();
      formData.append("file", file);

      await axios
        .post(SERVER.URL + SERVER.ROUTES.images.upload, formData, configs)
        .then((res) => {
          this.proofPost.photo = res.data.fileName;
        })
        .catch((err) => {
          console.log(err);
        });
    },

    getCampaign() {
      axios
        .get(
          SERVER.URL +
            SERVER.ROUTES.campaigns.URL +
            "/" +
            this.$route.params.campaignNo +
            "/"
        )
        .then((res) => {
          this.campaign = res.data["campaign"];
          this.proofPost.campaignNo = res.data["campaign"].no;
          if (res.data["official"]) {
            this.campaignTypeInfo = res.data["official"];
          } else if (res.data["personal"]) {
            this.campaignTypeInfo = res.data["personal"];
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style lang="scss" scoped>
.campaign-welcome {
  border: 2px solid black;
  border-radius: 5px;
  padding: 10px 20px;
  margin: 10px 0;
  text-align: start;
}

.campaign-header-img {
  border: 2px solid black;
  border-radius: 15px;
}

.campaign-title {
  font-size: 1.5rem;
  font-family: "NanumBarunpen";
}

.capmaign-info {
  font-family: "NanumBarunpen";
}

.custom-list {
  margin-top: 20px;
  font-family: "S-CoreDream-7ExtraBold";
}

.campaign-info-list {
  font-family: "S-CoreDream-7ExtraBold";
  border: 2px solid black;
  border-radius: 10px;
  padding: 5px 0;
}

.custom-list-item {
  border: 2px solid black;
  &:first-child {
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
  }
  &:last-child {
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
  }

  &:not(:last-child) {
    // border-bottom: 2px solid black;
    margin-bottom: -2px;
  }

  &-red.v-list-group--active,
  &-red:hover {
    background: #cf6a87;
  }

  &-orange.v-list-group--active,
  &-orange:hover {
    background: #f19066;
  }

  &-yellow.v-list-group--active,
  &-yellow:hover {
    background: #fdcb6e;
  }

  &-green.v-list-group--active,
  &-green:hover {
    background: #b8e994;
  }

  &-blue.v-list-group--active,
  &-blue:hover {
    background: #82ccdd;
  }

  &-indigo.v-list-group--active,
  &-indigo:hover {
    background: #60a3bc;
  }

  &-purple.v-list-group--active,
  &-purple:hover {
    background: #786fa6;
  }
}

.custom-white {
  background: var(--white-color);
}

.custom-make-btn {
  font-family: "S-CoreDream-7ExtraBold";
  font-size: 1rem;
  width: 100%;
  height: 48px;
  margin-top: 20px;
  background-color: var(--primary-color);
  border: 2px solid black;
  border-radius: 10px;
  text-align: center;
}
</style>
