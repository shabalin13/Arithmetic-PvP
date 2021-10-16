<template>

  <div class="body-con">
    <Header></Header>

    <div class="main-con wrapper">

      <div class="pt-3 px-2 d-flex flex-column flex-fill">

        <div class="1-place py-3">

          <div class="card bg-transparent border-0 d-flex align-items-center text-break text-center">
            <h1 class="fw-light fst-italic border-bottom border-2 border-dark">1st place <i class="bi bi-award"></i></h1>
            <h2 class="" id="first_place_player">None</h2>
          </div>

        </div>

        <div class="d-flex flex-row justify-content-around py-3">

          <div class="card bg-transparent px-2 border-0 d-flex align-items-center text-break text-center">
            <h2 class="fw-light fst-italic border-bottom border-2 border-dark">2nd place</h2>
            <h3 class="" id="second_place_player">None</h3>
          </div>

          <div class="card bg-transparent border-0 d-flex align-items-center text-break text-center">
            <h2 class="fw-light fst-italic border-bottom border-2 border-dark">3rd place</h2>
            <h3 class="" id="third_place_player">None</h3>
          </div>

        </div>

      </div>

      <div class="p-2 flex-fill">
        <div class="overflow-auto text-center">
          <table class="table table-hover table-light">
            <thead class="table-success sticky-top">
            <tr>
              <th class="border-0" scope="col">#</th>
              <th class="border-0" scope="col">Nickname</th>
              <th class="border-0" scope="col">Avg speed(eq/min)</th>
<!--              <th class="border-0" scope="col">Total accuracy</th>-->
            </tr>
            </thead>
            <tbody>
            <tr v-for="(item, index) in sorted_user_top" v-bind:key="item.pk">
                <th scope="row">{{ index + 1 }}</th>
                <td>{{ item.player.user.username }}</td>
                <td>{{ item.avg_speed }}</td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>

    </div>

  </div>

</template>

<script>
import Header from "./Header";
import axios from "axios";

export default {
  name: "Statistics",
  components: {Header},
  data(){
    return{
      room_id: null,
      sorted_user_top: [],
      first_person: null,
      second_person: null,
      third_person: null,
      start_time: null,
      avg_speeds: null,
      topPlayersTimer: null
    }
  },
  methods: {
    // get the user top by current game
    getTop(){
      axios.get("/api/get_rr_stats/" + this.room_id.toString() + "/")
          .then(response => {
            // console.log(response.data)
            this.formTable(response.data)
          })
          .catch(error => {
            if (error.response.status === 401) {
              // clearInterval(this.peopleTimer)
              this.$router.push("/signIn")
            }
            // alert(error);
            // console.log(error)
          })
    },
    // prepare the given data from the server (sort by places and compute the average speeds)
    formTable(user_top){
      this.sorted_user_top = user_top.sort(function (a,b){return a.place - b.place})
      document.getElementById("first_place_player").innerText = this.sorted_user_top[0].player.user.username
      if (this.sorted_user_top.length >= 2){
        document.getElementById("second_place_player").innerText = this.sorted_user_top[1].player.user.username
      }
      if (this.sorted_user_top.length >= 3){
        document.getElementById("third_place_player").innerText = this.sorted_user_top[2].player.user.username
      }
      for (let i = 0; i < this.sorted_user_top.length; i ++){
        let myDate1 = new Date(this.sorted_user_top[i].start_time);
        let myDate2 = new Date(this.sorted_user_top[i].last_activity);
        let result1 = myDate1.getTime();
        // console.log("Start time: " + result1.toString())
        let result2 = myDate2.getTime();
        // console.log("Last activity time: " + result2.toString())
        this.sorted_user_top[i]['avg_speed'] = ((this.sorted_user_top[i].task_index) * 60000) / (result2 - result1)
      }
    }
  },
  created() {
    this.room_id = this.$router.currentRoute.params.room_id || this.$cookies.get("lrid")
    if (this.room_id !== null){
      this.topPlayersTimer = setInterval(this.getTop, 1000)
    }else{
      this.$router.push("/")
    }
  },
  destroyed() {
    if (this.topPlayersTimer !== null)
      clearInterval(this.topPlayersTimer)
  }
}
</script>

<style scoped>

</style>