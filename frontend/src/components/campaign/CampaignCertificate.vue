<template>
  <div>
    <BarChart />
    <UserCertificate />
    <UserCertificatePosts />
  </div>
</template>

<script>
import BarChart from "./BarChart.vue";
import UserCertificate from "./UserCertificate";
import UserCertificatePosts from "./UserCertificatePosts";

export default {
  components: { BarChart, UserCertificate, UserCertificatePosts },
};
</script>

<style></style>
