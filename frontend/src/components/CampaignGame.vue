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

      <Screen v-bind="{'inputChecking': checking, 'parentCurrentTask': current_task, 'parentInputNumber': input_number}"></Screen>


      <Keyboard @changeInput="changeInput($event)" v-bind="{'parentInput': input_number}"></Keyboard>

    </div>

  </div>
</template>

<script>
import {generateQuestion} from "../assets/static/js/func"
import Screen from "./Screen";
import Keyboard from "./Keyboard";
export default {
  name: "CampaignGame",
  components: {
    Screen, Keyboard
  },
  data(){
    return{
      level: null,
      task_index: 0,
      checking: -1,
      current_task: "",
      input_number: "",
      amount_of_questions: 10,
      answer: "",
    }
  },
  methods: {
    getQuestion() {
      if (this.task_index <= 9){
        let generation = generateQuestion(this.level)
        this.current_task = generation.task.replace("*", '×')
        this.answer = generation.answer.toString()
      }else{
        alert("Congratulations")
        this.$router.push("/levels")
      }
    },
    changeInput(input_num){
      this.checking = 0
      this.input_number = input_num
      this.checking = 0
      this.submitAnswer()
    },
    submitAnswer(){
      if (this.input_number === this.answer){
        this.checking = 2
        this.input_number = ""
        this.task_index += 1
        this.getQuestion()
      }else{
        this.checking = 1
      }
    }
  },
  created() {
    this.level = this.$router.currentRoute.params.level
    this.getQuestion()
  }
}
</script>

<style scoped>

</style>