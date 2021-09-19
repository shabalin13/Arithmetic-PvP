<template>
    <div id="main_screen_div">
      <Header></Header>
      <div class="wrapper d-flex flex-column" style="flex: 1;">
    <div class="container pt-5 m-5">
    <div class="row">
       <div class="col-1"></div>
        <div class="col-5 fw-light p-5 d-flex flex-column align-items-start justify-content-center">
            <h1 class="py-2">Verbal math battles.</h1>
            <h1 class="py-2">Compete with anyone.</h1>
            <h1 class="py-2">Anywhere.</h1>
        </div>
        <div class="col-1"></div>

        <div class="col-5 d-flex align-items-center">
            <div class="card bg-transparent border-0">
                <img src="../assets/static/images/image.png" alt="first-image">
            </div>

        </div>
    </div>
</div>
</div>
    </div>
</template>

<script>
//var color = 0
import axios from 'axios'
import Header from "./Header"
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  components: {
    Header
  },
  data: function (){
    return{

    }
  },
  methods:{
    login(resp){
      resp.Zi
      this.$a
    }
  },
  created() {
    axios.get("", {
      params: {

      }
    }).catch(e => {
      this.errors.push(e)
    }).then(response => {
      print(response)
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  /*@import "../assets/static/styles/style.css";*/
  #main_screen_div{
    display: flex;
    flex-direction: column;
    height:100vh;
    margin: 0;
    padding: 0;
  }
</style>
