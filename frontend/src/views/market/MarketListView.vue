<template>
  <div id="market-list">
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

    <v-container>
      <v-row>
        <v-col cols="12" sm="3">
          <div :class="$vuetify.breakpoint.smAndDown ? '' : 'fixed-bar'">
            <market-search />
            <market-category class="custom-category" />
          </div>
        </v-col>

        <v-col cols="12" sm="9" class="pt-0">
          <div class="market-section">
            <h1 class="market-title text-left ml-3">
              {{ $route.params.mainCategory }} >
              {{ $route.params.mediumCategory }}
            </h1>
            <v-row>
              <v-col
                v-for="(product, index) in products"
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
                      <v-row
                        class="fill-height ma-0"
                        align="center"
                        justify="center"
                      >
                        <v-progress-circular
                          indeterminate
                          color="grey lighten-5"
                        ></v-progress-circular>
                      </v-row>
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

            <div class="py-12"></div>
            <core-pagination
              :curPage="pagination.curPage"
              :maxPage="pagination.endPage"
              @move-page="movePage"
            />
          </div>
        </v-col>
      </v-row>
    </v-container>

    <section>
      <div class="py-12"></div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import SERVER from "@/api/api";

import MarketCategory from "@/components/market/Category";
import MarketSearch from "@/components/market/Search";
import CorePagination from "@/components/core/Pagination";

export default {
  name: "MarketListView",
  data() {
    return {
      pagination: {
        curPage: 1,
        endPage: 1,
        next: false,
        perPageNum: 12,
        prev: false,
        startIndex: 1,
        startPage: 1,
        totalCount: 6,
      },
      products: [],
    };
  },
  components: {
    MarketCategory,
    MarketSearch,
    CorePagination,
  },
  created() {
    this.getProducts();
    this.pagination.curPage = parseInt(this.$route.params.pageNum);
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
  },
  methods: {
    getProducts() {
      axios
        .get(SERVER.URL + SERVER.ROUTES.products.URL, {
          params: {
            pageNum: this.$route.params.pageNum,
            mainCategory: 1,
            mediumCategory: 1,
            content: this.$route.params.content,
          },
        })
        .then((res) => {
          console.log(res);
          this.pagination = res.data.page;
          this.products = res.data.list;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    imageSrc(filename) {
      return SERVER.IMAGE_URL + filename;
    },
    movePage(page) {
      if (page == "«") {
        this.$router.push({ params: { pageNum: 1 } });
      } else if (page == "»") {
        this.$router.push({ params: { pageNum: this.pagination.endPage } });
      } else {
        this.$router.push({ params: { pageNum: parseInt(page) } });
      }
      scroll(0, 0);
    },
  },

  watch: {
    $route() {
      this.pagination.curPage = parseInt(this.$route.params.pageNum);
      this.getProducts();
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

.market-section {
  margin-bottom: 0px;
}

.market-title {
  margin-top: 10px;
  font-family: "NanumBarunpen";
}

.title-point {
  color: var(--primary-color);
}

.custom-pagination .v-pagination {
  .v-pagination__navigation,
  .v-pagination_item {
    border: 2px solid #000000 !important;
    &--active {
      background-color: var(--primary-color);
    }
  }
}

.fixed-bar {
  position: -webkit-sticky;
  position: sticky;
  top: 4rem;
  z-index: 2;
}
</style>
