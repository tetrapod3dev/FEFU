<template>
  <div class="campaign-info d-flex flex-column">
    <v-container class="my-7">
      <h2 class="text-left">게시글 인증 관리</h2>
      <v-container v-if="proofList.length != 0">
        <v-row>
          <v-col
            v-for="(proof, index) in proofList"
            :key="index"
            cols="12"
            sm="6"
            md="4"
            lg="4"
            no-gutter
          >
            <v-dialog v-model="dialogs[proof.no]" persistent max-width="600px">
              <template v-slot:activator="{ on, attrs }">
                <v-card
                  style="border-radius: 15px"
                  contain
                  class="dailyquest-item d-flex align-center justify-center"
                  height="300"
                  v-bind="attrs"
                  v-on="on"
                  ><v-img
                    height="300"
                    style="border: 2px solid #000000; border-radius: 15px"
                    :src="
                      proof.photo
                        ? imageSrc(proof.photo)
                        : '@/assets/images/noimage.jpg'
                    "
                  ></v-img
                ></v-card>
              </template>
              <v-card style="border: 3px solid #000000">
                <v-card-title
                  style="
                    background-color: var(--primary-color);
                    border-bottom: 2px solid #000000;
                  "
                >
                  <span class="headline">{{ proof.title }}</span>
                </v-card-title>
                <v-card-text class="py-0">
                  <v-container class="pb-0">
                    <v-row>
                      <v-col cols="12" class="py-0">
                        <v-img
                          id="Preview_image_create"
                          style="border: 2px solid #000000; border-radius: 15px"
                          height="400px"
                          :src="
                            !!proof.photo
                              ? imageSrc(proof.photo)
                              : require('@/assets/images/noimage.jpg')
                          "
                          lazy-src="@/assets/images/lazy-loading.jpg"
                        >
                          <template v-slot:placeholder>
                            <lazy-loading />
                          </template>
                        </v-img>
                      </v-col>
                      <v-col cols="12" class="py-12">
                        {{ proof.content }}
                      </v-col>
                    </v-row>
                  </v-container>
                </v-card-text>
                <v-card-actions class="px-5">
                  <v-spacer></v-spacer>
                  <v-btn
                    class="c-btn"
                    text
                    @click="$set(dialogs, proof.no, false)"
                  >
                    취소
                  </v-btn>
                  <v-btn class="c-btn" text @click="permitProof(proof.no)">
                    승인
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-col>
        </v-row>

        <div class="py-12"></div>
        <core-pagination
          :curPage="pagination.curPage"
          :maxPage="pagination.endPage"
          :next="pagination.next"
          :prev="pagination.prev"
          @move-page="movePage"
        />
      </v-container>
      <v-container v-else>
        <h1 class="no-text">작성된 인증글이 없습니다!</h1>
      </v-container>
    </v-container>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import axios from "axios";
import SERVER from "@/api/api";

import CorePagination from "@/components/core/Pagination";

export default {
  props: ["campaign", "campaignTypeInfo"],
  created() {
    this.getProofYetCampaign();
    this.pagination.curPage = parseInt(this.$route.params.page_no);
    // this.campaign = this.$route.params.campaign;
    // this.campaignTypeInfo = this.$route.params.campaignTypeInfo;
  },
  mounted() {},
  computed: {
    ...mapGetters("accounts", ["config"]),
  },
  components: {
    CorePagination,
  },
  data() {
    return {
      dialogs: {},
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
      proofList: [],
    };
  },
  watch: {
    $route() {
      this.pagination.curPage = parseInt(this.$route.params.page_no);
      this.getProducts();
    },
  },
  methods: {
    permitProof(proofNo) {
      axios
        .patch(SERVER.URL + SERVER.ROUTES.campaigns.proof + "/" + proofNo)
        .then(() => {
          this.dialog = false;
          location.reload();
        })
        .catch((err) => {
          alert("인증 승인 요청 간에 문제가 생겼습니다");
          console.log(err.response);
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

    getProofYetCampaign() {
      let configs = {
        headers: {
          Authorization: this.config,
        },
      };
      axios
        .get(
          SERVER.URL +
            SERVER.ROUTES.campaigns.yet +
            "/" +
            this.$route.params.campaignNo +
            "/" +
            this.$route.params.page_no,
          configs
        )
        .then((res) => {
          this.pagination = res.data.page;
          this.proofList = res.data.list;
          if (res.data.page.curPage != 1) {
            this.pagination.prev = true
          }
          if (res.data.page.curPage < res.data.page.endPage) {
            this.pagination.next = true
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style lang="scss" scoped>
.campaign-welcome {
  border: 2px solid black;
  border-radius: 5px;
  padding: 10px 20px;
  margin: 10px 0;
  text-align: start;
}

.campaign-title {
  font-size: 1.5rem;
  font-family: "NanumBarunpen";
}

.capmaign-info {
  font-family: "NanumBarunpen";
}

.custom-white {
  background: var(--white-color);
}

.campaign-info {
  font-family: "NanumBarunpen";
  border: 2px solid black;
  display: block;
  border-radius: 5px;
  padding: 10px 20px;
  margin: 10px 0;
  min-height: 440px;
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
.c-btn {
  font-family: "S-CoreDream-7ExtraBold";
  border: 2px solid black;
  border-radius: 10px;
}

.no-text {
  margin: 100px 0;
}
</style>
