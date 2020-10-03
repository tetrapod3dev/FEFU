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
              <p>대분류 > 중분류</p>
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
                </div>
              </div>
              <v-row no-gutters>
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
                <v-col cols="2">
                  <v-btn class="product-state" outlined tile>판매 중</v-btn>
                </v-col>
              </v-row>
            </div>
          </v-col>

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
                :src="imageSrc(products[index - 1].photo)"
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
import { mapGetters } from "vuex";
import axios from "axios";
import SERVER from "@/api/api";
import router from "@/router";

export default {
  name: "MarketDetailView",
  mixins: [mixinGetUserInfo],

  data() {
    return {
      cardSlide1: null,
      colors: ["indigo", "warning", "pink darken-2"],
      slides: ["First", "Second", "Third"],
      product: {
        contact: "",
        content: "",
        eco_point: 1,
        main_category_no: 1,
        medium_category_no: 1,
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
  async created() {
    await this.getProduct();
    await this.getInfo(this.product.writer)
      .then((res) => {
        this.writer = res.data;
      })
      .catch((err) => console.log(err));
    // await axios.post(
    //   SERVER.URL +
    //     SERVER.ROUTES.products.URL +
    //     "/" +
    //     this.$route.params.productNo +
    //     SERVER.ROUTES.products.viewed,
    //   {
    //     sub_category_no: this.product.sub_category_no,
    //   },
    //   {
    //     headers: {
    //       Authorization: this.config,
    //     },
    //   }
    // );
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
    getTopThreeProduct() {
      axios
        .get(SERVER.URL + SERVER.ROUTES.products.top_three_viewed_today)
        .then((res) => {
          console.log(res);
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
        .get(
          SERVER.URL + 
            SERVER.ROUTES.products.related_products, 
            {params: {"product_pk": this.$route.params.productNo}}  
        )
        .then((res) => {
          console.log(res)
          this.products = res.data.related_products
        })
    }
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

.market-title {
  margin-top: 10px;
  font-family: "NanumBarunpen";
}
</style>
