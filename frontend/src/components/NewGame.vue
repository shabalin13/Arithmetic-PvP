<template>
  <!--<b-overlay :show="show" class="d-flex flex-column h-100">
      <Header></Header>
      <div class="d-flex flex-column wrapper" :aria-hidden="show ? 'true' : null">
          <div class="d-md-flex flex-md-column my-md-3 ps-md-3">
              <div class="me-md-3 pt-3 px-3  px-md-5 text-center overflow-hidden">
                  <div class="p-3">
                      <h2 class="display-5">Choose the mode</h2>
                      <p class="lead">Play with friends and meet new people.</p>
                  </div>
                  <div class="ms-auto" v-show="smallScreen">
                      <div class="row d-flex flex-lg-column text-center my-2">
                          <div class="col my-2">
                              <div class="card rounded-3">
                                  <div class="card-body" style="height: 18rem">

                                      <img src="../assets/static/images/levels.svg" alt="levels"
                                           style="width: 5rem; animation: 1.11111s linear -1.11111s infinite normal forwards running breath-f235b970-61a7-4dc9-8bd5-98e617725c44;">
                                      <h4 class="my-3 fw-normal">Campaign</h4>
                                      <p>Play different levels from easiest to hardest ones</p>

                                      <button type="button" class="bg-transparent stretched-link"
                                              style="border: none; color: transparent"></button>
                                  </div>
                              </div>
                          </div>
                          <div class="col my-2">
                              <div class="card rounded-3">
                                  <div class="card-body" style="height: 18rem">
                                      <img src="../assets/static/images/infinity.svg" alt="levels"
                                           style="width: 5rem">
                                      <h4 class="my-3 fw-normal">Endless</h4>
                                      <p>Infinite mode for continuous improvement</p>

                                      <button type="button" class="bg-transparent stretched-link"
                                              style="border: none; color: transparent"></button>
                                  </div>
                              </div>
                          </div>
                      </div>
                      <div class="row d-flex flex-lg-column text-center my-2">
                          <div class="col my-2" onclick="location.href='#';">
                              <div class="card rounded-3">
                                  <div class="card-body" style="height: 18rem">
                                      <svg xmlns="http://www.w3.org/2000/svg" style="width: 5rem"
                                           fill="currentColor"
                                           class="bi bi-door-closed" viewBox="0 0 16 16">
                                          <path d="M3 2a1 1 0 0 1 1-1h8a1 1 0 0 1 1 1v13h1.5a.5.5 0 0 1 0 1h-13a.5.5 0 0 1 0-1H3V2zm1 13h8V2H4v13z"/>
                                          <path d="M9 9a1 1 0 1 0 2 0 1 1 0 0 0-2 0z"/>
                                      </svg>
                                      <h4 class="my-3 fw-normal">Private room</h4>
                                      <p>Create a room and send an invitation link to friends</p>

                                      <button type="button" class="bg-transparent stretched-link"
                                              style="border: none; color: transparent">
                                      </button>
                                  </div>
                              </div>
                          </div>
                          <div class="col my-2" @click="createRankedRoom">
                              <div class="card rounded-3">
                                  <div class="card-body" style="height: 18rem">
                                      <svg xmlns="http://www.w3.org/2000/svg" style="width: 5rem"
                                           fill="currentColor"
                                           class="bi bi-door-open-fill" viewBox="0 0 16 16">
                                          <path d="M1.5 15a.5.5 0 0 0 0 1h13a.5.5 0 0 0 0-1H13V2.5A1.5 1.5 0 0 0 11.5 1H11V.5a.5.5 0 0 0-.57-.495l-7 1A.5.5 0 0 0 3 1.5V15H1.5zM11 2h.5a.5.5 0 0 1 .5.5V15h-1V2zm-2.5 8c-.276 0-.5-.448-.5-1s.224-1 .5-1 .5.448.5 1-.224 1-.5 1z"/>
                                      </svg>
                                      <h4 class="my-3 fw-normal">Public room</h4>
                                      <p>Create an open room to meet new gamers and get experience</p>

                                      <button type="button" class="bg-transparent stretched-link"
                                              style="border: none; color: transparent"></button>
                                  </div>
                              </div>
                          </div>
                      </div>
                  </div>

                  <div class="ms-auto" v-show="!smallScreen">
                      <div class="row text-center my-2">
                          <div class="col my-2">
                              <div class="card rounded-3">
                                  <div class="card-body" style="height: 18rem">

                                      <img src="../assets/static/images/levels.svg" alt="levels"
                                           style="width: 5rem; animation: 1.11111s linear -1.11111s infinite normal forwards running breath-f235b970-61a7-4dc9-8bd5-98e617725c44;">
                                      <h4 class="my-3 fw-normal">Campain</h4>
                                      <p>Play different levels from easiest to hardest ones</p>

                                      <button type="button" class="bg-transparent stretched-link"
                                              style="border: none; color: transparent"></button>
                                  </div>
                              </div>
                          </div>
                          <div class="col my-2">
                              <div class="card rounded-3">
                                  <div class="card-body" style="height: 18rem">
                                      <img src="../assets/static/images/infinity.svg" alt="levels"
                                           style="width: 5rem">
                                      <h4 class="my-3 fw-normal">Endless</h4>
                                      <p>Infinite mode for continuous improvement</p>

                                      <button type="button" class="bg-transparent stretched-link"
                                              style="border: none; color: transparent"></button>
                                  </div>
                              </div>
                          </div>
                          <div class="col my-2" onclick="location.href='#';">
                              <div class="card rounded-3">
                                  <div class="card-body" style="height: 18rem">
                                      <svg xmlns="http://www.w3.org/2000/svg" style="width: 5rem"
                                           fill="currentColor"
                                           class="bi bi-door-closed" viewBox="0 0 16 16">
                                          <path d="M3 2a1 1 0 0 1 1-1h8a1 1 0 0 1 1 1v13h1.5a.5.5 0 0 1 0 1h-13a.5.5 0 0 1 0-1H3V2zm1 13h8V2H4v13z"/>
                                          <path d="M9 9a1 1 0 1 0 2 0 1 1 0 0 0-2 0z"/>
                                      </svg>
                                      <h4 class="my-3 fw-normal">Private room</h4>
                                      <p>Create a room and send an invitation link to friends</p>

                                      <button type="button" class="bg-transparent stretched-link"
                                              style="border: none; color: transparent">
                                      </button>
                                  </div>
                              </div>
                          </div>
                          <div class="col my-2" @click="createRankedRoom">
                              <div class="card rounded-3">
                                  <div class="card-body" style="height: 18rem">
                                      <svg xmlns="http://www.w3.org/2000/svg" style="width: 5rem"
                                           fill="currentColor"
                                           class="bi bi-door-open-fill" viewBox="0 0 16 16">
                                          <path d="M1.5 15a.5.5 0 0 0 0 1h13a.5.5 0 0 0 0-1H13V2.5A1.5 1.5 0 0 0 11.5 1H11V.5a.5.5 0 0 0-.57-.495l-7 1A.5.5 0 0 0 3 1.5V15H1.5zM11 2h.5a.5.5 0 0 1 .5.5V15h-1V2zm-2.5 8c-.276 0-.5-.448-.5-1s.224-1 .5-1 .5.448.5 1-.224 1-.5 1z"/>
                                      </svg>
                                      <h4 class="my-3 fw-normal">Public room</h4>
                                      <p>Create an open room to meet new gamers and get experience</p>

                                      <button type="button" class="bg-transparent stretched-link"
                                              style="border: none; color: transparent"></button>
                                  </div>
                              </div>
                          </div>

                      </div>
                  </div>
              </div>
          </div>
      </div>
  </b-overlay>-->
  <b-overlay class="body-con" :show="show">
    <Header></Header>
  <div style="height: 100%; width: 100%;">
    <div class="main-con" :aria-hidden="show ? 'true' : null" style=" height: 100%; justify-content: center; background-size: cover;
    align-items: center; background-color: #292b2c">
      <carousel :per-page="1" :mouse-drag="false" :autoplay="true" :autoplayHoverPause="true" :loop="true" :speed="1000" style="flex-shrink: 0;" v-bind:style="[smallScreen ? {'width': '100%'} : {'width': '75%'}]" @page-change="onPageChange" class="h-75">
        <slide>
          <div class="col my-2">
                <div class="card rounded-3 carousel_slide_back align-items-center" id="slide1_back" style="background-color: #40DAE3; height: 50vh;">
                    <img class="slide_image" src="../assets/static/images/alternative_campaign_game_mode_back2.png" height="256" width="256"/>
                    <div style="position: absolute; bottom: 0" class="align-items-center">
                      <h4 class="text-center">Campaign</h4>
                      <p class="text-center text-black mr-1 ml-1">Play different levels from easiest to hardest ones</p>
                    </div>

                    <button type="button" class="bg-transparent stretched-link"
                            style="border: none; color: transparent"></button>
                </div>
              </div>
        </slide>
        <slide>
          <div class="col my-2" @click="createRankedRoom">
                <div class="card rounded-3 carousel_slide_back align-items-center" id="slide2_back" style="background-color: #255918; height: 50vh;">
                  <img class="slide_image" src="../assets/static/images/alternative_rating_game_mode_back2.png" height="256" width="256"/>
                    <div style="position: absolute; bottom: 0" class="align-items-center">
                      <h4 class="text-center text-white">Rating room</h4>
                      <p class="text-center text-white mr-1 ml-1">Compete with other players and update your rating</p>
                    </div>
                    <button type="button" class="bg-transparent stretched-link"
                            style="border: none; color: transparent"></button>
                </div>
              </div>
        </slide>
        <slide>
           <div class="col my-2" onclick="location.href='#';">
                <div class="card rounded-3 carousel_slide_back align-items-center" id="slide3_back" style="background-color: #6b001a; height: 50vh;">
                  <img class="slide_image" src="../assets/static/images/alternative_private_game_mode_back2.png" height="256" width="256"/>
                    <div style="position: absolute; bottom: 0" class="align-items-center">
                      <h4 class="text-center" style="color: white">Private room</h4>
                      <p style="color: white" class="text-center mr-1 ml-1">Create a room and send an invitation link to friends</p>
                    </div>

                    <button type="button" class="bg-transparent stretched-link"
                            style="border: none; color: transparent">
                    </button>
                </div>
              </div>
        </slide>
        <slide>
          <div class="col my-2" onclick="location.href='#';">
                <div class="card rounded-3 carousel_slide_back align-items-center" id="slide4_back" style="background-color: #e1b107; height: 50vh;">
                  <img class="slide_image" src="../assets/static/images/alternative_public_game_mode_back2.png" height="256" width="256"/>
                    <div style="position: absolute; bottom: 0" class="align-items-center">
                      <h4 class="text-center">Open room</h4>
                      <p class="text-center mr-1 ml-1">Create an open room to meet new gamers and get experience</p>
                    </div>
                    <button type="button" class="bg-transparent stretched-link"
                            style="border: none; color: transparent">
                    </button>
                </div>
              </div>
        </slide>
        <slide>
          <div class="col my-2" onclick="location.href = '/endless';">
                <div class="card rounded-3 carousel_slide_back align-items-center" id="slide5_back" style="background-color: #000000; height: 50vh;">
                  <img class="slide_image" src="../assets/static/images/endless.png" height="256" width="256"/>
                    <div style="position: absolute; bottom: 0" class="align-items-center">
                      <h4 class="text-center text-white">Endless mode</h4>
                      <p class="text-center text-white mr-1 ml-1">Check how fast and smart you are?</p>
                    </div>
                    <button type="button" class="bg-transparent stretched-link"
                            style="border: none; color: transparent"></button>
                </div>
              </div>
        </slide>
      </carousel>

