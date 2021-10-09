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
<!--              <th class="border-0" scope="col">Avg speed(eq/s)</th>-->
<!--              <th class="border-0" scope="col">Total accuracy</th>-->
            </tr>
            </thead>
            <tbody>
            <tr v-for="(item, index) in sorted_user_top" v-bind:key="item.pk">
                <th scope="row">{{ index }}</th>
                <td>{{ item.player.user.username }}</td>
<!--                <td>1</td>-->
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
      // users_top: [],
      sorted_user_top: [],
      first_person: null,
      second_person: null,
      third_person: null
    }
  },
  methods: {
    getTop(){
      axios.get("/api/get_rr_stats/" + this.room_id.toString() + "/")
          .then(response => {
            // this.users_top = response.data
            // console.log(this.users_top)
            console.log(response.data)
            this.formTable(response.data)
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
    formTable(user_top){
      this.sorted_user_top = user_top.sort(function (a,b){return a.place - b.place})
      document.getElementById("first_place_player").innerText = this.sorted_user_top[0].player.user.username
      if (this.sorted_user_top.length >= 2){
        document.getElementById("second_place_player").innerText = this.sorted_user_top[1].player.user.username
      }
      if (this.sorted_user_top.length >= 3){
        document.getElementById("third_place_player").innerText = this.sorted_user_top[2].player.user.username
      }
    }
  }, created() {
    this.room_id = this.$router.currentRoute.params.room_id
    console.log("RoomId " + this.room_id.toString())
    if (this.room_id !== undefined){
      setInterval(this.getTop, 1000)
    }
  }
}
</script>

<style scoped>

</style>