<template>
  <div id="campaign-make">
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
    <v-container class="fill-height" fluid>
      <v-row align="center" justify="center">
        <v-col cols="12" md="10" lg="8">
          <v-stepper v-model="stepper" class="elevation-0"
            ><div class="campaign-make-welcome">
              <v-row align="center" no-gutters>
                <v-col cols="10" md="5"> 캠페인을 등록해주세요🌱!</v-col>
                <v-col cols="2" md="6">
                  <v-stepper-header class="elevation-0">
                    <v-stepper-step
                      class="pa-0"
                      :complete="stepper > 1"
                      step="1"
                      color="#37cdc2"
                    >
                      캠페인 기본정보
                    </v-stepper-step>

                    <v-stepper-step
                      class="pa-0"
                      :complete="stepper > 2"
                      step="2"
                      color="#37cdc2"
                    >
                      캠페인 상세정보
                    </v-stepper-step>
                  </v-stepper-header></v-col
                ></v-row
              >
            </div>
            <v-stepper-items>
              <v-stepper-content step="1" class="pa-0">
                <v-card class="custom-campaign-make-card">
                  <v-card-text>
                    <div class="campaign-make-title">캠페인 기본정보</div>
                    <v-form>
                      <v-row>
                        <v-col cols="12" md="4">
                          <v-file-input
                            label="캠페인 이미지"
                            v-model="images"
                            :roules="imageRules"
                            filled
                            prepend-icon=""
                            append-icon="mdi-camera"
                            color="#37cdc2"
                            accept="image/*"
                            @change="Preview_image"
                          ></v-file-input>
                          <v-img
                            id="Preview_image_create"
                            height="230px"
                            :style="
                              !url
                                ? 'border-bottom: 1px solid rgba(0, 0, 0, 0.42)'
                                : ''
                            "
                            :src="
                              !!url
                                ? url
                                : require('@/assets/images/noimage.jpg')
                            "
                          />
                        </v-col>
                        <v-col cols="12" md="8">
                          <v-text-field
                            v-model="campaign.title"
                            label="캠페인명"
                            name="캠페인명"
                            type="text"
                            required
                            filled
                            autofocus
                            autocapitalize="off"
                            autocorrect="off"
                            autocomplete="off"
                            color="#37cdc2"
                          ></v-text-field>

                          <v-menu
                            ref="menu"
                            v-model="menu"
                            :close-on-content-click="false"
                            :return-value.sync="campaign.startDate"
                            transition="scale-transition"
                            offset-y
                            min-width="290px"
                          >
                            <template v-slot:activator="{ on, attrs }">
                              <v-text-field
                                label="시작날짜"
                                name="시작날짜"
                                required
                                filled
                                v-model="campaign.startDate"
                                readonly
                                v-bind="attrs"
                                v-on="on"
                                color="#37cdc2"
                              ></v-text-field>
                            </template>
                            <v-date-picker
                              v-model="campaign.startDate"
                              no-title
                              scrollable
                            >
                              <v-spacer></v-spacer>
                              <v-btn text color="#37cdc2" @click="menu = false"
                                >취소</v-btn
                              >
                              <v-btn
                                text
                                color="#37cdc2"
                                @click="$refs.menu.save(campaign.startDate)"
                                >선택</v-btn
                              >
                            </v-date-picker>
                          </v-menu>

                          <v-text-field
                            label="종료날짜"
                            name="종료날짜"
                            type="text"
                            required
                            filled
                            disabled
                            autocapitalize="off"
                            autocorrect="off"
                            autocomplete="off"
                            color="#37cdc2"
                          ></v-text-field>

                          <v-combobox
                            label="태그"
                            name="태그"
                            v-model="tags"
                            hide-selected
                            multiple
                            filled
                            small-chips
                            color="#37cdc2"
                          >
                            <template v-slot:selection="data">
                              <v-chip color="#37cdc2" class="white--text">
                                {{ data.item }}
                              </v-chip>
                            </template>
                          </v-combobox>
                        </v-col>
                      </v-row>
                      <v-textarea
                        v-model="campaign.content"
                        label="상세 내용"
                        name="상세 내용"
                        type="text"
                        required
                        filled
                        autocapitalize="off"
                        autocorrect="off"
                        autocomplete="off"
                        color="#37cdc2"
                      ></v-textarea>
                    </v-form>
                  </v-card-text>

                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn class="custom-campaign-make-btn">취소 </v-btn>
                    <v-btn class="custom-campaign-make-btn" @click="stepper = 2"
                      >다음
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-stepper-content>

              <v-stepper-content step="2" class="pa-0">
                <v-card class="custom-campaign-make-card">
                  <v-card-text>
                    <div class="campaign-make-title">캠페인 상세정보</div>
                    <v-form v-if="$route.params.type != 2">
                      <v-text-field
                        v-model="personal.mission"
                        label="인증 미션"
                        name="인증 미션"
                        placeholder="ex) 하루 한가지 환경을 위한 행동을 나눠요"
                        type="text"
                        required
                        filled
                        autofocus
                        autocapitalize="off"
                        autocorrect="off"
                        autocomplete="off"
                        color="#37cdc2"
                      ></v-text-field>
                      <v-text-field
                        v-model="personal.authProcess"
                        label="인증 방법"
                        name="인증 방법"
                        placeholder="ex) 일상 속 친환경 행동 실천하고 인증샷을 올려주세요."
                        type="text"
                        required
                        filled
                        append-outer-icon
                        autocomplete="off"
                        color="#37cdc2"
                      ></v-text-field>

                      <v-text-field
                        v-model="personal.authStartTime"
                        label="인증 시작시간"
                        name="인증 시작시간"
                        type="text"
                        placeholder="ex) 매일 00:00"
                        required
                        filled
                        append-outer-icon
                        autocapitalize="off"
                        autocorrect="off"
                        autocomplete="off"
                        color="#37cdc2"
                      ></v-text-field>
                      <v-text-field
                        v-model="personal.authEndTime"
                        label="인증 종료시간"
                        name="인증 종료시간"
                        type="text"
                        placeholder="ex) 다음날 00:00"
                        required
                        filled
                        append-outer-icon
                        autocapitalize="off"
                        autocorrect="off"
                        autocomplete="off"
                        color="#37cdc2"
                      ></v-text-field>

                      <v-text-field
                        v-model="personal.requirement"
                        label="참여 조건"
                        name="참여 조건"
                        type="text"
                        placeholder="ex) 작은 행동 하나라도 지속적으로 꾸준히 환경보호를 실천해나갈 분"
                        required
                        filled
                        autocapitalize="off"
                        autocorrect="off"
                        autocomplete="off"
                        color="#37cdc2"
                      ></v-text-field>

                      <v-text-field
                        label="참여인원"
                        name="참여인원"
                        type="number"
                        v-model.number="personal.headcount"
                        required
                        filled
                        append-outer-icon
                        autocomplete="off"
                        color="#37cdc2"
                      ></v-text-field>
                    </v-form>
                    <v-form v-else>
                      <v-text-field
                        v-model="company.companyName"
                        label="주최"
                        name="주최"
                        type="text"
                        required
                        filled
                        autocapitalize="off"
                        autocorrect="off"
                        autocomplete="off"
                        color="#37cdc2"
                      ></v-text-field>
                      <v-text-field
                        v-model="company.campaignLink"
                        label="캠페인 링크"
                        name="캠페인 링크"
                        type="text"
                        placeholder="ex) 캠페인 링크를 작성해주세요."
                        required
                        filled
                        autocapitalize="off"
                        autocorrect="off"
                        autocomplete="off"
                        color="#37cdc2"
                      ></v-text-field>
                    </v-form>
                  </v-card-text>

                  <v-card-actions>
                    <v-spacer></v-spacer>

                    <v-btn class="custom-campaign-make-btn" @click="stepper = 1"
                      >이전
                    </v-btn>
                    <v-btn
                      class="custom-campaign-make-btn"
                      @click="registCampaign"
                      >등록
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-stepper-content>
            </v-stepper-items>
          </v-stepper>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";
