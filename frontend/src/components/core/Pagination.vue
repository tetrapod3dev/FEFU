<template>
  <nav aria-label="Page navigation">
    <ul class="pagination">
      <li v-if="prev" @click="movePage($event)" class="page-item">
        <p class="page-link" aria-label="Previous">&laquo;</p>
      </li>
      <li v-else class="page-item-disabled">
        <p class="page-link" aria-label="Previous">&laquo;</p>
      </li>
      <li @click="movePage($event)" v-if="curPage - 1 > 0" class="page-item">
        <p class="page-link">{{ curPage - 1 }}</p>
      </li>
      <li class="page-item active">
        <p class="page-link">{{ curPage }}</p>
      </li>
      <li @click="movePage($event)" v-if="curPage < maxPage" class="page-item">
        <p class="page-link">{{ curPage + 1 }}</p>
      </li>
      <li v-if="next" @click="movePage($event)" class="page-item">
        <p class="page-link" aria-label="Next">&raquo;</p>
      </li>
      <li v-else class="page-item-disabled">
        <p class="page-link" aria-label="Next">&raquo;</p>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: "Pagination",
  props: {
    curPage: {
      type: Number,
    },
    maxPage: {
      type: Number,
    },
    next: {
        type: Boolean
    },
    prev: {
        type: Boolean
    }
  },
  methods: {
    movePage(event) {
      this.$emit("move-page", event.target.outerText);
    },
  },
};
</script>

<style lang="scss" scoped>
.pagination {
  list-style: none;
  text-align: center;
}
.page-item {
  font-family: "Nunito", "NanumSquareRound", sans-serif;
  font-size: 20px;
  display: inline;
  padding: 2px;
  margin: 5px;
  &:hover {
    cursor: pointer;
    background-color: rgba(0, 0, 0, 0.1);
    border-radius: 15px;
  }
  &.active {
    background-color: var(--primary-color);
    border-radius: 15px;
    height: 45px;
  }
  p {
    margin: 0 1.15em;
    display: inline-block;
  }
}
.page-item-disabled {
  font-family: "Nunito", "NanumSquareRound", sans-serif;
  font-size: 20px;
  display: inline;
  padding: 2px;
  margin: 5px;
  color: #c9c9c9;
  p {
    margin: 0 1.15em;
    display: inline-block;
  }
}
</style>