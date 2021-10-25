<template>
    <div class="progress" style="width: 100%; height: 10px" >
            <div class="progress-bar progress-bar-striped" role="progressbar"
                 aria-valuemin="0" aria-valuemax="100" style="background-color: red"
                 v-bind:style="{'width': progress * (100 / numberOfQuestions)+ '%',
                  'background-color': bckColor}"></div>
      <img src="../assets/static/images/darth_vader.svg" alt="skin" v-bind:id="'skin_' + user_id"
      style="position: absolute; margin-top: -10px; margin-left: -16px; transition-duration: 0.68s" height="32" width="32"
      v-bind:style="skin === '' ? {'display':'none'} : {}"/>
  </div>

<!--    <button @click="increase(20)" class="mt-3">Click</button>-->
</template>

<script>
export default {
  name: "CustomProgressBar",
  props: {
    numberOfQuestions: Number,
    parentProgress: Number,
    bckColor: String,
    skin: String,
    user_id: String
  },
  data() {
    return {
      progress: 0,
      skin_element: null
    }
  },
  created() {
    this.progress = this.parentProgress
  },
  mounted() {
    this.skin_element = document.getElementById("skin_" + this.user_id)
    this.progress = this.parentProgress
  },
  methods: {
    increase() {
      if (this.skin_element !== null)
        this.skin_element.style.left = (this.parentProgress * (100 / this.numberOfQuestions)) + "%"
      this.progress = this.parentProgress
    }
  }
}
</script>

<style scoped>


.animate {
  transform: translateX(10vh);
  /*transition-duration: 0.5s;*/
}
</style>