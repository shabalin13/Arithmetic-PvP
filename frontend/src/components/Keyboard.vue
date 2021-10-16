<template>

  <div class="px-4 flex-column d-flex">
    <div class="mt-2" id="hide_show_keyboard">

        <button class="float-right" style="border-radius: 5px" @click="keyBoardIsShown = !keyBoardIsShown; $cookies.set('keyboardPreference', keyBoardIsShown ? 'show' : 'hide', '1y')"
        v-bind:style="[keyBoardIsShown ? {'background-color': 'white'}: {'background-color': 'black'}]">
          <svg v-bind:fill="[keyBoardIsShown ? '#000000': '#ffffff']" xmlns="http://www.w3.org/2000/svg" width="24" height="24" class="bi bi-keyboard" viewBox="0 0 16 16">
            <path d="M14 5a1 1 0 0 1 1 1v5a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h12zM2 4a2 2 0 0 0-2 2v5a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2H2z"/>
            <path d="M13 10.25a.25.25 0 0 1 .25-.25h.5a.25.25 0 0 1 .25.25v.5a.25.25 0 0 1-.25.25h-.5a.25.25 0 0 1-.25-.25v-.5zm0-2a.25.25 0 0 1 .25-.25h.5a.25.25 0 0 1 .25.25v.5a.25.25 0 0 1-.25.25h-.5a.25.25 0 0 1-.25-.25v-.5zm-5 0A.25.25 0 0 1 8.25 8h.5a.25.25 0 0 1 .25.25v.5a.25.25 0 0 1-.25.25h-.5A.25.25 0 0 1 8 8.75v-.5zm2 0a.25.25 0 0 1 .25-.25h1.5a.25.25 0 0 1 .25.25v.5a.25.25 0 0 1-.25.25h-1.5a.25.25 0 0 1-.25-.25v-.5zm1 2a.25.25 0 0 1 .25-.25h.5a.25.25 0 0 1 .25.25v.5a.25.25 0 0 1-.25.25h-.5a.25.25 0 0 1-.25-.25v-.5zm-5-2A.25.25 0 0 1 6.25 8h.5a.25.25 0 0 1 .25.25v.5a.25.25 0 0 1-.25.25h-.5A.25.25 0 0 1 6 8.75v-.5zm-2 0A.25.25 0 0 1 4.25 8h.5a.25.25 0 0 1 .25.25v.5a.25.25 0 0 1-.25.25h-.5A.25.25 0 0 1 4 8.75v-.5zm-2 0A.25.25 0 0 1 2.25 8h.5a.25.25 0 0 1 .25.25v.5a.25.25 0 0 1-.25.25h-.5A.25.25 0 0 1 2 8.75v-.5zm11-2a.25.25 0 0 1 .25-.25h.5a.25.25 0 0 1 .25.25v.5a.25.25 0 0 1-.25.25h-.5a.25.25 0 0 1-.25-.25v-.5zm-2 0a.25.25 0 0 1 .25-.25h.5a.25.25 0 0 1 .25.25v.5a.25.25 0 0 1-.25.25h-.5a.25.25 0 0 1-.25-.25v-.5zm-2 0A.25.25 0 0 1 9.25 6h.5a.25.25 0 0 1 .25.25v.5a.25.25 0 0 1-.25.25h-.5A.25.25 0 0 1 9 6.75v-.5zm-2 0A.25.25 0 0 1 7.25 6h.5a.25.25 0 0 1 .25.25v.5a.25.25 0 0 1-.25.25h-.5A.25.25 0 0 1 7 6.75v-.5zm-2 0A.25.25 0 0 1 5.25 6h.5a.25.25 0 0 1 .25.25v.5a.25.25 0 0 1-.25.25h-.5A.25.25 0 0 1 5 6.75v-.5zm-3 0A.25.25 0 0 1 2.25 6h1.5a.25.25 0 0 1 .25.25v.5a.25.25 0 0 1-.25.25h-1.5A.25.25 0 0 1 2 6.75v-.5zm0 4a.25.25 0 0 1 .25-.25h.5a.25.25 0 0 1 .25.25v.5a.25.25 0 0 1-.25.25h-.5a.25.25 0 0 1-.25-.25v-.5zm2 0a.25.25 0 0 1 .25-.25h5.5a.25.25 0 0 1 .25.25v.5a.25.25 0 0 1-.25.25h-5.5a.25.25 0 0 1-.25-.25v-.5z"/>
          </svg>
      </button>

      </div>

    <div class="keyboard d-flex flex-column flex-fill my-3" v-if="keyBoardIsShown">
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
</template>

<script>
export default {
  name: "Keyboard",
  data(){
    return{
      keyBoardIsShown: true,
      input_number: this.parentInput
    }
  },
  props:{
    parentInput: String
  },
  created() {
    document.addEventListener('keydown', (event) => { this.changeInput(event.key)});
    let kp = this.$cookies.get('keyboardPreference')
    if (kp != null){
      if (kp !== 'show'){
        this.keyBoardIsShown = false
      }
    }
  },
  methods: {
    changeInput(key){
      this.input_number = this.parentInput
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
        this.$emit("changeInput", this.input_number)
      }
    }
  }
}
</script>

<style scoped>

#hide_show_keyboard{
  display: block;
}

@media screen and (max-width: 801px){

  #hide_show_keyboard{
    display: none;
  }
}

</style>