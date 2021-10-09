<template>
  <div class="wrapper">
    <Header></Header>

    <div class="fw-light">
      <div class="card bg-transparent border-0 border-bottom">
        <img src="../assets/static/images/number-1.png" alt="first-image">
      </div>
    </div>

    <div class="fw-light">
      <div class="card bg-transparent border-0 border-bottom">
        <img src="../assets/static/images/second-place.png" alt="first-image">
      </div>
    </div>

    <div class="fw-light">
      <div class="card bg-transparent border-0 border-bottom">
        <img src="../assets/static/images/third-place.png" alt="first-image">
      </div>
    </div>
  </div>

</template>

<script>
import Header from "./Header";

export default {
  name: "Statistics",
  components: {Header}
}
</script>

<style scoped>

</style>