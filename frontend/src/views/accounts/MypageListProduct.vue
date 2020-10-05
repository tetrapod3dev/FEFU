<template>
  <div>
    <v-container justify="start">
      <div class="c-title c-card__content">등록 물건</div>

      <div class="c-txt c-card__content d-flex flex-column">
        <v-row v-if="myProducts.length != 0">
          <v-col
            v-for="(product, index) in myProducts"
            :key="index"
            cols="6"
            sm="4"
            justify="center"
            align="center"
          >
            <v-card
              class="custom-card"
              :height="1.6 * cardWidth"
              :width="cardWidth"
              :to="{
                name: 'MarketDetailView',
                params: { productNo: product.no },
              }"
            >
              <v-img
                :height="1.1 * cardWidth"
                :src="imageSrc(product.photo)"
                lazy-src="@/assets/images/lazy-loading.jpg"
              >
                <template v-slot:placeholder>
                  <lazy-loading />
                </template>
              </v-img>

              <v-card-text class="text-left text--primary">
                <div>{{ product.title }}</div>
                <div>{{ product.price }}</div>
                <div>{{ product.eco_point }}</div>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
        <core-banner
          v-else
          content="등록된 상품이 없네요. 당신이 먼저 물건을 등록해보세요!📃"
          btn-text="물건등록하러 가기"
          :to="{ name: 'MarketMakeView' }"
        />
      </div>
    </v-container>
  </div>
</template>

<script>
import SERVER from "@/api/api";
import axios from "axios";

import { mixinGetUserInfo } from "@/components/mixin/mixinGetUserInfo";

import { mapGetters } from "vuex";

import CoreBanner from "@/components/core/Banner.vue";

export default {
  name: "MypageListProduct",
  mixins: [mixinGetUserInfo],
  components: { CoreBanner },
  data() {
    return {
      isJoined: false,
      listColorName: [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "purple",
      ],
      userinfo: {
        no: 0,
        username: "",
        password: null,
        nickname: "",
        age: 0,
        gender: "남자",
        ecoPoint: 0,
        exp: 0,
        profileImage: "",
      },
      myProducts: [],
    };
  },
  created() {
    this.getUserInfo().catch((err) => console.log(err));

    this.getMyProducts();
  },
  computed: {
    ...mapGetters("accounts", ["config", "USERNAME"]),
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
  },

  methods: {
    imageSrc(filename) {
      return SERVER.IMAGE_URL + filename;
    },
    getMyProducts() {
      axios
        .get(SERVER.URL + SERVER.ROUTES.products.get_my_products, {
          headers: {
            Authorization: this.config,
          },
        })
        .then((res) => {
          this.myProducts = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
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

.c-sidebar {
  border: 2px solid black;
  border-radius: 10px;
  &__img {
    border-radius: 50%;
  }
  &__name {
    font-size: 1rem;
    width: 100%;
    height: 48px;
  }
}

.c-card__content {
  border: 2px solid black;
  border-radius: 5px;
  padding: 10px 20px;
  margin: 10px 0;
}
.c-txt,
.c-title {
  font-family: "NanumBarunpen";
}

.c-title {
  text-align: start;
  font-size: 1.5rem;
}

.c-btn {
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

.c-list {
  margin-top: 20px;
  font-family: "S-CoreDream-7ExtraBold";
}

.c-list-item {
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
</style>
