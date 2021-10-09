<template>

  <div class="body-con">
    <Header></Header>

    <div class="main-con">

      <div class="container pt-3 mt-3">

        <h1 class="pb-3 text-uppercase text-center">Waiting for the rest of the participants</h1>

        <div class="pb-3">
          <h5 class="fw-light pb-1">Player, share this link with your friends.</h5>

          <h5 class="fw-light pb-1">Happy and successful game!</h5>
        </div>


        <h6 class="fst-italic">Joined players:</h6>

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
          <tr v-for="(item, index) in users_list" v-bind:key="item">
            <th scope="row">{{ index }}</th>
            <td>{{ item.username }}</td>
          </tr>
          </tbody>
        </table>
      </div>

      <div class="container d-flex flex-row justify-content-around align-items-center">
        <a class="mx-1 w-100 btn btn-success" href="#" role="button" @click="startTheGame()">START GAME</a>
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
      players: [],
      peopleTimer: null,
      startGameTimeout: null,
      end_time: null,
      users_list: []
    }
  },
  created() {
    this.room_id = this.$router.currentRoute.params.room_id
    this.start_time = this.$router.currentRoute.params.start_time
    this.end_time = this.$router.currentRoute.params.end_time
    console.log(this.room_id)
    console.log(this.start_time)

    if (this.room_id !== undefined && this.start_time !== undefined && this.end_time !== undefined) {

      this.peopleTimer = setInterval(this.updateNewPeople, 1000)
      var myDate = new Date(this.start_time);
      var result = myDate.getTime();
      console.log("Time of the start: " + result.toString());
      var timeLeft = (result - Date.now())
      console.log("Time left: " + timeLeft.toString())
      this.startGameTimeout = setTimeout(this.startTheGame, timeLeft)
      this.updateNewPeople()

    }
  },
  methods: {
    updateNewPeople() {
      axios.get("/api/get_nicknames/" + this.room_id.toString() + "")
          .then(response => {
            console.log(response)
            this.users_list = response.data
          })
          .catch(error => {
            if (error.response.status === 401) {
              clearInterval(this.peopleTimer)
              this.$router.push("/signIn")
            }
            alert(error);
            console.log(error)
          })
    },
    startTheGame() {
      console.log("Game will start in a second")
      clearInterval(this.peopleTimer)
      clearTimeout(this.startGameTimeout)
      this.$router.push({name: "game", params: {room_id: this.room_id, end_time: this.end_time}})
    }
  }
}
</script>

<style scoped>

</style>