<template>

  <div class="body-con">
    <Header></Header>

    <div class="main-con" style="background-color: #292b2c">

      <div class="container pt-3 mt-3">

        <h1 class="pb-3 text-uppercase text-center text-white">Waiting for the rest of the participants</h1>

        <div class="pb-3">
<!--          <h5 class="fw-light pb-1">Player, share this link with your friends.</h5>-->

          <h5 class="fw-light pb-1 text-white">Happy and successful game!</h5>

          <h5 class="fw-light pb-1 text-white" v-if="timeLeft !== null">Time left: {{ timeLeft }}s</h5>
        </div>


        <h6 class="fst-italic text-white">Joined players:</h6>

      </div>

      <div class="container mb-2 overflow-auto">
        <table class="table table-hover table-light">
          <thead class="table-success sticky-top">
          <tr class="">
            <th scope="col">#</th>
            <th scope="col">Nickname</th>
          </tr>
          </thead>
          <tbody id="players_container">
          <tr v-for="(item, index) in users_list" v-bind:key="item.pk">
            <th scope="row">{{ index + 1 }}</th>
            <td>{{ item.username }}</td>
          </tr>
          </tbody>
        </table>
      </div>

      <div class="container d-flex flex-row justify-content-around align-items-center">
        <a class="mx-1 w-100 btn btn-success" href="#" role="button" @click="startTheGame('click')">START GAME</a>
      </div>

    </div>

  </div>

</template>

<script>
import Header from "./Header";
import axios from "axios";

export default {
  name: "WaitingRoom",
  components: {Header},
  data() {
    return {
      room_id: null,
      start_time: null,
      start_time_ms: null,
      players: [],
      peopleTimer: null,
      startGameTimeout: null,
      timeLeft: null,
      end_time: null,
      users_list: [],
      gameExpired: false
    }
  },
  created() {
    this.room_id = this.$router.currentRoute.params.room_id || this.$cookies.get("lrid")
    this.start_time = this.$router.currentRoute.params.start_time || this.$cookies.get("st")
    this.end_time = this.$router.currentRoute.params.end_time || this.$cookies.get("et")

    if (this.room_id !== null && this.start_time !== null && this.end_time !== null) {

      let myDate = new Date(this.start_time);
      let result = myDate.getTime();
      this.start_time_ms = result
      // console.log("Time of the start: " + result.toString());
      let timeLeft = (result - Date.now());
      // console.log("Time left: " + timeLeft.toString())
      if (timeLeft > 0){
        this.peopleTimer = setInterval(this.updateNewPeople, 1000)
        this.startGameTimeout = setTimeout(this.startTheGame, timeLeft, "")
        this.updateNewPeople()
      }else{
        this.$cookies.remove("lrid")
        this.$cookies.remove("st")
        this.$cookies.remove("et")
        this.gameExpired = true
        this.$router.push("/")
      }
    }else{
        this.$cookies.remove("lrid")
        this.$cookies.remove("st")
        this.$cookies.remove("et")
        this.gameExpired = true
        this.$router.push("/")
    }
  },
  methods: {
    // Check the newest people in the room and fill the table
    updateNewPeople() {
      axios.get("/api/get_nicknames/" + this.room_id.toString() + "/")
          .then(response => {
            // console.log(response)
            this.users_list = response.data
          })
          .catch(error => {
            if (error.response.status === 401) {
              clearInterval(this.peopleTimer)
              this.$router.push("/signIn")
            }
            // alert(error);
            // console.log(error)
          })

      let myDate = new Date();
      let result = myDate.getTime();
      this.timeLeft = ((this.start_time_ms - result) / 1000) | 0
    },
    // Start the game event triggered, if it's time to start (~1 min left after room creation (determined by the server)) or here already 4 people and they can press the button
    startTheGame(event){
      if (this.room_id !== undefined && this.start_time !== undefined && this.end_time !== undefined && (event === "" || (event === "click" && this.users_list.length === 4))) {
        // console.log("Game will start in a second")
        clearInterval(this.peopleTimer)
        clearTimeout(this.startGameTimeout)
        this.$router.push({
          name: "game",
          params: {room_id: this.room_id, end_time: this.end_time, start_time: this.start_time}
        })
      }
    }
  },
  destroyed() {
    if (this.startGameTimeout !== null){
      clearTimeout(this.startGameTimeout)
    }
    if (this.peopleTimer !== null){
      clearInterval(this.peopleTimer)
    }
  },
  beforeRouteLeave (to, from , next) {
    if (to.name !== "game" && !this.gameExpired){
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