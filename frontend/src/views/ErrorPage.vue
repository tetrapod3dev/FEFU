<template>
  <div class="home">
    <core-hero
      subtitle="잘못 온 거 같아요"
      :mainimage="require('@/assets/images/error.png')"
      backimage="https://cdn.imweb.me/upload/S20200610f999ac5b4f199/be7483f8a30b9.gif"
      max-height="404"
      ><template slot="footer">
        <v-row>
          <v-col>
            <router-link
              tag="a"
              :to="{ name: 'Home' }"
              class="c-btn--text"
              :class="'c-btn--text-' + $vuetify.breakpoint.name"
            >
              메인으로 돌아가기
              <v-img
                style="cursor: pointer; margin-top: 3px"
                :width="$vuetify.breakpoint.smAndDown ? 15 : 17"
                :height="$vuetify.breakpoint.smAndDown ? 15 : 17"
                class="c-btn--text-icon"
                contain
                :src="require('@/assets/illust/arrow-right.svg')"
              />
            </router-link>
          </v-col>
        </v-row>
      </template>
    </core-hero>
  </div>
</template>

<script>
import CoreHero from "@/components/core/Hero";

export default {
  name: "ErrorPage",
  components: {
    CoreHero,
  },
  data() {
    return {};
  },
};
</script>

<style lang="scss" scoped>
.c-btn--text {
  display: inline-block;
  text-decoration: none;
  border-bottom: 2px solid #000000;
  padding: 2px 0;
  font-family: "Nunito", "NanumSquareRound", sans-serif;
  font-size: 16px;
  color: #000000;
  transition: 0.3s;

  &-md,
  &-lg,
  &-xl {
    font-size: 18px;
    line-height: 1.5;
  }
}

.c-btn--text-icon {
  display: inline-block;
}
</style>
