<template>

  <div class="body-con wrapper">
    <Header></Header>

    <div class="main-con">
      <div class="fw-light pt-3 pb-3 px-5 d-flex flex-column align-items-start justify-content-center">
        <h1 class="py-2">Verbal math battles.</h1>
        <h1 class="py-2">Compete with anyone.</h1>
        <h1 class="py-2">Anywhere.</h1>
      </div>

      <div class="align-items-center pt-3 px-5 flex-grow-1">
        <div class="card bg-transparent border-0">
          <img src="../assets/static/images/image.png" class="card-img-top" alt="first-image">
        </div>
      </div>
    </div>

  </div>

</template>

<script>
//var color = 0
// import axios from 'axios'
import Header from "./Header"

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  components: {
    Header
  },
  data: function () {
    return {}
  },
  methods: {},
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/*@import "../assets/static/styles/style.css";*/
#main_screen_div {
  display: flex;
  flex-direction: column;
  height: 100vh;
  margin: 0;
  padding: 0;
}
</style>
