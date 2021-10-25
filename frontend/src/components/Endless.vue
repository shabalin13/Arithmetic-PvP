<template>
  <div class="body-con wrapper">
    <Header></Header>

    <div v-if="showModal" style="display: flex;
    flex-direction: column">
    <transition name="modal">
        <EndlessCustomizationModel @runEndlessMode="(...args)=>runEndlessMode(...args)"></EndlessCustomizationModel>
    </transition>
  </div>

    <div class="main-con">
      <div class="progress_bars px-4 my-3">

        <div class="row d-flex flex-row align-items-center justify-content-center" aria-valuenow="10">
          <div class="col-9">
            <div class="progress flex-fill">
              <div class="progress-bar bg-danger" role="progressbar"
                 aria-valuemin="0" aria-valuemax="100" v-bind:style="{width: (remainingTime / maxTime) * 100 + '%'}"></div>
              </div>
            </div>
          </div>
        </div>

      <div class="align-items-end mb-2 px-4">
        <h2>
          Solved: {{ solved }}
        </h2>
        <h2 style="color: red">
          Health: {{ health }}
        </h2>
      </div>

      <Screen v-bind="{'inputChecking': checking, 'parentCurrentTask': current_task, 'parentInputNumber': input_number}"></Screen>

      <Keyboard @changeInput="changeInput($event)" v-bind="{'parentInput': input_number}"></Keyboard>

    </div>

  </div>
</template>

<script>
import Screen from "./Screen";
import Keyboard from "./Keyboard";
import {generateQuestion, levels_conf, getRandomInt} from "../assets/static/js/func"
import EndlessCustomizationModel from "./EndlessCustomizationModel";


export default {
  name: "Endless",
  components: {Keyboard, Screen, EndlessCustomizationModel},
  data(){
    return{
      health: 3,
      solved: 0,
      record: 0,
      maxTime: 6,
      overTime: null,
      remainingTime: 6,
      // questions: "1 + 1 = ",
      answer: "2",
      current_task: "1 + 1 = ",
      timeReduceTimer: null,
      input_number: "",
      checking: -1,
      showModal: false,
      possible_expression_types: []

    }
  },
  methods: {
    reduceTime(){
      this.remainingTime -= 0.5
      if (this.remainingTime === 0){
        this.health -= 1
        if (this.health === 0){
          alert("Looser")
          if (this.timeReduceTimer !== null){
            clearInterval(this.timeReduceTimer)
          }
          this.$router.push("/newGame")
        }else{
          this.remainingTime = this.overTime
        }
      }
    },
    changeInput(number){
      this.checking = 0
      this.input_number = number
      this.submitAnswer()
    },
    submitAnswer() {
      if (this.input_number === this.answer.toString()){
        this.checking = 2
        this.input_number = ""
        this.solved += 1
        this.getQuestion()
      }else{
        this.checking = 1
      }
    },
    getQuestion(){
      let choice = getRandomInt(0, 3)
      let level_ = levels_conf[this.possible_expression_types[choice]]
      console.log(level_)
      let generation = generateQuestion(level_)
      this.current_task = generation["task"]
      this.answer = generation["answer"]
      this.remainingTime = this.overTime
      this.checking = -1
    },
    runEndlessMode(args){
      console.log(args)
      this.showModal = false
      this.maxTime = parseInt(args.time)
      this.overTime = this.maxTime + 0.5
      if (args.diff === "easy"){
        this.possible_expression_types = ['level1', 'level2', 'level3']
      }else if (args.diff === "norm"){
        this.possible_expression_types = ['level4', 'level5', 'level6']
      }else if (args.diff === "hard"){
        this.possible_expression_types = ['level7', 'level8', 'level8']
      }else{
        this.possible_expression_types = ['level10', 'level11', 'level12']
      }
      this.getQuestion()
      this.timeReduceTimer = setInterval(this.reduceTime, 500)

      // alert(diff + "" + time)
    }
  }, created() {
    this.showModal = true
    /*this.overTime = this.maxTime + 0.5
    this.timeReduceTimer = setInterval(this.reduceTime, 500)
    let generated = generateQuestion2(this.kind, this.level)
    this.current_task = generated["task"]
    this.answer = generated["answer"]*/
  }
}
</script>

<style scoped>


</style>