<!--      <div class="d-md-flex flex-md-column my-md-3 ps-md-3">
        <div class="me-md-3 pt-3 px-3  px-md-5 text-center overflow-hidden">
          <div class="p-3">
            <h2 class="display-5">Choose the mode</h2>
            <p class="lead">Play with friends and meet new people.</p>
          </div>
          <div class="ms-auto" v-show="smallScreen">

            <div class="row d-flex flex-lg-column text-center my-2">

              <div class="col my-2">
                <div class="card bg-light rounded-3">
                  <div class="card-body" style="height: 18rem">

                    <img src="../assets/static/images/levels.svg" alt="levels"
                         style="width: 5rem; animation: 1.11111s linear -1.11111s infinite normal forwards running breath-f235b970-61a7-4dc9-8bd5-98e617725c44;">
                    <h4 class="my-3 fw-normal">Campaign</h4>
                    <p>Play different levels from easiest to hardest ones</p>

                    <button type="button" class="bg-transparent stretched-link"
                            style="border: none; color: transparent"></button>
                  </div>
                </div>
              </div>

              <div class="col my-2" @click="createRankedRoom">
                <div class="card bg-light rounded-3">
                  <div class="card-body" style="height: 18rem">
                    <svg xmlns="http://www.w3.org/2000/svg" style="width: 5rem" fill="currentColor"
                         class="bi bi-graph-up" viewBox="0 0 16 16">
                      <path fill-rule="evenodd"
                            d="M0 0h1v15h15v1H0V0zm10 3.5a.5.5 0 0 1 .5-.5h4a.5.5 0 0 1 .5.5v4a.5.5 0 0 1-1 0V4.9l-3.613 4.417a.5.5 0 0 1-.74.037L7.06 6.767l-3.656 5.027a.5.5 0 0 1-.808-.588l4-5.5a.5.5 0 0 1 .758-.06l2.609 2.61L13.445 4H10.5a.5.5 0 0 1-.5-.5z"/>
                    </svg>
                    <h4 class="my-3 fw-normal">Rating room</h4>
                    <p>Compete with other players and update your rating</p>

                    <button type="button" class="bg-transparent stretched-link"
                            style="border: none; color: transparent"></button>
                  </div>
                </div>
              </div>

            </div>

            <div class="row d-flex flex-lg-column text-center my-2">

              <div class="col my-2" onclick="location.href='#';">
                <div class="card bg-light rounded-3">
                  <div class="card-body" style="height: 18rem">
                    <svg xmlns="http://www.w3.org/2000/svg" style="width: 5rem"
                         fill="currentColor"
                         class="bi bi-door-closed" viewBox="0 0 16 16">
                      <path
                          d="M3 2a1 1 0 0 1 1-1h8a1 1 0 0 1 1 1v13h1.5a.5.5 0 0 1 0 1h-13a.5.5 0 0 1 0-1H3V2zm1 13h8V2H4v13z"/>
                      <path d="M9 9a1 1 0 1 0 2 0 1 1 0 0 0-2 0z"/>
                    </svg>
                    <h4 class="my-3 fw-normal">Private room</h4>
                    <p>Create a room and send an invitation link to friends</p>

                    <button type="button" class="bg-transparent stretched-link"
                            style="border: none; color: transparent">
                    </button>
                  </div>
                </div>
              </div>

              <div class="col my-2" onclick="location.href='#';">
                <div class="card bg-light rounded-3">
                  <div class="card-body" style="height: 18rem">
                    <svg xmlns="http://www.w3.org/2000/svg" style="width: 5rem"
                         fill="currentColor"
                         class="bi bi-door-open-fill" viewBox="0 0 16 16">
                      <path
                          d="M1.5 15a.5.5 0 0 0 0 1h13a.5.5 0 0 0 0-1H13V2.5A1.5 1.5 0 0 0 11.5 1H11V.5a.5.5 0 0 0-.57-.495l-7 1A.5.5 0 0 0 3 1.5V15H1.5zM11 2h.5a.5.5 0 0 1 .5.5V15h-1V2zm-2.5 8c-.276 0-.5-.448-.5-1s.224-1 .5-1 .5.448.5 1-.224 1-.5 1z"/>
                    </svg>
                    <h4 class="my-3 fw-normal">Open room</h4>
                    <p>Create an open room to meet new gamers and get experience</p>

                    <button type="button" class="bg-transparent stretched-link"
                            style="border: none; color: transparent">
                    </button>
                  </div>
                </div>
              </div>

            </div>
          </div>

          <div class="ms-auto" v-show="!smallScreen">
            <div class="row text-center my-2">
              <div class="col my-2">
                <div class="card bg-light rounded-3">
                  <div class="card-body" style="height: 18rem">

                    <img src="../assets/static/images/levels.svg" alt="levels"
                         style="width: 5rem; animation: 1.11111s linear -1.11111s infinite normal forwards running breath-f235b970-61a7-4dc9-8bd5-98e617725c44;">
                    <h4 class="my-3 fw-normal">Campain</h4>
                    <p>Play different levels from easiest to hardest ones</p>

                    <button type="button" class="bg-transparent stretched-link"
                            style="border: none; color: transparent"></button>
                  </div>
                </div>
              </div>

              <div class="col my-2" @click="createRankedRoom">
                <div class="card bg-light rounded-3">
                  <div class="card-body" style="height: 18rem">
                    <svg xmlns="http://www.w3.org/2000/svg" style="width: 5rem" fill="currentColor"
                         class="bi bi-graph-up" viewBox="0 0 16 16">
                      <path fill-rule="evenodd"
                            d="M0 0h1v15h15v1H0V0zm10 3.5a.5.5 0 0 1 .5-.5h4a.5.5 0 0 1 .5.5v4a.5.5 0 0 1-1 0V4.9l-3.613 4.417a.5.5 0 0 1-.74.037L7.06 6.767l-3.656 5.027a.5.5 0 0 1-.808-.588l4-5.5a.5.5 0 0 1 .758-.06l2.609 2.61L13.445 4H10.5a.5.5 0 0 1-.5-.5z"/>
                    </svg>
                    <h4 class="my-3 fw-normal">Rating room</h4>
                    <p>Compete with other players and update your rating</p>

                    <button type="button" class="bg-transparent stretched-link"
                            style="border: none; color: transparent"></button>
                  </div>
                </div>
              </div>

              <div class="col my-2" onclick="location.href='#';">
                <div class="card bg-light rounded-3">
                  <div class="card-body" style="height: 18rem">
                    <svg xmlns="http://www.w3.org/2000/svg" style="width: 5rem"
                         fill="currentColor"
                         class="bi bi-door-closed" viewBox="0 0 16 16">
                      <path
                          d="M3 2a1 1 0 0 1 1-1h8a1 1 0 0 1 1 1v13h1.5a.5.5 0 0 1 0 1h-13a.5.5 0 0 1 0-1H3V2zm1 13h8V2H4v13z"/>
                      <path d="M9 9a1 1 0 1 0 2 0 1 1 0 0 0-2 0z"/>
                    </svg>
                    <h4 class="my-3 fw-normal">Private room</h4>
                    <p>Create a room and send an invitation link to friends</p>

                    <button type="button" class="bg-transparent stretched-link"
                            style="border: none; color: transparent">
                    </button>
                  </div>
                </div>
              </div>

              <div class="col my-2" onclick="location.href='#';">
                <div class="card bg-light rounded-3">
                  <div class="card-body" style="height: 18rem">
                    <svg xmlns="http://www.w3.org/2000/svg" style="width: 5rem"
                         fill="currentColor"
                         class="bi bi-door-open-fill" viewBox="0 0 16 16">
                      <path
                          d="M1.5 15a.5.5 0 0 0 0 1h13a.5.5 0 0 0 0-1H13V2.5A1.5 1.5 0 0 0 11.5 1H11V.5a.5.5 0 0 0-.57-.495l-7 1A.5.5 0 0 0 3 1.5V15H1.5zM11 2h.5a.5.5 0 0 1 .5.5V15h-1V2zm-2.5 8c-.276 0-.5-.448-.5-1s.224-1 .5-1 .5.448.5 1-.224 1-.5 1z"/>
                    </svg>
                    <h4 class="my-3 fw-normal">Open room</h4>
                    <p>Create an open room to meet new gamers and get experience</p>

                    <button type="button" class="bg-transparent stretched-link"
                            style="border: none; color: transparent">
                    </button>
                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>-->
    </div>
  </div>

  </b-overlay>


