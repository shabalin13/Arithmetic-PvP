<template>
  <div  id="communityScreen" class="body-con" style="background-color: gray">
    <Header></Header>
    <!-- Footer -->
    <!--    <footer class="page-footer font-small indigo" style="position: absolute; bottom: -20vh; background: linear-gradient(to right, #565353, #292b2c); width: 100%">

      &lt;!&ndash; Footer Links &ndash;&gt;
      <div class="container">

    &lt;!&ndash; Grid row&ndash;&gt;
    <div class="row text-center d-flex justify-content-center pt-5 mb-3">

      &lt;!&ndash; Grid column &ndash;&gt;
      <div class="col-md-2 mb-3">
          <button class="bg-transparent border-0" @click="showInfo = 0">
            <span class="text-primary text-uppercase">About us</span>
          </button>
      </div>
      &lt;!&ndash; Grid column &ndash;&gt;

      &lt;!&ndash; Grid column &ndash;&gt;
      <div class="col-md-2 mb-3">
        <button class="bg-transparent border-0" @click="showInfo = 1">
            <span class="text-primary text-uppercase">Products</span>
        </button>

&lt;!&ndash;        <h6 class="text-uppercase font-weight-bold">
          <a href="#">Products</a>
        </h6>&ndash;&gt;
      </div>
      &lt;!&ndash; Grid column &ndash;&gt;

      &lt;!&ndash; Grid column &ndash;&gt;
      <div class="col-md-2 mb-3">
        <button class="bg-transparent border-0" @click="showInfo = 2">
            <span class="text-primary text-uppercase">Contact</span>
        </button>
&lt;!&ndash;        <h6 class="text-uppercase font-weight-bold">
          <a href="#">Contact</a>
        </h6>&ndash;&gt;
      </div>
      &lt;!&ndash; Grid column &ndash;&gt;

    </div>
    &lt;!&ndash; Grid row&ndash;&gt;
    <hr class="rgba-white-light" style="margin: 0 15%; color: white">

    &lt;!&ndash; Grid row&ndash;&gt;
    <div class="row d-flex text-center justify-content-center mb-md-0 mb-4">

      &lt;!&ndash; Grid column &ndash;&gt;
      <div class="col-md-8 col-12 mt-5">
&lt;!&ndash;        <p style="line-height: 1.7rem; color: white">We are arithmeticPvP team)</p>&ndash;&gt;

&lt;!&ndash;        <div>
          <p class="text-white">We are on Google Play</p>
          <a href="https://play.google.com/">
            <img src="../assets/static/images/google-play-badge.png" style="width: 175px; height: 75px; position: relative; top: 50%" />
          </a>
        </div>&ndash;&gt;

        <transition name="fade">
          <div v-if="showInfo === 2">
            <p class="text-white">Contact us if you have any problems or suggestions: <a href="https://mail.google.com/mail/u/0/#inbox?compose=CllgCKCDCHXLBmSSzSBNjVMHBptZvwnxDZJxQZxttdcGPgggcTSCKtssJCHRqCkjwmzsJdzWVtg">arithmetic.pvp.main@gmail.com</a></p>
            <p class="text-white">Support us on:</p>
            <p style="color: blue">WebMoney:</p>
            <p style="color: darkorange">Kiwi:</p>
            <p style="color: deepskyblue">PayPal:</p>
          </div>
        </transition>
        <transition name="fade">
          <div v-if="showInfo === 1">
              <p class="text-white">We are on Google Play</p>
               <a href="https://play.google.com/">
                <img src="../assets/static/images/google-play-badge.png" style="width: 175px; height: 75px; position: relative; top: 50%" />
              </a>
          </div>
        </transition>
        <transition name="fade">
          <div v-if="showInfo === 0">
              <p style="line-height: 1.7rem; color: white">We are arithmeticPvP team)</p>
          </div>
        </transition>
      </div>
      &lt;!&ndash; Grid column &ndash;&gt;

    </div>
    &lt;!&ndash; Grid row&ndash;&gt;
    <hr class="clearfix d-md-none rgba-white-light" style="margin: 10% 15% 5%;">

    &lt;!&ndash; Grid row&ndash;&gt;
    <div class="row pb-3">

      &lt;!&ndash; Grid column &ndash;&gt;
      <div class="col-md-12">

        <div class="mb-5 flex-center">

          &lt;!&ndash; Facebook &ndash;&gt;
          <a class="fb-ic">
            <i class="fab fa-facebook-f fa-lg white-text mr-4"> </i>
          </a>
          &lt;!&ndash; Twitter &ndash;&gt;
          <a class="tw-ic">
            <i class="fab fa-twitter fa-lg white-text mr-4"> </i>
          </a>
          &lt;!&ndash; Google +&ndash;&gt;
          <a class="gplus-ic">
            <i class="fab fa-google-plus-g fa-lg white-text mr-4"> </i>
          </a>
          &lt;!&ndash;Linkedin &ndash;&gt;
          <a class="li-ic">
            <i class="fab fa-linkedin-in fa-lg white-text mr-4"> </i>
          </a>
          &lt;!&ndash;Instagram&ndash;&gt;
          <a class="ins-ic">
            <i class="fab fa-instagram fa-lg white-text mr-4"> </i>
          </a>
          &lt;!&ndash;Pinterest&ndash;&gt;
          <a class="pin-ic">
            <i class="fab fa-pinterest fa-lg white-text"> </i>
          </a>

        </div>

      </div>
      &lt;!&ndash; Grid column &ndash;&gt;

    </div>
    &lt;!&ndash; Grid row&ndash;&gt;

  </div>
      &lt;!&ndash; Footer Links &ndash;&gt;

      &lt;!&ndash; Copyright &ndash;&gt;
      <div class="footer-copyright text-center py-3">© 2021 Copyright:
        <a href="/"> ArithmeticPvP.com</a>
      </div>
      &lt;!&ndash; Copyright &ndash;&gt;

    </footer>-->
    <!-- Footer -->

    <div class="main-con" style="background-color: black; width: 100%; height: 100%">
    <div class="card card0 flex-column h-100">
        <div id="support_div" class="d-flex flex-lg-row flex-column h-100">
            <div class="card card2 align-items-center">
                <div class="my-auto mx-md-5 px-md-5 right">
                  <div class="flex-column">
                    <div class="mb-4">
                      <button class="bg-transparent border-0" @click="current_page=0">
