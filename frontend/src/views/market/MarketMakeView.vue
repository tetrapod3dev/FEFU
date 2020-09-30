<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" md="10" lg="8">
        <div class="market-make-welcome">상품을 등록해주세요🧾!</div>
        <v-card class="custom-market-make-card">
          <v-card-text>
            <div class="market-make-title">카테고리</div>
            <v-form ref="form">
              <v-row no-gutters>
                <v-col cols="12" md="4">
                  <v-select
                    label="대분류"
                    v-model="product.main_category_no"
                    :menu-props="{ bottom: true, offsetY: true }"
                    :items="maincategories"
                    item-text="main_category_name"
                    item-value="no"
                    required
                    filled
                    autofocus
                    color="#37cdc2"
                  ></v-select>
                </v-col>
                <v-col cols="12" md="4">
                  <v-select
                    label="중분류"
                    v-model="product.medium_category_no"
                    :menu-props="{ bottom: true, offsetY: true }"
                    :items="mediumcategories[product.main_category_no]"
                    item-text="medium_category_name"
                    item-value="no"
                    required
                    filled
                    color="#37cdc2"
                    @input="getSubcategories"
                  ></v-select>
                </v-col>
                <v-col cols="12" md="4">
                  <v-select
                    label="소분류"
                    v-model="product.sub_category_no"
                    :menu-props="{ bottom: true, offsetY: true }"
                    :items="subcategories"
                    item-text="sub_category_name"
                    item-value="no"
                    required
                    filled
                    color="#37cdc2"
                  ></v-select
                ></v-col>
              </v-row>
              <v-row>
                <v-col cols="12" md="4">
                  <v-file-input
                    label="상품 이미지"
                    v-model="images"
                    :roules="imageRules"
                    filled
                    :rules="[(v) => !!v || '이미지를 첨부해주세요']"
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
                      !url ? 'border-bottom: 1px solid rgba(0, 0, 0, 0.42)' : ''
                    "
                    :src="!!url ? url : require('@/assets/images/noimage.jpg')"
                  />
                </v-col>
                <v-col cols="12" md="8">
                  <v-text-field
                    label="상품명"
                    v-model="product.title"
                    name="title"
                    type="text"
                    required
                    filled
                    autocapitalize="off"
                    autocorrect="off"
                    autocomplete="off"
                    color="#37cdc2"
                  ></v-text-field>
                  <v-text-field
                    label="판매금액"
                    v-model.number="product.price"
                    name="price"
                    type="number"
                    required
                    filled
                    append-outer-icon
                    autocomplete="off"
                    color="#37cdc2"
                  ></v-text-field>

                  <v-text-field
                    label="에코포인트"
                    v-model.number="product.eco_point"
                    name="ecopoint"
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
                    v-model="product.contact"
                    name="contact"
                    type="text"
                    required
                    filled
                    autocapitalize="off"
                    autocorrect="off"
                    autocomplete="off"
                    color="#37cdc2"
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-textarea
                label="상세 내용"
                v-model="product.content"
                name="content"
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
            <v-btn class="custom-market-make-btn" @click="uploadImage(images)"
              >이미지 업로드 테스트 버튼</v-btn
            >
            <v-btn
              class="custom-market-make-btn"
              :to="{ name: 'MarketMainView' }"
              >취소</v-btn
            >
            <v-btn class="custom-market-make-btn" @click="registProduct"
              >등록
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
import SERVER from "@/api/api";
import { mapGetters } from "vuex";
import router from "@/router";
import { imageUploadable } from "@/components/mixin/imageUploadable";

export default {
  name: "MarketMakeView",
  mixins: [imageUploadable],
  data() {
    return {
      product: {
        title: "",
        content: "",
        writer: "",
        contact: "",
        price: "",
        photo: "",
        eco_point: 0,
        main_category_no: null,
        medium_category_no: null,
        sub_category_no: null,
      },
      maincategories: [],
      mediumcategories: {},
      subcategories: [],
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
  mounted() {
    this.maincategories = this.MAINCATEGORIES;
    this.mediumcategories = this.MEDIUMCATEGORIES;
  },
  computed: {
    ...mapGetters("accounts", ["config", "USERNAME"]),
    ...mapGetters("market", ["MAINCATEGORIES", "MEDIUMCATEGORIES"]),
  },
  methods: {
    Preview_image() {
      if (!this.images) {
        this.url = null;
      } else {
        this.url = URL.createObjectURL(this.images);
      }
    },

    registProduct: async function () {
      this.product.writer = this.USERNAME;
      this.product.photo = this.uploadImage(this.images);
      // await this.uploadImage();
      await axios
        .post(SERVER.URL + SERVER.ROUTES.products.URL + "/", this.product, {
          headers: {
            Authorization: this.config,
          },
        })
        .then(() => {
          alert("상품 등록 완료 되었습니다.");
          router.push({ name: "MarketMainView" });
        })
        .catch((err) => {
          console.log(err);
        });
    },

    // async uploadImage() {
    //   let configs = {
    //     headers: {
    //       "Content-Type": "multipart/form-data",
    //     },
    //   };

    //   let file = this.images;
    //   let formData = new FormData();
    //   formData.append("file", file);

    //   await axios
    //     .post(SERVER.URL + SERVER.ROUTES.images.upload, formData, configs)
    //     .then((res) => {
    //       this.product.photo = res.data.fileName;
    //       console.log(res);
    //     })
    //     .catch((err) => {
    //       console.log(err);
    //     });
    // },

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
    getSubcategories() {
      axios
        .get(SERVER.URL + SERVER.ROUTES.products.subcategory, {
          params: { mediumCategoryNo: this.product.medium_category_no },
        })
        .then((res) => {
          this.subcategories = res.data;
        })
        .catch((err) => {
          console.log(err.response);
        });
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