</template>

<script>
import Header from "./Header";
import axios from "axios";
// documentation https://github.com/SSENSE/vue-carousel
import { Carousel, Slide } from 'vue-carousel';

export default {
  name: "NewGame",
  components: {
    Header,
    Carousel,
    Slide
  },
  data() {
    return {
      show: false,
      smallScreen: window.innerWidth < 810,
      slide: 0,
      sliding: null,
      currentSlide: 0
    }
  },
  created() {
    window.addEventListener("resize", this.myEventHandler);
  },
  methods: {
    // Resize page listener
    // eslint-disable-next-line no-unused-vars
    myEventHandler(e) {
      this.smallScreen = window.innerWidth < 810;
    },
    // Here we create ranked room on the sever, if the user in the system, otherwise go to the login page
    createRankedRoom() {
      this.show = true
      axios.put("/api/ranked_room/join/")
          .then(response => {
            // console.log(response)
            // console.log(response.data.id)
            this.$cookies.set('lrid', response.data.id, "2min")
            this.$cookies.set("st", response.data.start_time, "2min")
            this.$cookies.set("et", response.data.end_time, "2min")

            this.$router.push({
              name: "waitingRoom",
              params: {
                room_id: response.data.id,
                start_time: response.data.start_time,
                end_time: response.data.end_time
              }
            })
          })
          .catch(error => {
            this.show = false
            if (error.response.status === 401) {
              this.$router.push("/signIn")
            }
            alert(error);
            console.log(error)
          })
    },
    onPageChange(pageNum) {
      this.currentSlide = pageNum
    }
  }
}
</script>

<style scoped>

.carousel_slide_back{
  background-size: cover;
  /*  width:100%;*/
  /*  height: 100%;*/
    /*background-image: url("./images/bg.jpg");*/
}

/*#slide1_back{
  background: url("../assets/static/images/alternative_campaign_game_mode_back.jpg") center center no-repeat #eee;
}

#slide2_back{
  background: url('../assets/static/images/alternative_rating_game_mode_back.jpg') no-repeat center #eee;
}

#slide3_back{
  background: url('../assets/static/images/alternative_private_game_mode_back.jpg') no-repeat center #eee;
}

#slide4_back{
  background: url('../assets/static/images/alternative_public_room_game_mode_back.jpg') no-repeat center #eee;
}*/

@media screen and (max-width: 450px) and (max-height: 720px){
  .slide_image{
    height: 200px;
    width: 200px;
  }
}
</style>