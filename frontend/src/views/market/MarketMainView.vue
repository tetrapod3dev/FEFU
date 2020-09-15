<template>
  <div>
    <v-container>
      <v-row justify="center">
        <v-col cols="12" xl="10">
          <v-row dense>
            <v-breadcrumbs class="pb-0" :items="breadcrums"></v-breadcrumbs>
            <v-spacer></v-spacer>

            <v-col cols="12" sm="4">
              <v-select
                class="pa-0"
                v-model="select"
                :items="options"
                style="margin-bottom: -20px;"
                outlined
                dense
              ></v-select>
            </v-col>
          </v-row>
        </v-col>
      </v-row>

      <h3>이 상품 어때요? (추천 상품)</h3>
      <v-row justify="center">
        <v-col cols="12" xl="10">
          <v-slide-group v-model="products" center-active show-arrows>
            <v-slide-item v-for="(product, index) in products" :key="index">
              <v-hover v-slot:default="{ hover }" open-delay="200">
                <v-card
                  :elevation="hover ? 16 : 2"
                  class="ma-4"
                  :height="1.6 * cardWidth"
                  :width="cardWidth"
                >
                  <v-img
                    :height="1.2 * cardWidth"
                    src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
                  ></v-img>

                  <v-card-text class="text-left text--primary">
                    <div>{{product.name}}</div>
                    <div>{{product.price}}</div>
                    <div>{{product.price}}</div>
                  </v-card-text>
                </v-card>
              </v-hover>
            </v-slide-item>
          </v-slide-group>
        </v-col>
      </v-row>

      <h3>지금 바로 신상품</h3>
      <v-row justify="center">
        <v-col cols="12" xl="10">
          <v-slide-group v-model="products" center-active show-arrows>
            <v-slide-item v-for="(product, index) in products" :key="index">
              <v-hover v-slot:default="{ hover }" open-delay="200">
                <v-card
                  :elevation="hover ? 16 : 2"
                  class="ma-4"
                  :height="1.6 * cardWidth"
                  :width="cardWidth"
                >
                  <v-img
                    :height="1.2 * cardWidth"
                    src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
                  ></v-img>

                  <v-card-text class="text-left text--primary">
                    <div>{{product.name}}</div>
                    <div>{{product.price}}</div>
                    <div>{{product.price}}</div>
                  </v-card-text>
                </v-card>
              </v-hover>
            </v-slide-item>
          </v-slide-group>
        </v-col>
      </v-row>

      <h3>지금 인기 상품</h3>
      <v-row justify="center">
        <v-col cols="12" xl="10">
          <v-slide-group v-model="products" center-active show-arrows>
            <v-slide-item v-for="(product, index) in products" :key="index">
              <v-hover v-slot:default="{ hover }" open-delay="200">
                <v-card
                  :elevation="hover ? 16 : 2"
                  class="ma-4"
                  :height="1.6 * cardWidth"
                  :width="cardWidth"
                >
                  <v-img
                    :height="1.2 * cardWidth"
                    src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
                  ></v-img>

                  <v-card-text class="text-left text--primary">
                    <div>{{product.name}}</div>
                    <div>{{product.price}}</div>
                    <div>{{product.price}}</div>
                  </v-card-text>
                </v-card>
              </v-hover>
            </v-slide-item>
          </v-slide-group>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
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
  data() {
    return {
      range: [0, 10000],
      select: "Popularity",
      options: [
        "Default",
        "Popularity",
        "Relevance",
        "Price: Low to High",
        "Price: High to Low",
      ],
      page: 1,
      breadcrums: [
        {
          text: "Home",
          disabled: false,
          href: "breadcrumbs_home",
        },
        {
          text: "Clothing",
          disabled: false,
          href: "breadcrumbs_clothing",
        },
        {
          text: "T-Shirts",
          disabled: true,
          href: "breadcrumbs_shirts",
        },
      ],
      min: 0,
      max: 10000,
      items: [
        {
          id: 2,
          name: "Shoes",
          children: [
            { id: 2, name: "Casuals" },
            { id: 3, name: "Formals" },
            { id: 4, name: "Sneakers" },
          ],
        },
        {
          id: 1,
          name: "Clothing",
          children: [
            { id: 5, name: "Shirts" },
            { id: 6, name: "Tops" },
            { id: 7, name: "Tunics" },
            { id: 8, name: "Bodysuit" },
          ],
        },
      ],
      products: [
        {
          id: 1,
          name: "BLACK TEE",
          price: "18.00",
          src: require("@/assets/logo.png"),
        },
        {
          id: 2,
          name: "WHITE TEE",
          price: "40.00",
          src: require("@/assets/logo.png"),
        },
        {
          id: 3,
          name: "Zara limited...",
          price: "25.00",
          src: require("@/assets/logo.png"),
        },
        {
          id: 4,
          name: "SKULL TEE",
          price: "30.00",
          src: require("@/assets/logo.png"),
        },
        {
          id: 5,
          name: "MANGO WINTER",
          price: "50.00",
          src: require("@/assets/logo.png"),
        },
        {
          id: 6,
          name: "SHIRT",
          price: "34.00",
          src: require("@/assets/logo.png"),
        },
        {
          id: 7,
          name: "TRUCKER JACKET",
          price: "38.00",
          src: require("@/assets/logo.png"),
        },
        {
          id: 8,
          name: "COATS",
          price: "25.00",
          src: require("@/assets/logo.png"),
        },
        {
          id: 9,
          name: "MANGO WINTER",
          price: "50.00",
          src: require("@/assets/logo.png"),
        },
        {
          id: 10,
          name: "SHIRT",
          price: "34.00",
          src: require("@/assets/logo.png"),
        },
        {
          id: 11,
          name: "TRUCKER JACKET",
          price: "38.00",
          src: require("@/assets/logo.png"),
        },
        {
          id: 12,
          name: "COATS",
          price: "25.00",
          src: require("@/assets/logo.png"),
        },
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
        스포츠: [
          "골프",
          "자전거",
          "인라인/스케이트/전동",
          "축구",
          "야구",
          "농구",
          "라켓스포츠",
          "헬스/요가",
          "수상스포츠",
          "겨울스포츠",
          "검토/격투/권투",
          "기타 스포츠",
        ],
        "티켓/쿠폰": [
          "티켓",
          "상품권/쿠폰",
          "여행숙박/이용권",
          "기타 티켓/쿠폰/이용권",
        ],
        게임: [
          "PC게임",
          "플레이스테이션",
          "PSP",
          "닌텐도",
          "Wii",
          "XBOX",
          "게임타이틀",
          "기타 게임",
        ],
        "도서/음반/문구": [
          "유아동도서/음반",
          "학습/교육",
          "소설/만화책",
          "여행/취미/레저",
          "문학/과학/경영",
          "예술/디자인",
          "잡지",
          "기타 도서",
          "음반/DVD/굿즈",
          "문구/사무용품",
        ],
        가전제품: [
          "냉장고",
          "TV",
          "세탁기/건조기",
          "주방가전",
          "스마트홈",
          "영상가전",
          "음향가전",
          "계절가전",
          "생활가전",
          "미용가전",
          "기타 가전제품",
        ],
        "가구/인테리어": [
          "침실가구",
          "거실가구",
          "주방가구",
          "수납/선반/공간박스",
          "학생/서재/사무용가구",
          "기타가구",
          "침구",
          "커튼/카패트",
          "조명/무드등",
          "인테리어소품",
          "이벤트/파티용품",
          "디퓨저/캔들",
          "시계/액자/팝아트",
          "원예",
        ],
        패션의류: ["여성의류", "남성의류", "교복/체육복/단복"],
        "노트북/데스크탑": [
          "노트북/넷북",
          "데스크탑/본체",
          "모니터",
          "CPU/메인보드",
          "HDD/SSD/ODD",
          "RAM/VGA/SOUND",
          "USB/케이블",
          "케이스/파워/쿨러",
          "키보드/마우스/스피커",
          "프린터/복합기/잉크/토너",
          "공유기/랜카드",
          "소프트웨어",
          "기타 주변기기",
        ],
      },
    };
  },
};
</script>

<style>
.v-card--reveal {
  align-items: center;
  bottom: 0;
  justify-content: center;
  opacity: 0.8;
  position: absolute;
  width: 100%;
}
</style>
