<template>
  <v-col cols="12" sm="9" class="pt-0">
    <div class="market-section">
      <h1
        v-if="
          $route.params.mainCategoryNo &&
          FILTER_MAINCATEGORY.no == $route.params.mainCategoryNo
        "
        class="market-title text-left ml-3"
      >
        {{ FILTER_MAINCATEGORY.name }} >
        {{ FILTER_MEDIUMCATEGORY.name }}
      </h1>
      <h1
        v-if="
          !$route.params.mainCategoryNo ||
          FILTER_MAINCATEGORY.no != $route.params.mainCategoryNo
        "
        class="market-title text-left ml-3"
      >
        검색결과 "{{ $route.params.content }}"
      </h1>
      <v-row v-if="products.length != 0">
        <v-col
          v-for="(product, index) in products"
          :key="index"
          cols="6"
          sm="4"
          justify="center"
          align="center"
        >
          <market-card :product="product"> </market-card>
        </v-col>
      </v-row>
      <core-banner
        v-else
        content="등록된 상품이 없네요. 당신이 먼저 물건을 등록해보세요!📃"
        btn-text="물건등록하러 가기"
        align="center"
        :to="{ name: 'MarketMakeView' }"
      />
      <div class="py-12"></div>
      <core-pagination
        :curPage="pagination.curPage"
        :maxPage="pagination.endPage"
        :next="pagination.next"
        :prev="pagination.prev"
        @move-page="movePage"
      />
    </div>
  </v-col>
</template>

<script>
import axios from "axios";
import SERVER from "@/api/api";

import { mapGetters } from "vuex";

import CorePagination from "@/components/core/Pagination";
import CoreBanner from "@/components/core/Banner.vue";
import MarketCard from "@/components/market/MarketCard.vue";

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
    CorePagination,
    CoreBanner,
    MarketCard,
  },
  created() {
    this.getProducts();
    this.pagination.curPage = parseInt(this.$route.params.pageNum);
  },
  computed: {
    ...mapGetters("market", [
      "FILTER",
      "FILTER_MAINCATEGORY",
      "FILTER_MEDIUMCATEGORY",
    ]),
  },
  methods: {
    getProducts() {
      axios
        .get(SERVER.URL + SERVER.ROUTES.products.URL, {
          params: {
            pageNum: this.$route.params.pageNum,
            mainCategory: this.$route.params.mainCategoryNo,
            mediumCategory: this.$route.params.mediumCategoryNo,
            content: this.$route.params.content,
          },
        })
        .then((res) => {
          this.pagination = res.data.page;
          this.products = res.data.list;
        })
        .catch((err) => {
          console.log(err);
        });
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
</style>
