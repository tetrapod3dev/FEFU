<template>
  <div>
    <input
      type="text"
      class="custom-search"
      placeholder="🔍 검색어를 입력하세요"
      v-model="searchWord"
      @keyup.enter="gotoMarketList"
    />
  </div>
</template>

<script>


export default {
  name: "MarketSearchView",
  data() {
    return{
      searchWord: ""
    }
  },
  methods: {
    gotoMarketList() {
      // console.log(this.searchWord)
      this.$router.push({
        name: "MarketListView", 
        params: {
          pageNum:1,
          content: this.searchWord
          }})
    }
  }
};
</script>

<style scoped>
.custom-search {
  border: 2px solid black;
  border-radius: 10px;
  padding: 7px 10px;
  margin: 10px 0 20px 0;
  text-align: start;
  width: 100%;
  font-family: "NanumBarunpen";
}

.custom-search:focus {
  outline: none;
}
</style>
