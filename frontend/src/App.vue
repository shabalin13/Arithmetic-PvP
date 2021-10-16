<template>
<div id="app">
  <router-view></router-view>
</div>

</template>

<script>

import axios from "axios";
import store from "./vuex/store";
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'


export default {
  name: 'App',
  components: {

  },
  created() {
    this.getAccess()
    setInterval(this.getAccess, 60000)
  },
  beforeCreate() {
    document.title = "ArithmeticPvP"
    store.commit("initializeStore")

    const access = store.state.access_token

    if (access){
      axios.defaults.headers.common['Authorization'] = "JWT " + access
    }else{
      axios.defaults.headers.common['Authorization'] = ''
    }

  },
  methods: {
    // Asks the server the access token in order to be authorized
    getAccess(){
      const accessData = {
        refresh: store.state.refresh_token
      }

      axios.post("/api/v1/jwt/refresh/", accessData)
      .then(response => {
        const access = response.data.access

        localStorage.setItem("access_token", access)
        store.commit("setAccess", access)
        axios.defaults.headers.common['Authorization'] = "JWT " + access
      })
      .catch(error => {
        console.log(error)
      })
    }
  }
}
</script>



<style>
@import "assets/static/styles/style.css";
@import "assets/static/styles/burger.css";
@import "https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css";
@import "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css";
@import "assets/static/styles/signin.css";



#app{
  display: flex;
  flex-direction: column;
  height: 100%;
  margin: 0;
  padding: 0;
}
</style>

