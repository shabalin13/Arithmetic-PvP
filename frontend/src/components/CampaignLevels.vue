<template>

  <div class="wrapper flex-fill" style="background: #008cff">
    <div id="overlay">
    </div>
    <Header></Header>
    <div class="container">
<div class="main-timeline">

                        <!-- start experience section-->
                        <div v-for="(item, index) in levels" v-bind:key="index" class="timeline">
                            <div class="icon"></div>
                            <div class="date-content">
                                <div class="date-outer" v-b-hover="v => handleHover(v, index)" @click="runLevel(item)">
                                    <span class="date">
                                        <span class="month" v-bind:id="'spanLevelNum' + index" v-bind:style="[hovered === index ? {color: 'white'} : {}]">{{ index + 1 }}</span>
                                        <span class="year" v-bind:id="'spanLevelTitle' + index" v-bind:style="[hovered === index ? {color: 'white'} : {}]">Level</span>
                                    </span>
                                </div>
                            </div>
<!--                          <div class="timeline-content">
                                <h5 class="title text-white">Graphic Designer</h5>
                          </div>-->
<!--                            <div class="timeline-content">
                                <h5 class="title">Visual Art &amp; Design</h5>
                                <p class="description">
                                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed efficitur ex sit amet massa scelerisque scelerisque. Aliquam erat volutpat. Aenean interdum finibus efficitur. Praesent dapibus dolor felis, eu ultrices elit molestie.
                                </p>
                            </div>-->
                        </div>

                    </div>
</div>
  </div>
</template>

<script>
import Header from "./Header";
// import {levels} from "../assets/static/js/func"
import axios from "axios";

export default {
  name: "CampaignConstructor",
  components: {Header},
  data(){
    return{
      levels: [],
      hovered: -1,
      bgHiddenLevels: 'red',
      windowWidth: 0
    }
  },
  methods: {
    handleHover(hovered, value) {
      if (hovered){
          this.hovered = value
      }else{
        this.hovered = -1
      }
    },
    runLevel(level){
      this.$router.push({
          name: "campaignGame",
          params: {level: level}
        })
    },
    getLevelStats(){
      // this.turnOnLoading()
      axios.get('api/get_level_info/')
        .then(response => {
          // console.log(response)
          let input_arr = response.data
          console.log(input_arr)
          input_arr.sort((a,b) => (a.index > b.index) ? 1 : -1)
          this.levels = []
          for (let i = 0; i < input_arr.length; i++){
            if (input_arr[i].time === -1){
              if (i === 0){
                this.levels.push(input_arr[i])
                break
              }else{
                if (input_arr[i - 1].time !== -1){
                  this.levels.push(input_arr[i])
                  break
                }
              }
            }else{
              this.levels.push(input_arr[i])
            }
          }
          // this.levels = response.data
          this.turnOffLoading()
        })
        .catch(error => {
          console.log(error)
          this.turnOffLoading()
          if (error.response.status === 401)
            this.$router.push("/signIn")
          else
            alert("Server maintenance")
            this.$router.push("/newGame")
        })
    },
    turnOnLoading() {
      document.getElementById("overlay").style.display = "block";
    },
    turnOffLoading() {
      document.getElementById("overlay").style.display = "none";
    }
  },
  created() {
    this.getLevelStats()
    this.windowWidth = window.innerWidth
  },
  mounted() {
    this.turnOnLoading()
  }
}
</script>

<style scoped>

/*Design is taken from https://www.bootdey.com/snippets/view/bs4-my-experience-timeline*/

body{
    background-color: #f7f7f7;
    margin-top:20px;
}

.container{
  margin-top: 1px;
}

.main-timeline {
    position: relative;
    padding-bottom: 6px;
}

.main-timeline:before {
    content: "";
    display: block;
    width: 2px;
    height: 100%;
    background: #000000;
    margin: 0 auto;
    position: absolute;
    top: 0;
    left: 0;
    right: 0
}

.main-timeline .timeline {
    margin-bottom: 40px;
    position: relative
}

.main-timeline .timeline:after {
    content: "";
    display: block;
    clear: both
}

.main-timeline .icon {
    width: 18px;
    height: 18px;
    line-height: 18px;
    margin: auto;
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0
}

