<template>
   <div class="body-con wrapper">
    <Header></Header>

    <div class="main-con">
      <div class="progress_bars px-4 my-3">

      <div class="row d-flex flex-row align-items-center justify-content-center" aria-valuenow="10">
        <div class="col-9">
          <div class="progress flex-fill">
            <div class="progress-bar progress-bar-striped" role="progressbar"
                 aria-valuemin="0" aria-valuemax="100" v-bind:style="{width: (task_index) * (100 / amount_of_questions) + '%'}"></div>
          </div>
        </div>
      </div>

    </div>

      <div class="px-4">
        <div class="row">
          <h4> Seconds Passed: {{ timePassed }} sec</h4>
        </div>
        <div class="row">
          <h4> Your Best Time: {{ bestTime }} sec</h4>
        </div>
      </div>

      <Screen v-bind="{'inputChecking': checking, 'parentCurrentTask': current_task, 'parentInputNumber': input_number}"></Screen>


      <Keyboard @changeInput="changeInput($event)" v-bind="{'parentInput': input_number}"></Keyboard>

    </div>

  </div>
</template>

<script>
import {generateQuestion, levels_conf} from "../assets/static/js/func"
import Screen from "./Screen";
import Keyboard from "./Keyboard";
import axios from "axios";

export default {
  name: "CampaignGame",
  components: {
    Screen, Keyboard
  },
  data() {
    return {
      level: null,
      task_index: 0,
      checking: -1,
      current_task: "",
      input_number: "",
      amount_of_questions: 10,
      answer: "",
      startGame: null,
      timePassed: 0,
      timer: null,
      bestTime: 0
    }
  },
  methods: {
    getQuestion() {
      if (this.task_index <= 9) {
        let generation = generateQuestion(levels_conf['level' + this.level.index])
        this.current_task = generation.task.replace("*", '×')
        this.answer = generation.answer.toString()
        this.checking = -1
      } else {
        alert("Congratulations")
        // this.$router.push("/levels")
        this.submitGame()
      }
    },
    changeInput(input_num) {
      this.checking = 0
      this.input_number = input_num
      // this.checking = 0
      this.submitAnswer()
    },
    submitAnswer() {
      if (this.input_number === this.answer) {
        this.checking = 2
        this.input_number = ""
        this.task_index += 1
        this.getQuestion()
      } else {
        this.checking = 1
      }
    },
    submitGame(){
      let session_id = ((new Date().getTime() - this.startGame) / 2) - 15324
      axios.post('api/submit_level_info/', {session_id: session_id, index: this.level.index})
        .then(response => {
          console.log(response)
          this.$router.push("/levels")
        })
        .catch(error => {
          console.log(error)
        })
    },
    handler: function handler(event) {
      event.preventDefault()
      event.returnValue = ""
    },
    incrementTimer(){
      this.timePassed += 1
    }
  },
  created() {
    /*let decode_trick = this.$cookies.get('cl')
    if (decode_trick !== null){
      // alert(typeof decode_trick)
      let num = decode_trick.substring(9, decode_trick.indexOf('__', 10))
      this.level = Math.round((parseInt(num) + 2) / 13)
      if (isNaN(this.level)){
        this.$cookies.remove("cl")
        this.$router.push("/levels")
      }else{

      }
    }else{
      this.level = this.$router.currentRoute.params.level
      if (this.level !== undefined){
        let trick = this.level.index * 13 - 2
        this.$cookies.set('cl', 'sensors__' + trick + '__data', '1d')
        this.getQuestion()
    }else{
      this.$cookies.remove("cl")
      this.$router.push("/levels")
    }
    }*/

    this.level = this.$router.currentRoute.params.level
    this.startGame = new Date().getTime()
    window.addEventListener('beforeunload', this.handler)
    if (this.level !== undefined){
      this.bestTime = this.level.time / 1000
      this.getQuestion()
      this.timer = setInterval(this.incrementTimer, 1000)
    }else{
      this.$router.push("/levels")
    }
    /*if (this.level === undefined){
      let decode_trick = this.$cookies.get('cl')
      if (decode_trick !== null){
      // alert(typeof decode_trick)
      let num = decode_trick.substring(9, decode_trick.indexOf('__', 10))
      this.level = {index: Math.round((parseInt(num) + 2) / 13)}
      if (isNaN(this.level.index)){
        this.$cookies.remove("cl")
        this.$router.push("/levels")
      }else{

      }
    }else{
      let trick = this.level.index * 13 - 2
      this.$cookies.set('cl', 'sensors__' + trick + '__data', '1d')
    }
  }*/
  },
  destroyed() {
    if (this.timer !== null){
      clearInterval(this.timer)
    }
    window.removeEventListener('beforeunload', this.handler, false)
  }
}
</script>

<style scoped>

</style>