<!--                        style="text-shadow: #FC0 1px 0 10px;"-->
                        <h1 class="text-white" v-bind:style="[current_page === 0 ? {'text-shadow': '#FC0 1px 0 10px'}: {}]"> About</h1>
                    </button>
                    </div>
                    <div class="mb-4">
                      <button class="bg-transparent border-0" @click="current_page=1">
                        <h1 class="text-white" v-bind:style="[current_page === 1 ? {'text-shadow': '#FC0 1px 0 10px'}: {}]"> Products</h1>
                    </button>
                    </div>
                    <div class="mb-4">
                      <button class="bg-transparent border-0" @click="current_page=2">
                        <h1 class="text-white" v-bind:style="[current_page === 2 ? {'text-shadow': '#FC0 1px 0 10px'}: {}]"> Contacts</h1>
                    </button>
                    </div>
                    <div class="mb-4">
                      <button class="bg-transparent border-0" @click="current_page=3">
                        <h1 class="text-white" v-bind:style="[current_page === 3 ? {'text-shadow': '#FC0 1px 0 10px'}: {}]"> Donations</h1>
                    </button>
                    </div>
                  </div>
                </div>
            </div>
            <div class="card card1">
                <div class="row justify-content-center my-auto">
                  <div class="col-md-10 col-10 my-5">
<!--                    <div class="row justify-content-center px-3 mb-3"></div>-->
                    <transition name="fade_community">
                      <div v-if="current_page === 2">
                        <h2 class="text-center">Contact us if you have any problems or suggestions: <a href="https://mail.google.com/mail/u/0/#inbox?compose=CllgCKCDCHXLBmSSzSBNjVMHBptZvwnxDZJxQZxttdcGPgggcTSCKtssJCHRqCkjwmzsJdzWVtg">arithmetic.pvp.main@gmail.com</a></h2>
<!--                        <h2 class="">Support us on:</h2>
                        <h3 style="color: blue">WebMoney:</h3>
                        <h3 style="color: darkorange">Kiwi:</h3>
                        <h3 style="color: deepskyblue">PayPal:</h3>-->
                      </div>
                    </transition>
                  <transition name="fade_community">
                    <div v-if="current_page === 1" class="mb-5 text-center heading">
                      <p class="text-white">We are on Google Play</p>
                      <a href="https://play.google.com/">
                        <img src="../assets/static/images/google-play-badge.png" style="height: 65%; width: 65%" />
                      </a>
                    </div>
                  </transition>
                  <transition name="fade_community" class="mb-5 text-center heading">
                    <div v-if="current_page === 0">
                      <h1 style="line-height: 1.7rem;" class="mb-5">We are arithmeticPvP team)</h1>
                      <p class="card-text">
                        Arithmetic PvP is a verbal counting online game. Players compete in calculating various
                        expressions,
                        starting from primitive ones, such as 2+2, ending with extremely hard containing
                        several-digit
                        numbers. There is also a single-player mode, where you can run the endless mode and
                        constantly
                        improve your skill, or play campaign which has levels of increasing complexity.
                      </p>
                      <h6>Play our game if you want to:</h6>
                      <ul>
                        <li>Improve your arithmetic skills</li>
                        <li>Find new friends with same interests</li>
                        <li>Compete!</li>
                      </ul>
                    </div>
                  </transition>
                  </div>


                </div>
                <div class="bottom text-center mb-5" >

                </div>
            </div>
        </div>
    </div>
