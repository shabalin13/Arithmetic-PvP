<template>
  <div class="body-con wrapper">
    <Header></Header>

    <div class="main-con">
      <div class="progress_bars px-4 my-3">

      <div class="row d-flex flex-row align-items-center justify-content-center" v-for="(item, key) in user_list" v-bind:key="key" aria-valuenow="10">
        <div class="col-3">
          <div class="text-truncate"><span class="fw-light">{{ item.player.user.username }}</span></div>
        </div>
        <div class="col-9">
          <div class="progress flex-fill">
            <div class="progress-bar progress-bar-striped" role="progressbar"
                 aria-valuemin="0" aria-valuemax="100" v-bind:style="{width: (item.task_index) * 10 + '%'}"></div>
          </div>
        </div>
      </div>

    </div>

      <div class="equation_canvas px-4 d-flex flex-fill">
        <div class="card bg-light flex-fill text-dark border-0 m-0 p-0" id="eq">
          <div class="card-body d-flex align-items-center justify-content-center">
            <span class="m-0 p-0 fs-1">{{ current_task }} {{ input_number }} </span>

            <b-spinner label="Spinning" v-if="checking === 0"></b-spinner>
            <b-spinner type="grow" label="Spinning" v-else-if="checking === 1" variant="danger"></b-spinner>
            <b-spinner type="grow" label="Spinning" v-else-if="checking === 2" variant="success"></b-spinner>

          </div>
        </div>
      </div>

      <div class="keyboard d-flex flex-column flex-fill px-4 my-3">
        <div class="row my-1 flex-fill">
          <div class="d-grid col-4 mx-auto">
            <button type="button" class="btn btn-outline-dark" @click="changeInput('7')"><span
                class="fs-4 fw-bold">7</span></button>
          </div>
          <div class=" d-grid col-4 mx-auto">
            <button type="button" class="btn btn-outline-dark" @click="changeInput('8')"><span
                class="fs-4 fw-bold">8</span></button>
          </div>
          <div class=" d-grid col-4 mx-auto">
            <button type="button" class="btn btn-outline-dark" @click="changeInput('9')"><span
                class="fs-4 fw-bold">9</span></button>
          </div>
        </div>

        <div class="row my-1 flex-fill">
          <div class="d-grid col-4 mx-auto">
            <button type="button" class="btn btn-outline-dark" @click="changeInput('4')"><span
                class="fs-4 fw-bold">4</span></button>
          </div>
          <div class="d-grid col-4 mx-auto">
            <button type="button" class="btn btn-outline-dark" @click="changeInput('5')"><span
                class="fs-4 fw-bold">5</span></button>
          </div>
          <div class="d-grid col-4 mx-auto">
            <button type="button" class="btn btn-outline-dark" @click="changeInput('6')"><span
                class="fs-4 fw-bold">6</span></button>
          </div>
        </div>

        <div class="row my-1 flex-fill">
          <div class="d-grid col-4 mx-auto">
            <button type="button" class="btn btn-outline-dark" @click="changeInput('1')"><span
                class="fs-4 fw-bold">1</span></button>
          </div>
          <div class="d-grid col-4 mx-auto">
            <button type="button" class="btn btn-outline-dark" @click="changeInput('2')"><span
                class="fs-4 fw-bold">2</span></button>
          </div>
          <div class="d-grid col-4 mx-auto">
            <button type="button" class="btn btn-outline-dark" @click="changeInput('3')"><span
                class="fs-4 fw-bold">3</span></button>
          </div>
        </div>

        <div class="row my-1 flex-fill">
          <div class="d-grid col-4 mx-auto">
            <button type="button" class="btn btn-outline-dark" @click="changeInput('-')"><span
                class="fs-4 fw-bold">-</span></button>
          </div>
          <div class="d-grid col-4 mx-auto">
            <button type="button" class="btn btn-outline-dark" @click="changeInput('0')"><span
                class="fs-4 fw-bold">0</span></button>
          </div>
          <div class="d-grid col-4 mx-auto">
            <button type="button" class="btn btn-outline-dark" @click="changeInput('Backspace')"><span
                class="fs-4 fw-bold">Del</span></button>
          </div>
        </div>

      </div>

    </div>

  </div>
</template>

<script>
import Header from "@/components/Header";
import axios from "axios";
const QUESTIONS = 10


