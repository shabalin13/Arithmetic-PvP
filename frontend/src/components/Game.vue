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

      <Screen v-bind="{'inputChecking': checking, 'parentCurrentTask': current_task, 'parentInputNumber': input_number}"></Screen>


      <Keyboard @changeInput="changeInput($event)" v-bind="{'parentInput': input_number}"></Keyboard>

    </div>

  </div>
</template>

<script>
import Header from "./Header";
import Keyboard from "./Keyboard";
import Screen from "./Screen";
import axios from "axios";
const QUESTIONS = 10


export default {
  name: "Game",
  components: {Screen, Header, Keyboard},
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
      gameTimer: null,
      roomExpired: false
    }
  },
  created() {
    // Getting necessary params from previous page (waiting room) or from cookies
    this.room_id = this.$router.currentRoute.params.room_id || this.$cookies.get("lrid")
    this.end_time = this.$router.currentRoute.params.end_time || this.$cookies.get("et")
    this.start_time = this.$router.currentRoute.params.start_time || this.$cookies.get("st")

    // if following data is not defined -> redirects to main page
    if (this.room_id !== null && this.end_time !== null && this.start_time !== null){

      // save this data in cookies in case of some errors, accidentally reloading/exiting
      this.$cookies.set("lrid", this.room_id, "5min")
      this.$cookies.set("et", this.end_time, "5min")
      this.$cookies.set("st", this.start_time, "5min")

      // starts the timers: 1) checks progress of other people 2) checks the end of the game (game is approximately 5 minutes)
      let myDate = new Date(this.end_time);
      let result = myDate.getTime();
      let timeLeft = (result - Date.now());
      console.log("start timer")
      this.gameTimer = setTimeout(this.gameIsOver, timeLeft)
      if (timeLeft > 0){
        this.peopleScoreInterval = setInterval(this.updatePeopleScore, 1000)
        this.getQuestion()
      }

    }else{
      this.roomExpired = true
      this.$router.push("/")
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
              if (response.data.error !== undefined){
                alert(response.data.error)
                this.$router.push("/")
                // remove data about last game since the game expired or this user doesn't corresponds to this game
                this.$cookies.remove("lrid")
                this.$cookies.remove("et")
                this.$cookies.remove("st")
              }else{
                console.log("Rerun")
                this.getQuestion()
              }
            }
          })
          .catch(error =>{
            if (error.response.status === 401){
              this.$router.push("/signIn")
            }else if (error.response.status === 404){
              alert("Game doesn't currently exists")
              this.roomExpired = true
              this.$router.push("/")
              this.$cookies.remove("lrid")
              this.$cookies.remove("et")
              this.$cookies.remove("st")
            }
          })
      }else{
        this.$router.push({name: "statistics", params: {room_id: this.room_id}})
      }
    },
    changeInput(input_num){
      this.input_number = input_num
      this.checking = 0
      this.submitAnswer()
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
    if (to.name !== "statistics" && !this.roomExpired){
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