<template>
<div id="app">
  <router-view></router-view>
</div>

</template>

<script>

export default {
  name: 'App',
  components: {

  },
  created() {

  },
  beforeCreate() {
    document.title = "ArithmeticPvP"
  }
}
</script>

<style>
@import "assets/static/styles/style.css";
@import "https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css";
@import "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css";
#app{
  display: flex;
  flex-direction: column;
  height:100vh;
  margin: 0;
  padding: 0;
}
/*#app {*/
/*  font-family: Avenir, Helvetica, Arial, sans-serif;*/
/*  -webkit-font-smoothing: antialiased;*/
/*  -moz-osx-font-smoothing: grayscale;*/
/*  text-align: center;*/
/*  color: #2c3e50;*/
/*  margin-top: 60px;*/
/*}*/
</style>