export default {
  name: "Game",
  components: {Header},
  data(){
    return{
      room_id: null,
      end_time: null,
      start_time: null,
      current_task: "",
      input_number: "",
      current_index: 0,
      peopleScoreInterval: null,
      user_list: [],
      checking: -1,
      gameTimer: null
    }
  },
  created() {
    document.addEventListener('keydown', (event) => { this.changeInput(event.key)});
    this.room_id = this.$router.currentRoute.params.room_id
    // console.log("RoomId " + this.room_id.toString())
    this.end_time = this.$router.currentRoute.params.end_time
    // console.log("End Time " + this.end_time)
    this.start_time = this.$router.currentRoute.params.start_time
    // console.log("Start Time " + this.start_time)
    let myDate = new Date(this.end_time);
    let result = myDate.getTime();
    let timeLeft = (result - Date.now());
    // console.log("Time left: " + timeLeft.toString())
    this.gameTimer = setTimeout(this.gameIsOver, timeLeft)
    this.peopleScoreInterval = setInterval(this.updatePeopleScore, 1000)

    if (this.room_id !== undefined && this.end_time !== undefined){
      this.getQuestion()
    }
  },
  methods: {
    // get the next question in the queue, if no questions left, then game is over, go to the statistics page
    getQuestion(){
      if (this.current_index < QUESTIONS - 1){
        axios.get("/api/ranked_room/get_task/" + this.room_id.toString() + "/")
          .then(response =>{
            // console.log(response)
            if (response.data.content !== undefined){
              this.checking = -1
              this.current_task = response.data.content + " = "
              this.current_index = response.data.index
            }else{
              console.log("Rerun")
              this.getQuestion()
            }
          })
          .catch(error =>{
            if (error.response.status === 401){
              this.$router.push("/signIn")
            }
            // alert(error);
            // console.log(error)
          })
      }else{
        this.$router.push({name: "statistics", params: {room_id: this.room_id}})
      }
    },
    // keyboard listener
    changeInput(key){
      console.log(key)
      let input_changed = false;
      switch (key){
        case "0":
          this.input_number += "0"
            input_changed = true
          break
        case "1":
          this.input_number += "1"
            input_changed = true
          break
        case "2":
          this.input_number += "2"
            input_changed = true
          break
        case "3":
          this.input_number += "3"
            input_changed = true
          break
        case "4":
          this.input_number += "4"
            input_changed = true
          break
        case "5":
          this.input_number += "5"
            input_changed = true
          break
        case "6":
          this.input_number += "6"
            input_changed = true
          break
        case "7":
          this.input_number += "7"
            input_changed = true
          break
        case "8":
          this.input_number += "8"
            input_changed = true
          break
        case "9":
          this.input_number += "9"
            input_changed = true
          break
        case "-":
          if (this.input_number === "-"){
            this.input_number = ""
          }else{
            let num = parseInt(this.input_number)
            if (num < 0){
              this.input_number = this.input_number.slice(1,)
            }else{
              this.input_number = "-" + this.input_number
            }
          }
          input_changed = true
          break
        case "Backspace":
          this.input_number = this.input_number.slice(0, -1)
          input_changed = true
          break
      }
      if (input_changed){
        this.checking = 0
        this.submitAnswer()
      }
    },
    // submit answer on the current question, if the answer is correct, then next question loading, otherwise try another answer
    submitAnswer(){
      let num = parseInt(this.input_number)
      if (!isNaN(num)){
         axios.put("/api/ranked_room/submit_task/" + this.room_id.toString() + "/"  + this.input_number +  "/")
            .then(response =>{
              let correct = response.data.is_correct
              if (correct){
                  this.checking = 2
                  this.getQuestion()
                  this.input_number= ""
                  this.current_task = ""
              }else{
                this.checking = 1
              }
            })
            .catch(error =>{
              if (error.response.status === 401){
                this.$router.push("/signIn")
              }
              // alert(error);
              // console.log(error)
            })
      }
    },
    // game over event triggered if timer for the game is expired (~5 minutes) or last question is answered
    gameIsOver(){
      clearInterval(this.peopleScoreInterval)
      this.$router.push({name: "statistics", params: {room_id: this.room_id}})
    },
    // Function which is responsible for getting progress of the competitors
    updatePeopleScore(){
      axios.get("/api/get_rr_progress/" + this.room_id.toString() + "/")
          .then(response => {
            this.user_list = response.data
            // console.log(this.user_list)
          })
          .catch(error => {
            if (error.response.status === 401) {
              clearInterval(this.peopleTimer)
              this.$router.push("/signIn")
            }
            // alert(error);
            // console.log(error)
          })
    },
  },
  destroyed() {
    if (this.peopleScoreInterval !== null)
      clearInterval(this.peopleScoreInterval)
    if (this.gameTimer !== null)
      clearTimeout(this.gameTimer)
  },
  beforeRouteLeave (to, from , next) {
    if (to.name !== "statistics"){
      const answer = window.confirm('Do you really want to leave? Your rating will decrease!')
    if (answer) {
      next()
    } else {
      next(false)
    }
    }else{
      next()
    }
},
}
</script>

<style scoped>

</style>