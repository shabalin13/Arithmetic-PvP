<template>

  <div class="body-con">
    <b-overlay class="body-con" :show="showLoading">
      <Header></Header>

     <div class="main-con" :aria-hidden="showLoading ? 'true' : null">

      <div class="d-flex flex-row px-2 py-2">

        <div class="user-logo py-3 px-2">
          <svg xmlns="http://www.w3.org/2000/svg" width="84" height="84" fill="currentColor"
               class="bi bi-person-square" viewBox="0 0 16 16">
            <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
            <path
                d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm12 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1v-1c0-1-1-4-6-4s-6 3-6 4v1a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12z"/>
          </svg>
        </div>

        <div class="user d-flex flex-column text-start justify-content-center flex-grow-1 py-3 px-2">
          <div class="fw-light fst-italic fs-4 user-rank">
            <p>Newbie</p>
          </div>
          <div class="user-name">
            <h3>{{ username }}</h3>
          </div>
        </div>

        <div class="user-rating d-flex flex-column justify-content-center py-3 px-2 ">
          <div class="fw-light fs-5 pb-2">
            <span>Rating:</span>
          </div>
          <div
              class="border rounded-3 border-info bg-info text-dark fs-6 d-flex align-items-center justify-content-center flex-fill">
            <span>{{ rating }}</span>
          </div>
        </div>


      </div>

      <div class="flex-grow-1">
        <div class="row m-0 p-0">

        <div class="col-6 user-links border-end border-dark d-flex flex-column">

          <div class="link1 flex-fill p-3">
            <button type="button" class="btn btn-success w-100">Skins shop</button>
          </div>

          <div class="link2 flex-fill p-3">
            <button type="button" class="btn btn-success w-100">Your skins</button>
          </div>

          <div class="link3 flex-fill p-3">
            <button type="button" class="btn btn-success w-100">Last games</button>
          </div>

          <div class="link4 flex-fill p-3">
            <button type="button" class="btn btn-success w-100">Settings</button>
          </div>

          <div class="link4 flex-fill p-3">
            <button type="button" class="btn btn-danger w-100" @click="logout()">Logout</button>
          </div>

        </div>

        <div class="col-6 user-stats d-flex flex-column">

          <div class="stat1 flex-fill pb-4">
            <div class="fw-light fs-6 text-muted pb-2">
              <span>Total average speed:</span>
            </div>
            <div
                class="border rounded-1 border-warning bg-light text-warning fs-6 d-flex align-items-center justify-content-center">
              <span> {{ avg_speed }}</span>
            </div>
          </div>

          <div class="stat2 flex-fill pb-4">
            <div class="fw-light fs-6 text-muted pb-2">
              <span>Total average accuracy:</span>
            </div>
            <div
                class="border rounded-1 border-warning bg-light text-warning fs-6 d-flex align-items-center justify-content-center">
              <span>{{ avg_accuracy }}</span>
            </div>
          </div>

          <div class="stat3 flex-fill pb-4">
            <div class="fw-light fs-6 text-muted pb-2">
              <span>Total solved tasks:</span>
            </div>
            <div
                class="border rounded-1 border-warning bg-light text-warning fs-6 d-flex align-items-center justify-content-center">
              <span>{{ tasks_solved }}</span>
            </div>
          </div>

          <div class="stat4 flex-fill pb-4">
            <div class="fw-light fs-6 text-muted pb-2">
              <span>Total rating solved tasks:</span>
            </div>
            <div
                class="border rounded-1 border-warning bg-light text-warning fs-6 d-flex align-items-center justify-content-center">
              <span>{{ rating_tasks_solved }}</span>
            </div>
          </div>

          <div class="stat4 flex-fill pb-4">
            <div class="fw-light fs-6 text-muted pb-2">
              <span>Total number of games:</span>
            </div>
            <div
                class="border rounded-1 border-warning bg-light text-warning fs-6 d-flex align-items-center justify-content-center">
              <span>{{ matches_played }}</span>
            </div>
          </div>

        </div>

      </div>
      </div>



    </div>

  </b-overlay>

  </div>

</template>

<script>
import Header from "@/components/Header";
import axios from "axios";
import store from "../vuex/store";

export default {
  name: "User",
  components: {Header},
  data(){
    return{
      username: "",
      rating: "",
      avg_accuracy: "",
      avg_speed: "",
      matches_played: "",
      rating_tasks_solved: "",
      tasks_solved: "",
      showLoading: false
    }
  },
  created() {
    this.getUserInfo()
  },
  methods: {
    // get info about myself (username, rating, average speed/accuracy ans so on)
    getUserInfo(){
      this.showLoading = true
      axios.get("/api/get_player_overall_stats/")
          .then(response => {
            console.log(response.data)
            let parse_data = response.data
            this.username = parse_data.user.username
            this.rating = parse_data.rating
            this.avg_accuracy = parse_data.avg_accuracy
            this.avg_speed = parse_data.avg_speed
            this.matches_played = parse_data.matches_played
            this.rating_tasks_solved = parse_data.rating_tasks_solved
            this.tasks_solved = parse_data.tasks_solved
            this.showLoading = false
          })
          .catch(error => {
            if (error.response.status === 401) {
              this.$router.push("/signIn")
            }
            alert(error);
            console.log(error)
          })
    },
    logout(){
      if(confirm("Do you really want to logout?")){
        axios.defaults.headers.common['Authorization'] = ''
        store.state.access_token = ''
        store.state.refresh_token = ''
        localStorage.setItem("access_token", '')
        localStorage.setItem("refresh_token", '')
        this.$router.push("/")
      }
    }
  }
}
</script>

<style scoped>

</style>