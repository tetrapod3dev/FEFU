<template>
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
                  <v-form ref="form">
                    <v-row>
                      <v-col cols="12" md="4">
                        <v-file-input
                          label="캠페인 이미지"
                          ref="imageInput"
                          v-model="images"
                          :rules="imageRules"
                          filled
                          prepend-icon=""
                          append-icon="mdi-camera"
                          color="#37cdc2"
                          accept="image/*"
                          @change="Preview_image"
                        ></v-file-input>
                        <v-img
                          @click="onClickImageUpload"
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
                      </v-col>
                      <v-col cols="12" md="8">
                        <v-text-field
                          v-model="campaign.title"
                          label="캠페인명"
                          name="캠페인명"
                          type="text"
                          :rules="[(v) => !!v || '캠페인명을 적어주세요']"
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
                              :rules="[startDateRules]"
                              readonly
                              v-bind="attrs"
                              v-on="on"
                              color="#37cdc2"
                            ></v-text-field>
                          </template>
                          <v-date-picker
                            v-model="campaign.startDate"
                            color="var(--primary-color)"
                            no-title
                            scrollable
                          >
                            <v-spacer></v-spacer>
                            <v-btn
                              text
                              color="#37cdc2"
                              @click="this.menu = false"
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

                        <v-menu
                          ref="menu2"
                          v-model="menu2"
                          :close-on-content-click="false"
                          :return-value.sync="campaign.endDate"
                          transition="scale-transition"
                          offset-y
                          min-width="290px"
                        >
                          <template v-slot:activator="{ on, attrs }">
                            <v-text-field
                              label="종료날짜"
                              name="종료날짜"
                              required
                              filled
                              :disabled="$route.params.type == 1"
                              v-model="add100Day"
                              :rules="[endDateRules]"
                              readonly
                              v-bind="attrs"
                              v-on="on"
                              color="#37cdc2"
                            ></v-text-field>
                          </template>
                          <v-date-picker
                            v-model="add100Day"
                            color="var(--primary-color)"
                            no-title
                            scrollable
                          >
                            <v-spacer></v-spacer>
                            <v-btn
                              text
                              color="#37cdc2"
                              @click="this.menu2 = false"
                              >취소</v-btn
                            >
                            <v-btn
                              text
                              color="#37cdc2"
                              @click="$refs.menu2.save(campaign.endDate)"
                              >선택</v-btn
                            >
                          </v-date-picker>
                        </v-menu>

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
                      :rules="[(v) => !!v || '캠페인명에 대해 이야기해보세요']"
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
                  <v-btn
                    class="custom-campaign-make-btn"
                    :to="{ name: 'CampaignMain' }"
                    >취소
                  </v-btn>
                  <v-btn class="custom-campaign-make-btn" @click="preTest"
                    >다음
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-stepper-content>

            <v-stepper-content step="2" class="pa-0">
              <v-card class="custom-campaign-make-card">
                <v-card-text>
                  <div class="campaign-make-title">캠페인 상세정보</div>
                  <v-form ref="formType1n3" v-if="$route.params.type != 2">
                    <v-text-field
                      v-model="personal.mission"
                      label="인증 미션"
                      name="인증 미션"
                      placeholder="ex) 하루 한가지 환경을 위한 행동을 나눠요"
                      type="text"
                      :rules="[(v) => !!v || '미션을 정해봐요']"
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
                      :rules="[(v) => !!v || '인증 방법을 적어주세요']"
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
                      :rules="[(v) => !!v || '인증 시작 시간을 알려주세요']"
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
                      :rules="[(v) => !!v || '인증 종료 시간을 알려주세요']"
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
                      :rules="[
                        (v) => !!v || '어떤 사람이 참여했으면 좋겠나요?',
                      ]"
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
                      :rules="[(v) => !!v || '몇 명이서 함께 하고 싶나요?']"
                      required
                      filled
                      append-outer-icon
                      autocomplete="off"
                      color="#37cdc2"
                    ></v-text-field>
                  </v-form>
                  <v-form v-else ref="formType2">
                    <v-text-field
                      v-model="company.companyName"
                      label="주최"
                      name="주최"
                      type="text"
                      :rules="[
                        (v) => !!v || '어느 회사가 환경에 관심을 가지나요?',
                      ]"
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
                      :rules="[(v) => !!v || '어떻게 찾아가는지 알려주세요']"
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
</template>

<script>
import axios from "axios";
import SERVER from "@/api/api";
import { mapActions, mapGetters } from "vuex";
import router from "@/router";
import { mixinUploadImage } from "@/components/mixin/mixinUploadImage";

export default {
  name: "CampaignMakeView",
  mixins: [mixinUploadImage],
  data() {
    return {
      menu: false,
      menu2: false,
      campaign: {
        title: "",
        content: "",
        startDate: new Date().toISOString().substr(0, 10),
        endDate: new Date().toISOString().substr(0, 10),
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
      imageRules: [(v) => !!v || "이미지 파일을 등록해주세요"],
    };
  },
  created() {
    if (this.$route.params.type == 1) {
      this.campaign.endDate = this.add100Day;
    }
    if (!this.isLoggedIn) {
      alert('로그인 해주세요!');
      router.push({ name: "Home" });
    }
  },
  computed: {
    ...mapGetters("accounts", ["config", "USERNAME", "isLoggedIn"]),

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
    add100Day() {
      let nowStartDate = new Date(this.campaign.startDate);
      let resultDate = new Date();
      resultDate.setDate(nowStartDate.getDate() + 100);
      return resultDate.toISOString().substr(0, 10);
    },
    startDateRules() {
      return (
        new Date().toISOString().substr(0, 10) <= this.campaign.startDate ||
        "시작 날짜는 오늘부터 가능합니다"
      );
    },
    endDateRules() {
      return (
        this.campaign.startDate <= this.campaign.endDate ||
        "종료 날짜는 시작 날짜보다 더 늦어야 해요"
      );
    },
  },
  methods: {
    ...mapActions("accounts", ["logout"]),
    onClickImageUpload() {
      this.$refs.imageInput.$refs.input.click()
    },
    Preview_image() {
      if (!this.images) {
        this.url = null;
      } else {
        this.url = URL.createObjectURL(this.images);
      }
      this.preUploadImage();
    },
    preTest() {
      if (this.$refs.form.validate()) {
        this.stepper = 2;
      }
    },
    async registCampaign() {
      if (this.$route.params.type == 2) {
        if (!this.$refs.formType2.validate()) {
          return;
        }
      } else {
        if (!this.$refs.formType1n3.validate()) {
          return;
        }
      }
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

      body.campaign.endDate = this.add100Day

      this.campaign.writer = this.USERNAME;
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
        .catch(() => {
          alert("로그인 정보가 만료되었습니다 ㅠㅠ 다시 입력해주세요..");
          this.logout();
        });
    },

    preUploadImage() {
      this.uploadImage(this.images)
        .then((res) => {
          this.campaign.photo = res.data.fileName;
        })
        .catch((err) => {
          console.log(err);
        });
    },

    imageSrc(filename) {
      return SERVER.IMAGE_URL + filename;
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

#Preview_image_create {
  cursor: pointer;
}
</style>