</div>
    <!--    <div class="main-con">
      <div class="fw-light pt-4 pb-2 px-3">
        <div class="card text-black bg-light">
          <div class="card-body">
            <h5 class="card-title">About the game</h5>
            <p class="card-text">
              Arithmetic PvP is a verbal counting online game. Players compete in calculating various
              expressions,
              starting from primitive ones, such as 2+2, ending with extremely hard containing
              several-digit
              numbers. There is also a single-player mode, where you can run the endless mode and
              constantly
              improve your skill, or play campaign which has levels of increasing complexity.
            </p>
            <h6>Play our game if you want to:</h6>
            <ul>
              <li>Improve your arithmetic skills</li>
              <li>Find new friends with same interests</li>
              <li>Compete!</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="fw-light pt-4 pb-2 px-3">
        <div class="card text-black bg-light">
          <div class="card-body">
            <h5 class="card-title">Leaderboard</h5>
            <p class="card-text">
            </p>
            <h6>Our best players</h6>
            <ul>
              <li>troHaN - 100000000000000 points</li>
              <li>KamilAin - 9999999999999 points</li>
            </ul>
          </div>
        </div>
      </div>
    </div>-->

  </div>
</template>

<script>
import Header from "./Header";

export default {
  name: "Community",
  components: {Header},
  data(){
    return{
      showInfo: -1,
      current_page: 0
    }
  },
  mounted() {
    this.showInfo = 0
    this.current_page = 0
  }
}
</script>

<style scoped>

#rock{
  width: 150px;
  height: 150px;
  background: url("../assets/static/images/google-play-badge.png") no-repeat;
}

.btn-image {
    background-image: url('https://brandflow.net/assets/img/featured/mdb-prolog.jpg') !important;
    background-size: contain;
}


body {
    color: #000;
    overflow-x: hidden;
    height: 100%;
    /*background-image: linear-gradient(to right, #D500F9, #FFD54F);*/
    background-repeat: no-repeat
}

input,
textarea {
    background-color: #e7d6d6;
    border-radius: 50px !important;
    padding: 12px 15px 12px 15px !important;
    width: 100%;
    box-sizing: border-box;
    border: none !important;
    border: 1px solid #F3E5F5 !important;
    font-size: 16px !important;
    color: #000 !important;
    font-weight: 400
}

input:focus,
textarea:focus {
    -moz-box-shadow: none !important;
    -webkit-box-shadow: none !important;
    box-shadow: none !important;
    border: 1px solid #D500F9 !important;
    outline-width: 0;
    font-weight: 400
}

button:focus {
    -moz-box-shadow: none !important;
    -webkit-box-shadow: none !important;
    box-shadow: none !important;
    outline-width: 0
}

.card {
    border-radius: 0;
    border: none
}

.card1 {
    width: 50%;
    padding: 40px 30px 10px 30px
}

.card2 {
    width: 50%;
    /*background-image: linear-gradient(to right, #FFD54F, #D500F9)*/
  background-image: linear-gradient(to right, #292b2c, #000000);
}

#logo {
    width: 70px;
    height: 60px
}

.heading {
    margin-bottom: 60px !important
}

::placeholder {
    color: #000 !important;
    opacity: 1
}

:-ms-input-placeholder {
    color: #000 !important
}

::-ms-input-placeholder {
    color: #000 !important
}

.form-control-label {
    font-size: 12px;
    margin-left: 15px
}

.msg-info {
    padding-left: 15px;
    margin-bottom: 30px
}

.btn-color {
    border-radius: 50px;
    color: #fff;
    background-image: linear-gradient(to right, #292b2c, #000000);
    padding: 15px;
    cursor: pointer;
    border: none !important;
    margin-top: 40px
}

.btn-color:hover {
    color: #fff;
    background-image: linear-gradient(to right, #292b2c, #292b2c);
}

.btn-white {
    border-radius: 50px;
    color: black;
    background-color: #fff;
    padding: 8px 40px;
    cursor: pointer;
    border: 2px solid black !important
}

.btn-white:hover {
    color: #fff;
    background-image: linear-gradient(to right, #292b2c, #292b2c)
}

a {
    color: #000
}

a:hover {
    color: #000
}

.bottom {
    width: 100%;
    margin-top: 50px !important
}

.sm-text {
    font-size: 15px
}

@media screen and (max-width: 992px) {
    .card1 {
        width: 100%;
        padding: 40px 30px 10px 30px
    }

    .card2 {
        width: 100%
    }

    .right {
        margin-top: 50px !important;
        margin-bottom: 50px !important
    }

    .card0, #support_div{
      height: 50%;
    }
}

@media screen and (max-width: 768px) {

    .card2 {
        padding: 50px
    }

}

</style>