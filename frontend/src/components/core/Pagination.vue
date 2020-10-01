<template>
  <nav aria-label="Page navigation">
    <ul class="pagination">
      <li class="page-item">
        <p @click="movePage($event)" class="page-link" aria-label="Previous">
          &laquo;
        </p>
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
      <li class="page-item">
        <p @click="movePage($event)" class="page-link" aria-label="Next">
          &raquo;
        </p>
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
</style>