import SERVER from "@/api/api";
import { mapGetters } from "vuex";
import router from "@/router";

export default {
  name: "CampaignMakeView",
  data() {
    return {
      menu: false,
      campaign: {
        title: "",
        content: "",
        startDate: new Date().toISOString().substr(0, 10),
        endDate: "2022-09-11",
        type: "",
        writer: "",
        photo: "",
      },
      tags: JSON.stringify(this.tags),
      personal: {
        mission: "",
        authProcess: "",
        authStartTime: "",
        authEndTime: "",
        headcount: null,
        requirement: "",
      },
      company: {
        companyName: "",
        campaignLink: "",
      },
      stepper: 1,
      url: null,
      images: null,
      imageRules: [
        (value) =>
          !value ||
          value.size < 2000000 ||
          "이미지 파일은 최대 2 MB까지 가능해요",
      ],
    };
  },
  computed: {
    ...mapGetters("accounts", ["config", "USERNAME"]),

    getCampaignType() {
      let campaignType = "";
      if (this.$route.params.type == 1) {
        campaignType = "personal";
      } else if (this.$route.params.type == 2) {
        campaignType = "company";
      } else {
        campaignType = "official";
      }
      return campaignType;
    },
  },
  methods: {
    Preview_image() {
      if (!this.images) {
        this.url = null;
      } else {
        this.url = URL.createObjectURL(this.images);
      }
    },

    registCampaign: async function () {
      let body = {};
      this.campaign.type = this.getCampaignType;

      if (this.$route.params.type == 2) {
        body = {
          campaign: this.campaign,
          tag: this.tags,
          company: this.company,
        };
      } else if (this.$route.params.type == 1) {
        body = {
          campaign: this.campaign,
          tag: this.tags,
          personal: this.personal,
        };
      } else {
        body = {
          campaign: this.campaign,
          tag: this.tags,
          official: this.personal,
        };
      }

      this.campaign.writer = this.USERNAME;
      await this.uploadImage();
      await axios
        .post(SERVER.URL + SERVER.ROUTES.campaigns.URL + "/", body, {
          headers: {
            Authorization: this.config,
          },
        })
        .then(() => {
          alert("캠페인 등록 완료 되었습니다.");
          router.push({ name: "CampaignMain" });
        })
        .catch((err) => {
          console.log(err);
        });
      console.log(body);
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
          this.campaign.photo = res.data.fileName;
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },

    imageSrc(filename) {
      return SERVER.IMAGE_URL + filename;
    },

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
  },
};
</script>

<style lang="scss" scoped>
.campaign-make-welcome {
  border: 2px solid black;
  border-radius: 5px;
  padding: 10px 20px;
  margin: 10px 0;
  text-align: start;
  font-size: 1.3rem;
  font-family: "NanumBarunpen";
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.16), 0 1px 5px rgba(0, 0, 0, 0.23);
}

.campaign-make-title {
  text-align: start;
  font-size: 1.3rem;
  font-family: "NanumBarunpen";
  margin-bottom: 20px;
}

.custom-campaign-make-card {
  font-family: "NanumBarunpen";
  border: 2px solid black;
  padding: 10px 5px;
}

.custom-campaign-make-btn {
  border: 2px solid black;
  background: var(--primary-color);
}
</style>