.main-timeline .icon:before,
.main-timeline .icon:after {
    content: "";
    width: 100%;
    height: 100%;
    border-radius: 50%;
    position: absolute;
    top: 0;
    left: 0;
}

.main-timeline .icon:before {
    /*should be change on hover*/
    background: #9c0a0a;
    border: 2px solid #232323;
}

.main-timeline .date-content {
    width: 50%;
    float: left;
    margin-top: 22px;
    position: relative;
}

.main-timeline .date-content:before {
    content: "";
    width: 35%;
    height: 2px;
    background: #000000;
    margin: auto 0;
    position: absolute;
    top: -21px;
    right: 10px;
    bottom: 0
}

.main-timeline .date-outer {
    width: 125px;
    height: 125px;
    font-size: 16px;
    text-align: center;
    margin: auto;
    z-index: 1;
}

.date-outer :hover{
  cursor: pointer;
}

.main-timeline .date-outer:before,
.main-timeline .date-outer:after {
    content: "";
    width: 125px;
    height: 125px;
    margin: 0 auto;
    border-radius: 50%;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
}

.date-outer:hover:after{
  background: black;
  position: absolute;
  top: -6px;
  border: 2px solid #ffffff;
}

.main-timeline .date-outer:before {
    background: rgba(73, 210, 157, 0.6);
    border: 2px solid #232323;
    position: absolute;
    top: -6px;
}

.main-timeline .date {
    width: 100%;
    margin: auto;
    position: absolute;
    top: 27%;
    left: 0;
    z-index: 3;
}

.main-timeline .month {
    font-size: 24px;
    font-weight: 700;
    z-index: 3;
}

.main-timeline .year {
    display: block;
    font-size: 18px;
    font-weight: 700;
    color: #232323;
    line-height: 36px
}

.main-timeline .timeline-content {
    width: 50%;
    padding: 20px 0 20px 50px;
    float: right
}

.main-timeline .title {
    font-size: 19px;
    font-weight: 700;
    line-height: 24px;
    margin: 0 0 15px 0;
}

.main-timeline .description {
    margin-bottom: 0
}

.main-timeline .timeline:nth-child(2n) .date-content {
    float: right
}

.main-timeline .timeline:nth-child(2n) .date-content:before {
    left: 10px
}

.main-timeline .timeline:nth-child(2n) .timeline-content {
    padding: 20px 50px 20px 0;
    text-align: right;
}

@media only screen and (max-width: 991px) {
    .main-timeline .date-content:before {
        width: 22.5%
    }
    .main-timeline .timeline-content {
        padding: 10px 0 10px 30px
    }
    .main-timeline .title {
        font-size: 17px;
    }
    .main-timeline .timeline:nth-child(2n) .timeline-content {
        padding: 10px 30px 10px 0
    }
}

@media only screen and (max-width: 767px) {

    .container{
      margin-top: 10px;
    }

    .main-timeline:before {
        margin: 0;
        left: 7px
    }
    .main-timeline .timeline {
        margin-bottom: 20px
    }
    .main-timeline .timeline:last-child {
        margin-bottom: 0
    }
    .main-timeline .icon {
        margin: auto 0
    }
    .main-timeline .date-content {
        width: 95%;
        float: right;
        margin-top: 0
    }
    .main-timeline .date-content:before {
        display: none
    }
    .main-timeline .date-outer {
        width: 110px;
        height: 110px
    }
    .main-timeline .date-outer:before,
    .main-timeline .date-outer:after {
        width: 110px;
        height: 110px
    }
    .main-timeline .date {
        top: 30%
    }
    .main-timeline .year {
        font-size: 14px
    }
    .main-timeline .timeline-content,
    .main-timeline .timeline:nth-child(2n) .timeline-content {
        width: 95%;
        text-align: center;
        padding: 10px 0
    }
    .main-timeline .title {
        margin-bottom: 10px
    }
}


#overlay {
  position: fixed; /* Sit on top of the page content */
  display: none; /* Hidden by default */
  width: 100%; /* Full width (cover the whole page) */
  height: 100%; /* Full height (cover the whole page) */
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0,0,0,0.5); /* Black background with opacity */
  z-index: 2; /* Specify a stack order in case you're using a different order for other elements */
  cursor: wait; /* Add a pointer on hover */
}

</style>