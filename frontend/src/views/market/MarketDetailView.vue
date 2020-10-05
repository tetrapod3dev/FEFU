<template>
  <v-col cols="12" sm="9" class="pt-0">
    <section id="product-list">
      <v-container>
        <v-row>
          <v-col cols="12" md="5">
            <v-img
              class="custom-carousel"
              :src="
                product.photo
                  ? imageSrc(product.photo)
                  : '@/assets/images/lazy-loading.jpg'
              "
              height="400px"
              lazy-src="@/assets/images/lazy-loading.jpg"
            >
              <template v-slot:placeholder>
                <lazy-loading />
              </template>
            </v-img>
          </v-col>
          <v-col cols="12" md="7">
            <div class="product-info-wrapper text-left d-flex flex-column pa-3">
              <p class="product-title">{{ product.title }}</p>
              <p>
                {{ product.main_category_name }} >
                {{ product.medium_category_name }}
              </p>
              <p class="product-price">{{ product.price }}원</p>
              <p class="product-ecopoint">
                사용가능한 에코포인트는 {{ product.eco_point }}p 입니다.
              </p>
              <div class="seller-info">
                <p class="mb-2">판매자</p>
                <div class="d-flex">
                  <v-avatar size="40" color="teal">
                    <img
                      :src="
                        !!writer.photo
                          ? imageSrc(writer.photo)
                          : require(`@/assets/images/${writer.gender}.png`)
                      "
                    />
                  </v-avatar>
                  <div class="d-flex flex-column ml-3">
                    <p class="product-owner">{{ product.writer }}</p>
                    <p class="product-phonenumber">
                      {{ product.contact }}
                    </p>
                  </div>
                  <div class="d-flex flex-column ml-3">
                    <v-tooltip v-if="!chat.isAlreadyJoined" right>
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn
                          @click="enterChat(chat)"
                          color="var(--primary-color)"
                          fab
                          text
                          small
                          v-bind="attrs"
                          v-on="on"
                        >
                          <v-icon> mdi-comment </v-icon>
                        </v-btn>
                      </template>
                      <span>채팅 입장</span>
                    </v-tooltip>
                    <v-tooltip v-if="chat.isAlreadyJoined" right>
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn
                          color="grey"
                          fab
                          text
                          small
                          v-bind="attrs"
                          v-on="on"
                        >
                          <v-icon> mdi-comment </v-icon>
                        </v-btn>
                      </template>
                      <span>이미 채팅 중입니다</span>
                    </v-tooltip>
                  </div>
                </div>
              </div>
              <v-row no-gutters>
                <v-col cols="2">
                  <v-btn
                    v-if="product.status == 0"
                    class="product-state"
                    outlined
                    tile
                    @click="handleStatusButton"
                    >판매 중</v-btn
                  >

                  <v-btn
                    v-else
                    class="product-state"
                    outlined
                    tile
                    @click="handleStatusButton"
                    >판매 완료</v-btn
                  >
                </v-col>
                <v-spacer></v-spacer>
                <v-col cols="3" align="end">
                  <v-btn
                    v-if="product.writer == USERNAME"
                    class="product-state"
                    outlined
                    tile
                    @click="deleteProduct"
                  >
                    삭제
                  </v-btn>
                </v-col>
                <v-col cols="3" align="center">
                  <v-btn
                    v-if="product.writer == USERNAME"
                    class="product-state"
                    outlined
                    tile
                    :to="{
                      name: 'MarketUpdateView',
                      params: { productNo: $route.params.productNo },
                    }"
                  >
                    수정
                  </v-btn>
                </v-col>
              </v-row>
            </div>
          </v-col>

          <SoldModal
            :product="product"
            v-if="visible"
            @close="handleStatusButton"
          >
          </SoldModal>

          <v-col cols="12">
            <p class="product-description text-left pa-3">
              {{ product.content }}
            </p>
            <div class="py-12"></div>
          </v-col>
          <v-col cols="12">
            <h1 class="market-title">같이 보면 좋을 상품</h1>
          </v-col>
          <v-col
            v-for="index in 3"
            :key="index"
            cols="12"
            sm="4"
            align="center"
          >
            <v-card
              class="custom-card ma-4"
              :height="1.6 * cardWidth"
              :width="cardWidth"
              cols="12"
              md="4"
              @click="
                moveToPage({
                  name: 'MarketDetailView',
                  params: { productNo: products[index - 1].no },
                })
              "
            >
              <v-img
                :height="1.1 * cardWidth"
                :src="
                  products[index - 1].photo
                    ? imageSrc(products[index - 1].photo)
                    : '@/assets/images/lazy-loading.jpg'
                "
                lazy-src="@/assets/images/lazy-loading.jpg"
              >
                <template v-slot:placeholder>
                  <lazy-loading />
                </template>
              </v-img>
              <v-card-text class="text-left text--primary">
                <div>{{ products[index - 1].title }}</div>
                <div>{{ products[index - 1].price }}</div>
                <div>{{ products[index - 1].eco_point }}</div>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </section>
    <div class="py-12"></div>
  </v-col>
