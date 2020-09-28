<template>
  <div id="market-make">
    <section id="section-hero">
      <v-img
        id="about-hero"
        style="position: absolute"
        position="top"
        :height="$vuetify.breakpoint.smAndDown ? '24vh' : '49vh'"
        src="@/assets/images/market-hero.jpg"
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
        src="@/assets/illust/market-hero.svg"
      />
    </section>
    <v-container class="fill-height" fluid>
      <v-row align="center" justify="center">
        <v-col cols="12" md="10" lg="8">
          <div class="market-make-welcome">상품을 등록해주세요🧾!</div>
          <v-card class="custom-market-make-card">
            <v-card-text>
              <div class="market-make-title">카테고리</div>
              <v-form>
                <v-row no-gutters>
                  <v-col cols="4">
                    <v-select
                      label="대분류"
                      :menu-props="{ bottom: true, offsetY: true }"
                      required
                      filled
                      autofocus
                      color="#37cdc2"
                    ></v-select>
                  </v-col>
                  <v-col cols="4">
                    <v-select
                      label="중분류"
                      :menu-props="{ bottom: true, offsetY: true }"
                      required
                      filled
                      autofocus
                      color="#37cdc2"
                    ></v-select
                  ></v-col>
                  <v-col cols="4">
                    <v-select
                      label="소분류"
                      :menu-props="{ bottom: true, offsetY: true }"
                      required
                      filled
                      autofocus
                      color="#37cdc2"
                    ></v-select
                  ></v-col>
                </v-row>
                <v-row>
                  <v-col cols="4">
                    <v-file-input
                      label="상품 이미지"
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
                        url ? url : 'https://cdn-ds.com/noimage/noimage.jpg'
                      "
                    />
                  </v-col>
                  <v-col cols="8">
                    <v-text-field
                      label="상품명"
                      name="상품명"
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
                      label="판매금액"
                      name="판매금액"
                      type="number"
                      required
                      filled
                      append-outer-icon
                      autocomplete="off"
                      color="#37cdc2"
                    ></v-text-field>

                    <v-text-field
                      label="에코포인트"
                      name="에코포인트"
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
                      label="판매자 연락 방법"
                      name="판매자 연락 방법"
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
                </v-row>
                <v-textarea
                  label="상세 내용"
                  name="상세 내용"
                  type="text"
                  required
                  filled
                  autofocus
                  autocapitalize="off"
                  autocorrect="off"
                  autocomplete="off"
                  color="#37cdc2"
                ></v-textarea>
              </v-form>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn class="custom-market-make-btn">취소 </v-btn>
              <v-btn class="custom-market-make-btn">등록 </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "MarketMakeView",
  data() {
    return {
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
.market-make-welcome {
  border: 2px solid black;
  border-radius: 5px;
  padding: 10px 20px;
  margin: 10px 0;
  text-align: start;
  font-size: 1.3rem;
  font-family: "NanumBarunpen";
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.16), 0 1px 5px rgba(0, 0, 0, 0.23);
}

.market-make-title {
  text-align: start;
  font-size: 1.3rem;
  font-family: "NanumBarunpen";
  margin-bottom: 20px;
}

.custom-market-make-card {
  font-family: "NanumBarunpen";
  border: 2px solid black;
  padding: 10px 5px;
}

.custom-market-make-btn {
  border: 2px solid black;
  background: var(--primary-color);
}
</style>