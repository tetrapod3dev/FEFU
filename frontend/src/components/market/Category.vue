<template>
  <div>
    <v-list class="custom-list">
      <v-list-group
        v-for="(category, index) in Object.keys(marketCategories)"
        :key="index"
        no-action
        class="custom-list-item"
        :class="
          `custom-list-item-${listColorName[index % listColorName.length]}`
        "
      >
        <template v-slot:activator>
          <v-list-item-content>
            <v-list-item-title v-text="category"></v-list-item-title>
          </v-list-item-content>
        </template>

        <v-list-item
          v-for="subCategory in marketCategories[category]"
          :key="subCategory"
          :link="true"
          :to="{
            name: 'MarketListView',
            params: { pageNo: 1, category: category, subCategory: subCategory },
          }"
        >
          <v-list-item-content class="custom-list-item-content">
            <v-list-item-title v-text="subCategory"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-group>
    </v-list>
  </div>
</template>

<script>
export default {
  name: "MarketCategory",
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

      marketCategories: {
        뷰티: [
          "스킨케어",
          "메이크업",
          "팩/클렌징/필링",
          "헤어/바디",
          "향수",
          "네일케어",
          "남성 화장품",
          "가발/기타",
        ],
        "반려동물/취미": [
          "반려동물",
          "키덜트",
          "핸드메이드/DIY",
          "악기",
          "예술작품/골동품/수집",
          "미술재료/미술도구",
        ],
        패션잡화: [
          "운동화",
          "여성신발",
          "남성신발",
          "가방/핸드백",
          "지갑/벨트",
          "악세서리/귀금속",
          "시계",
          "선글라스/안경",
          "모자",
          "기타잡화/관련용품",
        ],
        "리빙/생활": [
          "주방용품",
          "차량용품",
          "가공식품",
          "욕실용품",
          "청소/세탁용품",
          "생활잡화",
          "기타 생활용품",
        ],
        "출산/유아동": [
          "출산/육아용품",
          "유아동안전/실내용품",
          "유아동의류",
          "유아동잡화",
          "유아동가구",
          "유아동교구/완구",
          "기타 유아동용품",
        ],
        "모바일/태블릿": [
          "스마트폰",
          "태블릿PC",
          "스마트워치/밴드",
          "일반/피쳐폰",
          "케이스/거치대/보호필름",
          "배터리/충전기/케이블",
          "메모리/젠더/리더기",
          "로밍/데이터/쿠폰",
        ],
        "레저/여행": [
          "등산의류/용품",
          "캠핑용품",
          "낚시용품",
          "기타 레저/여행용품",
        ],
        "공구/산업용품": [
          "드릴/전동공구",
          "에어/유압",
          "작업공구",
          "측정공구",
          "초경/절삭/접착윤활",
          "전기/전자",
          "배관설비/포장운송",
          "금형공작",
          "용접기자재",
          "산업/안전/공구함",
          "산업자재",
          "농기계/농업용공구",
        ],
        "카메라/캠코더": [
          "DSLR",
          "미러리스",
          "디지털카메라",
          "필름/즉석카메라",
          "캠코더/액션캠",
          "기타 카메라",
          "카메라렌즈",
          "삼각대/조명/플래시",
          "기타 악세서리",
        ],
      },
    };
  },
};
</script>

<style lang="scss" scoped>
.custom-list {
  border: 2px solid black;
  border-radius: 10px;
  padding: 5px 0;
  font-family: "S-CoreDream-7ExtraBold";
}

.custom-list-item {
  &:not(:last-child) {
    border-bottom: 2px solid black;
  }

  &-red:hover {
    background: #cf6a87;
  }

  &-orange:hover {
    background: #f19066;
  }

  &-yellow:hover {
    background: #fdcb6e;
  }

  &-green:hover {
    background: #b8e994;
  }

  &-blue:hover {
    background: #82ccdd;
  }

  &-indigo:hover {
    background: #60a3bc;
  }

  &-purple:hover {
    background: #786fa6;
  }
}

.custom-white {
  background: var(--white-color);
}
</style>
