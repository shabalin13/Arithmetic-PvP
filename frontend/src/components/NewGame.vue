<template>
    <b-overlay :show="show" class="d-flex flex-column h-100" fixed>
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
    </b-overlay>
</template>

<script>
    import Header from "./Header";
    import axios from "axios";

    export default {
        name: "NewGame",
        components: {Header},
        data() {
            return {
                show: false,
                smallScreen: window.innerWidth < 810
            }
        },
        created() {
            window.addEventListener("resize", this.myEventHandler);
        },
        methods: {
          // eslint-disable-next-line no-unused-vars
            myEventHandler(e) {
                // console.log(e)
                this.smallScreen = window.innerWidth < 810;
            },
            createRankedRoom() {
                this.show = true
                axios.put("/api/ranked_room/join/")
                    .then(response => {
                        console.log(response)
                        console.log(response.data.id)
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
            }
        }
    }
</script>

<style scoped>

</style>