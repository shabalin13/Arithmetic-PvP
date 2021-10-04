<template>
  <div class="wrapper d-flex flex-column justify-content-between">
    <Header></Header>

    <div class="progress_bars px-4 my-3">

      <div class="row d-flex flex-row align-items-center justify-content-center">
        <div class="col-3">
          <div class="me-2"><span class="fw-light">DIMbI4</span></div>
        </div>
        <div class="col-9">
          <div class="progress flex-fill">
            <div class="progress-bar progress-bar-striped" role="progressbar" style="width: 10%" aria-valuenow="10"
                 aria-valuemin="0" aria-valuemax="100"></div>
          </div>
        </div>
      </div>

      <div class="row d-flex flex-row align-items-center justify-content-center">
        <div class="col-3">
          <div class="text-truncate"><span class="fw-light">troHaN</span></div>
        </div>
        <div class="col-9">
          <div class="progress flex-fill">
            <div class="progress-bar progress-bar-striped bg-success" role="progressbar" style="width: 25%"
                 aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
          </div>
        </div>
      </div>

      <div class="row d-flex flex-row align-items-center justify-content-center">
        <div class="col-3">
          <div class="text-truncate"><span class="fw-light">KamilAin</span></div>
        </div>
        <div class="col-9">
          <div class="progress flex-fill">
            <div class="progress-bar progress-bar-striped bg-info" role="progressbar" style="width: 50%"
                 aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
          </div>
        </div>
      </div>

      <div class="row d-flex flex-row align-items-center justify-content-center">
        <div class="col-3">
          <div class="text-truncate"><span class="fw-light ">qwertyasdfawbvaerberb</span></div>
        </div>
        <div class="col-9">
          <div class="progress flex-fill">
            <div class="progress-bar progress-bar-striped bg-danger" role="progressbar" style="width: 100%"
                 aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
          </div>
        </div>
      </div>




      <!--<div class="d-flex flex-row align-items-center">
        <div class="me-2"><span class="fw-light">DIMbI4</span></div>
        <div class="progress flex-fill">
          <div class="progress-bar progress-bar-striped" role="progressbar" style="width: 10%" aria-valuenow="10"
               aria-valuemin="0" aria-valuemax="100"></div>
        </div>
      </div>

      <div class="d-flex flex-row align-items-center">
        <div class="me-2"><span class="fw-light">troHaN</span></div>
        <div class="progress flex-fill">
          <div class="progress-bar progress-bar-striped bg-success" role="progressbar" style="width: 25%"
               aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
      </div>

      <div class="d-flex flex-row align-items-center">
        <div class="me-2"><span class="fw-light">aerilvbaerwivbewqrivbceivbcqe</span></div>
        <div class="progress flex-fill">
          <div class="progress-bar progress-bar-striped bg-info" role="progressbar" style="width: 50%"
               aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
      </div>

      <div class="d-flex flex-row align-items-center">
        <div class="me-2"><span class="fw-light">troHaN</span></div>
        <div class="progress flex-fill">
          <div class="progress-bar progress-bar-striped bg-danger" role="progressbar" style="width: 100%"
               aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
      </div>-->


    </div>

    <div class="equation_canvas px-4 mb-3 d-flex flex-grow-1">
      <div class="card bg-light text-dark flex-grow-1 center" id="eq">
          <h1 style="text-align: center; vertical-align: middle; line-height: 90px;">{{ current_task }} {{ input_number }}</h1>
      </div>
    </div>

    <div class="keyboard d-flex flex-column px-4 mb-3">
      <div class="row my-1">
        <div class="d-grid col-4 mx-auto">
          <button type="button" class="btn btn-outline-dark" @click="changeInput('7')"><span>7</span></button>
        </div>
        <div class=" d-grid col-4 mx-auto">
          <button type="button" class="btn btn-outline-dark" @click="changeInput('8')"><span>8</span></button>
        </div>
        <div class=" d-grid col-4 mx-auto">
          <button type="button" class="btn btn-outline-dark" @click="changeInput('9')"><span>9</span></button>
        </div>
      </div>

      <div class="row my-1">
        <div class="d-grid col-4 mx-auto">
          <button type="button" class="btn btn-outline-dark" @click="changeInput('4')"><span>4</span></button>
        </div>
        <div class="d-grid col-4 mx-auto">
          <button type="button" class="btn btn-outline-dark" @click="changeInput('5')"><span>5</span></button>
        </div>
        <div class="d-grid col-4 mx-auto">
          <button type="button" class="btn btn-outline-dark" @click="changeInput('6')"><span>6</span></button>
        </div>
      </div>

      <div class="row my-1">
        <div class="d-grid col-4 mx-auto">
          <button type="button" class="btn btn-outline-dark" @click="changeInput('1')"><span>1</span></button>
        </div>
        <div class="d-grid col-4 mx-auto">
          <button type="button" class="btn btn-outline-dark" @click="changeInput('2')"><span>2</span></button>
        </div>
        <div class="d-grid col-4 mx-auto">
          <button type="button" class="btn btn-outline-dark" @click="changeInput('3')"><span>3</span></button>
        </div>
      </div>

      <div class="row my-1">
        <div class="d-grid col-4 mx-auto">
          <button type="button" class="btn btn-outline-dark" @click="changeInput('-')"><span>-</span></button>
        </div>
        <div class="d-grid col-4 mx-auto">
          <button type="button" class="btn btn-outline-dark" @click="changeInput('0')"><span>0</span></button>
        </div>
        <div class="d-grid col-4 mx-auto">
          <button type="button" class="btn btn-outline-dark" @click="changeInput('Backspace')"><span>Del</span></button>
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
      current_task: "",
      input_number: "",
      current_index: 0,
    }
  },
  created() {
    document.addEventListener('keydown', (event) => { this.changeInput(event.key)});
    this.room_id = this.$router.currentRoute.params.room_id
    console.log("RoomId " + this.room_id.toString())
    this.end_time = this.$router.currentRoute.params.end_time
    console.log("End Time " + this.end_time)
    let myDate = new Date(this.end_time);
    let result = myDate.getTime();
    let timeLeft = (result - Date.now());
    console.log("Time left: " + timeLeft.toString())
    setTimeout(this.gameIsOver, timeLeft)
    if (this.room_id !== undefined && this.end_time !== undefined){
      this.getQuestion()
    }
  },
  methods: {
    getQuestion(){
      if (this.current_index < QUESTIONS - 1){
        axios.get("/api/ranked_room/get_task/" + this.room_id.toString() + "/")
          .then(response =>{
            console.log(response)
            this.current_task = response.data.content + " = "
            this.current_index = response.data.index
          })
          .catch(error =>{
            if (error.response.status === 401){
              this.$router.push("/signIn")
            }
            alert(error);
            console.log(error)
          })
      }else{
        alert("Game for you is over pidoras!")
      }
    },
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
        this.submitAnswer()
      }
    },
    submitAnswer(){
      let num = parseInt(this.input_number)
      if (!isNaN(num)){
         axios.put("/api/ranked_room/submit_task/" + this.room_id.toString() + "/"  + this.input_number +  "/")
            .then(response =>{
              let correct = response.data.is_correct
              if (correct){
                 this.getQuestion()
                 this.input_number= ""
              }
            })
            .catch(error =>{
              if (error.response.status === 401){
                this.$router.push("/signIn")
              }
              alert(error);
              console.log(error)
            })
      }
    },
    gameIsOver(){
      alert("Game is over")
      this.$router.push("/")
    }

  }
}
</script>

<style scoped>

</style>