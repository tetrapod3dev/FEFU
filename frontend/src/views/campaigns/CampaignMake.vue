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
                            v-model="image"
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
                            :src="
                              !!url
                                ? url
                                : require('@/assets/images/noimage.jpg')
                            "
                          />
                        </v-col>
                        <v-col cols="12" md="8">
                          <v-text-field
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
                          <v-text-field
                            label="참여인원"
                            name="참여인원"
                            type="number"
                            required
                            filled
                            append-outer-icon
                            autocomplete="off"
                            color="#37cdc2"
                          ></v-text-field>

                          <v-text-field
                            label="시작날짜"
                            name="시작날짜"
                            type="number"
                            required
                            filled
                            append-outer-icon
                            autocapitalize="off"
                            autocorrect="off"
                            autocomplete="off"
                            color="#37cdc2"
                          ></v-text-field>

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
                        </v-col>
                      </v-row>
                      <v-textarea
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
                    <v-form>
                      <v-text-field
                        label="인증 미션"
                        name="인증 미션"
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
                        label="인증 방법"
                        name="인증 방법"
                        type="text"
                        required
                        filled
                        append-outer-icon
                        autocomplete="off"
                        color="#37cdc2"
                      ></v-text-field>

                      <v-text-field
                        label="인증 시간"
                        name="인증 시간"
                        type="text"
                        required
                        filled
                        append-outer-icon
                        autocapitalize="off"
                        autocorrect="off"
                        autocomplete="off"
                        color="#37cdc2"
                      ></v-text-field>

                      <v-text-field
                        label="참여 조건"
                        name="참여 조건"
                        type="text"
                        required
                        filled
                        autocapitalize="off"
                        autocorrect="off"
                        autocomplete="off"
                        color="#37cdc2"
                      ></v-text-field>

                      <v-combobox
                        label="태그"
                        name="태그"
                        v-model="compaign.tags"
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
                    </v-form>
                  </v-card-text>

                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn class="custom-campaign-make-btn" @click="stepper = 1"
                      >이전
                    </v-btn>
                    <v-btn class="custom-campaign-make-btn" @click="stepper = 1"
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
export default {
  name: "CampaignMakeView",
  data() {
    return {
      compaign: {
        tags: [],
      },
      stepper: 1,
      url: null,
      image: null,
      imageRules: [
        (value) =>
          !value ||
          value.size < 2000000 ||
          "이미지 파일은 최대 2 MB까지 가능해요",
      ],
    };
  },
  methods: {
    Preview_image() {
      if (!this.image) {
        this.url = null;
      } else {
        this.url = URL.createObjectURL(this.image);
      }
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