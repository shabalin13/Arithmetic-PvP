<template>

  <div class="body-con bg-image" style="background-color: #cccccc;"
  :style="{'background-image': 'url(' + require('../assets/static/images/alternative_welcome_back.jpg') + ')'}">
    <Header></Header>

    <div class="main-con mask" style="background-color: rgba(204, 204, 204, 0.6);">
      <div class="fw-light pt-3 pb-3 px-5 d-flex flex-column align-items-start justify-content-center">
        <transition name="fade" mode="out-in">
          <h1 v-if="show1" class="py-2">Verbal math battles.</h1>
        </transition>
        <transition name="fade">
          <h1 v-if="show2" class="py-2">Compete with anyone.</h1>
        </transition>
        <transition name="fade">
          <h1 v-if="show3" class="py-2">Anywhere.</h1>
        </transition>

<!--        <h1 class="py-2">Verbal math battles.</h1>
        <h1 class="py-2">Compete with anyone.</h1>
        <h1 class="py-2">Anywhere.</h1>-->
      </div>
      <div class="pt-3 pb-3 px-5" style="position: absolute; bottom: 0; right: 0" >
          <vue-typed-js v-if="show" :strings="all_answers" :typeSpeed="500" :loop="true" @onStringTyped="verifyAnswer()" :fadeOut="true">
          <div>
            <h3 id="current_typed_question">{{ current_example }} <span class="typing" id="current_typed_number"></span></h3>
<!--            <b-spinner type="grow" label="Spinning" v-if="checking === 1" variant="danger"></b-spinner>-->
<!--            <b-spinner type="grow" label="Spinning" v-else-if="checking === 2" variant="success"></b-spinner>-->
          </div>
        </vue-typed-js>
        </div>
    </div>
  </div>

<!--      <div class="align-items-center pt-3 px-5 flex-grow-1">
        <div class="card bg-transparent border-0 align-items-end">
          <img src="../assets/static/images/image.png" class="card-img-top" alt="first-image" style="max-height: 450px; max-width: 560px">
        </div>
      </div>

    </div>


  </div>-->

<!--  <div
  class="bg-image"
  style="
    background-image: url('https://mdbootstrap.com/img/new/fluid/nature/012.jpg');
    height: 100vh;
  "
>
  <div class="mask" style="background-color: rgba(178, 60, 253, 0.6);">
    <div class="d-flex justify-content-center align-items-center h-100">
      <h1 class="text-white mb-0">Page title</h1>
    </div>
  </div>
</div>-->

</template>

<script>
import Header from "./Header"
// documentation https://github.com/Orlandster/vue-typed-js
import VueTypedJs from 'vue-typed-js'
import Vue from "vue";

Vue.use(VueTypedJs)

export default {
  name: 'HelloWorld',
  data(){
    return{
      examples: ['6 × (2 + 4) = ', '7 × (8 + 3) = ', '(4 + 7) × 1 = ',
                '(12 + 3) × 8 = ', '(1 + 1) × 1 = ',  '9 × (7 + 8) = ',
                '10 × (16 + 1) = ', '(3 + 4) × 9 = ', '2 × (4 + 11) = '],
      answers: {'6 × (2 + 4) = ': [[16, 36, 48], 36],
                '7 × (8 + 3) = ': [[77, 59, 29], 77],
                '(4 + 7) × 1 = ': [[28, 12, 11], 11],
                '(12 + 3) × 8 = ': [[120, 99, 36], 120],
                '(1 + 1) × 1 = ': [[1, 3, 2], 2],
                '9 × (7 + 8) = ': [[71, 135, 79], 135],
                '10 × (16 + 1) = ': [[161, 26, 170], 170],
                '(3 + 4) × 9 = ': [[31, 63, 39], 63],
                '2 × (4 + 11) = ': [[30, 19, 26], 30]},
      all_answers: ['16', '36', '48', '77', '59', '29', '28', '12', '11', '120', '99', '36', '4', '3', '2', '71', '135', '79', '161', '26', '170', '31', '63', '39', '30', '19', '26'],
      checking: 0,
      current_example: "",
      show: false,
      show1: false,
      show2: false,
      show3: false,
    }
  },
  props: {
    msg: String
  },
  components: {
    // eslint-disable-next-line vue/no-unused-components
    Header
  }, created() {
    this.current_example = this.examples[this.randomInteger(0, this.examples.length - 1)]
    console.log("First example: " + this.current_example)
    this.show = true
  },
  methods: {
    verifyAnswer(){
      let num_text = document.getElementById("current_typed_number")
      let q_text = document.getElementById("current_typed_question")
      let num = num_text.textContent
      console.log("New: " + num)
      // let correct = false
      if (this.answers[this.current_example][1].toString() === num){
        // this.checking = 2
        q_text.style.color = '#00ff00'
        this.current_example = this.examples[this.randomInteger(0, this.examples.length - 1)]
        // correct = true
      }else{
        q_text.style.color = '#9c0a0a'
        // this.checking = 1
      }
      setTimeout(function (){
        q_text.style.color = '#000000'
      }, 300)
    },
    randomInteger(min, max) {
    // получить случайное число от (min-0.5) до (max+0.5)
      let rand = min - 0.5 + Math.random() * (max - min + 1);
      return Math.round(rand);
  },
    appearTitle(num){
      if (num === 0)
        this.show1 = true
      else if (num === 1)
        this.show2 = true
      else if (num === 2)
        this.show3 = true
    }
  },
  mounted() {
    setTimeout(this.appearTitle, 1500, 0)
    setTimeout(this.appearTitle, 3000, 1)
    setTimeout(this.appearTitle, 4500, 2)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


</style>