</template>

<script>
import { mixinGetUserInfo } from "@/components/mixin/mixinGetUserInfo";
import { mixinJoinChat } from "@/components/mixin/mixinJoinChat";

import { mapGetters } from "vuex";
import axios from "axios";
import SERVER from "@/api/api";
import router from "@/router";
import SoldModal from "../../components/market/SoldModal";

export default {
  name: "MarketDetailView",
  mixins: [mixinGetUserInfo, mixinJoinChat],
  components: {
    SoldModal: SoldModal,
  },

  data() {
    return {
      cardSlide1: null,
      colors: ["indigo", "warning", "pink darken-2"],
      slides: ["First", "Second", "Third"],
      visible: false,
      product: {
        contact: "",
        content: "",
        eco_point: 1,
        main_category_no: 1,
        medium_category_no: 1,
        main_category_name: "",
        medium_category_name: "",
        sub_category_no: 1,
        no: 45,
        photo: "",
        price: 0,
        reg_time: "",
        status: null,
        title: "",
        writer: "",
      },
      writer: {
        gender: "남자",
        photo: "",
      },
      products: [
        {
          no: 0,
          title: "",
          price: "",
          eco_point: "",
          photo: "",
        },
        {
          no: 0,
          title: "",
          price: "",
          eco_point: "",
          photo: "",
        },
        {
          no: 0,
          title: "",
          price: "",
          eco_point: "",
          photo: "",
        },
      ],
    };
  },
  created() {},
  async mounted() {
    await this.getProduct().then(() => {
      this.getChat("p" + this.product.no);
    });
    await this.createViewLog();
    await this.getInfo(this.product.writer)
      .then((res) => {
        this.writer = res.data;
      })
      .catch((err) => console.log(err));

    this.getRelatedProduct();
  },
  computed: {
    cardWidth() {
      let resultWidth;
      switch (this.$vuetify.breakpoint.name) {
        case "xs":
          resultWidth = 220;
          break;
        case "sm":
          resultWidth = 220;
          break;
        case "md":
          resultWidth = 220;
          break;
        case "lg":
          resultWidth = 280;
          break;
        case "xl":
          resultWidth = 280;
          break;
      }
      return resultWidth;
    },
    ...mapGetters("accounts", ["config", "USERNAME"]),
  },
  methods: {
    moveToPage(_url) {
      this.$router
        .push(_url)
        .then(() => {
          location.reload();
        })
        .catch((error) => {
          if (error.name === "NavigationDuplicated") {
            location.reload();
          }
        });
    },
    async getProduct() {
      await axios
        .get(
          SERVER.URL +
            SERVER.ROUTES.products.URL +
            "/" +
            this.$route.params.productNo +
            "/"
        )
        .then((res) => {
          this.product = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async createViewLog() {
      await axios
        .post(
          SERVER.URL +
            SERVER.ROUTES.products.URL +
            "/" +
            this.$route.params.productNo +
            "/viewed/",
          null,
          {
            headers: {
              Authorization: this.config,
            },
          }
        )
        .then((res) => {
          this.products = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },

    imageSrc(filename) {
      return SERVER.IMAGE_URL + filename;
    },
    deleteProduct() {
      if (confirm("정말 삭제하실건가요?")) {
        axios
          .delete(
            SERVER.URL +
              SERVER.ROUTES.products.URL +
              "/" +
              this.$route.params.productNo +
              "/",
            {
              headers: {
                Authorization: this.config,
              },
            }
          )
          .then(() => {
            router.push({ name: "MarketMainView" });
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
    getRelatedProduct() {
      axios
        .get(SERVER.URL + SERVER.ROUTES.products.related_products, {
          params: { product_pk: this.$route.params.productNo },
        })
        .then((res) => {
          this.products = res.data.related_products;
        });
    },
    handleStatusButton() {
      this.visible = !this.visible;
    },
  },
};
</script>

<style lang="scss" scoped>
.custom-card {
  border: 2px solid black;
  border-radius: 15px;
  font-family: "NanumBarunpen";

  &:hover {
    transform: translate3d(0px, -5px, -5px);
    box-shadow: 3px 3px black;
    transition: 0.4s;
    cursor: pointer;
  }
}

.custom-carousel {
  border: 3px solid black;
  background: black;
  border-radius: 15px;
}

// .product-info-wrapper {
//   margin-left: 40px;
// }

.product-title {
  font-family: "NanumBarunpen";
  font-size: 40px;
  margin-bottom: 0;
}

.product-price {
  font-family: "NanumBarunpen";
  font-size: 2rem;
  margin-bottom: 0;
}

.product-ecopoint {
  font-family: "NanumBarunpen";
  font-size: 1.3rem;
  color: var(--primary-color);
}

.product-owner {
  margin-bottom: 0;
}

.product-state {
  border: 2px solid black;
  border-radius: 10px;
  padding: 5px 10px;
}

.product-chat {
  border: 2px solid black;
}

.market-title {
  margin-top: 10px;
  font-family: "NanumBarunpen";
}
</style>
