<template>
  <div class="body-con wrapper">
    <Header></Header>

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
import {generateQuestion2} from "../assets/static/js/func"


export default {
  name: "Endless",
  components: {Keyboard, Screen},
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
      tasks_on_each_level: 20,
      // level: prompt("Enter the level(from 0 to 5 inclusively)"),
      kind: 0,
      level: 0
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
        if (this.solved % this.tasks_on_each_level === 0 && this.solved !== 0){
          if (this.kind % 2 === 1){
              this.level += 1
              alert("Next Level")
          }
          this.kind = Math.abs(1 - this.kind)
        }
        let generation = generateQuestion2(this.kind,this.level)
        this.current_task = generation["task"]
        this.answer = generation["answer"]
        this.remainingTime = this.overTime
        this.checking = -1
      }else{
        this.checking = 1
      }
    }
  }, created() {
    this.overTime = this.maxTime + 0.5
    this.timeReduceTimer = setInterval(this.reduceTime, 500)
    let generated = generateQuestion2(this.kind, this.level)
    this.current_task = generated["task"]
    this.answer = generated["answer"]
  }
}
</script>

<style scoped>

</style>