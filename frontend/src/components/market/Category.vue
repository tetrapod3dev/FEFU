<template>
  <div>
    <v-list class="custom-list">
      <v-list-group
        v-for="(mainCategory, index) in MAINCATEGORIES"
        :key="index"
        no-action
        class="custom-list-item"
        :class="`custom-list-item-${
          listColorName[index % listColorName.length]
        }`"
      >
        <template v-slot:activator>
          <v-list-item-content>
            <v-list-item-title
              v-text="mainCategory.main_category_name"
            ></v-list-item-title>
          </v-list-item-content>
        </template>

        <v-list-item
          v-for="mediumCategory in MEDIUMCATEGORIES[mainCategory.no]"
          :key="mediumCategory.no"
          :link="true"
          @click="
            moveToPage({
              name: 'MarketListView',
              params: {
                pageNum: 1,
                mainCategoryNo: mainCategory.no,
                mediumCategoryNo: mediumCategory.no,
                mainCategory: mainCategory.main_category_name,
                mediumCategory: mediumCategory.medium_category_name,
              },
            })
          "
        >
          <v-list-item-content class="custom-list-item-content">
            <v-list-item-title
              v-text="mediumCategory.medium_category_name"
            ></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-group>
    </v-list>

    <router-link
      v-if="isLoggedIn"
      tag="button"
      class="custom-make-btn"
      :to="{ name: 'MarketMakeView' }"
    >
      상품 등록
    </router-link>
  </div>
</template>


<script>
import { mapGetters, mapMutations } from "vuex";

export default {
  name: "MarketCategory",
  computed: {
    ...mapGetters("market", ["MAINCATEGORIES", "MEDIUMCATEGORIES", "FILTER"]),
    ...mapGetters("accounts", ["isLoggedIn"]),
  },
  data() {
    return {
      listColorName: [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "purple",
      ],
    };
  },
  methods: {
    ...mapMutations("market", ["SET_FILTER"]),
    moveToPage(_url) {
      this.SET_FILTER({
        maincategory: {
          no: _url.params.mainCategoryNo,
          name: _url.params.mainCategory,
        },
        mediumcategory: {
          no: _url.params.mediumCategoryNo,
          name: _url.params.mediumCategory,
        },
        pageNum: 1,
        content: null,
      });
      console.log(this.FILTER);
      this.$router.push(_url).catch((error) => {
        if (error.name === "NavigationDuplicated") {
          location.reload();
        }
      });
    },
  },
};
</script>

<style lang="scss" scoped>
.custom-list {
  // border: 2px solid black;
  // border-radius: 10px;
  // padding: 5px 0;
  font-family: "S-CoreDream-7ExtraBold";
}

.custom-list-item {
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

.custom-white {
  background: var(--white-color);
}

.custom-make-btn {
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
</style>
