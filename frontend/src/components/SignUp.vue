<template>

  <div class="body-con">
<!--    <Header></Header>

    <div class="main-con" :aria-hidden="showLoading ? 'true' : null">
      <b-alert
          v-model="showBottom"
          class="position-fixed fixed-bottom m-0 rounded-0 w-50"
          style="z-index: 2000;"
          variant="danger"
          dismissible>
        <b>{{ this.report_message }}</b>
      </b-alert>

      <div class="container con d-flex flex-column justify-content-center">

        <div class="card text-center bg-transparent border-0">
          <div class="card-body">

            <svg class="mb-4" width="84" height="97" viewBox="0 0 84 97" fill="none"
                 xmlns="http://www.w3.org/2000/svg">
              <path
                  d="M39.5211 95.6902L3.61798 74.6835C2.75718 74.178 2.04247 73.4524 1.54536 72.5792C1.04825 71.706 0.786152 70.7159 0.785291 69.7078V27.7114C0.783212 26.7005 1.04391 25.7069 1.54117 24.8304C2.03843 23.954 2.75472 23.2257 3.61798 22.7187L39.5211 1.72904C40.3849 1.22377 41.3647 0.957764 42.3621 0.957764C43.3596 0.957764 44.3394 1.22377 45.2032 1.72904L81.0895 22.7357C81.9528 23.2427 82.6691 23.971 83.1663 24.8474C83.6636 25.7239 83.9243 26.7175 83.9222 27.7284V69.7078C83.9243 70.7187 83.6636 71.7124 83.1663 72.5888C82.6691 73.4653 81.9528 74.1936 81.0895 74.7005L45.2032 95.6902C44.3394 96.1955 43.3596 96.4615 42.3621 96.4615C41.3647 96.4615 40.3849 96.1955 39.5211 95.6902Z"
                  fill="white"/>
              <path
                  d="M33.9814 70.0738C32.8046 70.0738 31.851 69.1059 31.851 67.9137V30.3623C31.851 29.1717 32.299 28.385 33.3161 27.7889L48.7459 18.753C49.7639 18.1569 50.6607 18.1569 51.6786 18.753L58.9932 23.0368C60.0103 23.633 60.4583 24.4196 60.4583 25.6102V67.9134C60.4583 69.1056 59.5039 70.0727 58.3271 70.0727C57.1503 70.0727 56.1959 69.1056 56.1959 67.9134V26.3864L50.2117 22.8816L36.1136 31.1385V67.9123C36.1136 69.1045 35.1591 70.0715 33.9824 70.0715L33.9814 70.0738ZM33.9822 79.5779C33.5811 79.5779 33.2058 79.4678 32.8848 79.2722L25.2016 74.7725C24.1844 74.1764 23.7365 73.3897 23.7365 72.1992V25.6127C23.7365 24.4222 24.1845 23.6355 25.2016 23.0394L32.8848 18.5396C33.2058 18.3441 33.5811 18.2314 33.9822 18.2314C35.159 18.2314 36.1134 19.1985 36.1134 20.3907C36.1134 21.2036 35.6697 21.9115 35.0145 22.2799L27.9982 26.3884V71.421L35.0145 75.5295C35.6697 75.8979 36.1134 76.6058 36.1134 77.4187C36.1134 78.6109 35.159 79.5779 33.9822 79.5779ZM42.0982 79.5804C40.9214 79.5804 39.9678 78.6125 39.9678 77.4202V54.127C39.9678 52.9364 40.4158 52.1497 41.4329 51.5536L49.1379 47.0353C49.4738 46.8388 49.8399 46.7457 50.2017 46.7457C50.938 46.7457 51.6543 47.1327 52.0488 47.8253C52.2427 48.1657 52.3346 48.5365 52.3346 48.9032L52.3447 72.6678C52.3447 73.86 51.3902 74.827 50.2134 74.827C49.0367 74.827 48.0822 73.86 48.0822 72.6678V52.6473L44.2293 54.9039V77.421C44.2293 78.6132 43.2748 79.5802 42.0981 79.5802L42.0982 79.5804ZM42.0982 46.312C40.9214 46.312 39.9678 45.3441 39.9678 44.1518V35.1159C39.9678 33.9253 40.4166 33.1395 41.4337 32.5425L49.1387 28.0242C49.4747 27.8277 49.8407 27.7346 50.2026 27.7346C50.9389 27.7346 51.6552 28.1216 52.0496 28.8142C52.2436 29.1546 52.3355 29.5255 52.3355 29.8921L52.3455 39.3996C52.3455 40.5919 51.3902 41.5589 50.2134 41.5589C49.0367 41.5589 48.0822 40.5919 48.0822 39.3996V33.6365L44.2293 35.8931V44.1525C44.2293 45.3448 43.2748 46.3118 42.0981 46.3118L42.0982 46.312Z"
                  fill="#111111"/>
            </svg>

            <h1 class="mb-4 fw-normal">Please register</h1>

            <form class="row gx-1" @submit.prevent="submitForm">

              <div class="form-floating col-6 mb-2">
                <input type="text" class="form-control" id="name" v-model="name" placeholder="name" required>
                <label for="name">Name</label>
              </div>
              <div class="form-floating col-6 mb-2">
                <input type="text" class="form-control" id="surname" v-model="surname" placeholder="surname" required>
                <label for="surname">Surname</label>
              </div>

              <div class="form-floating col-12 mb-2">
                <input type="text" class="form-control" id="nickname" v-model="nickname" placeholder="nickname"
                       required>
                <label for="nickname">Nickname</label>
              </div>

              <div class="form-floating mb-2">
                <input type="email" class="form-control" id="floatingInput" v-model="email" placeholder="email"
                       required>
                <label for="floatingInput">Email address</label>
              </div>
              <div class="form-floating col-6 mb-3">
                <input type="password" class="form-control" id="floatingPassword1" v-model="password"
                       placeholder="password1" required>
                <label for="floatingPassword1">Password</label>
              </div>
              <div class="form-floating col-6 mb-3">
                <input type="password" class="form-control" id="floatingPassword2" v-model="password2"
                       placeholder="password2" required>
                <label for="floatingPassword2">Repeat password</label>
              </div>

              <div class="form-check mb-4 col-12 text-start mx-1">
                <input class="form-check-input" type="checkbox" id="seePassword" @click="showPasswords">
                <label class="form-check-label" for="seePassword">Show password</label>
              </div>


              <div>
                <button class="w-100 btn btn-lg btn-dark" type="submit">Sign up</button>
              </div>

            </form>
          </div>
        </div>
      </div>
    </div>-->
<div id="overlay">
</div>

  <div class="main-con" style="background-color: black; width: 100%; height: 100%">
      <b-alert
          v-model="showBottom"
          class="position-fixed fixed-bottom m-0 rounded-0 w-50"
          style="z-index: 2000;"
          variant="danger"
          dismissible>
        <b> {{ report_message }} </b>
      </b-alert>
    <div class="card card0">
        <div class="d-flex flex-lg-row flex-column-reverse">
            <div class="card card2 align-items-center">
                <div class="my-auto mx-md-5 px-md-5 right">
                  <a href="/" class="d-flex align-items-center my-2 my-lg-0 me-lg-auto text-light text-decoration-none">
                    <svg width="150" height="160" viewBox="0 0 84 97" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M39.5211 95.6902L3.61798 74.6835C2.75718 74.178 2.04247 73.4524 1.54536 72.5792C1.04825 71.706 0.786152 70.7159 0.785291 69.7078V27.7114C0.783212 26.7005 1.04391 25.7069 1.54117 24.8304C2.03843 23.954 2.75472 23.2257 3.61798 22.7187L39.5211 1.72904C40.3849 1.22377 41.3647 0.957764 42.3621 0.957764C43.3596 0.957764 44.3394 1.22377 45.2032 1.72904L81.0895 22.7357C81.9528 23.2427 82.6691 23.971 83.1663 24.8474C83.6636 25.7239 83.9243 26.7175 83.9222 27.7284V69.7078C83.9243 70.7187 83.6636 71.7124 83.1663 72.5888C82.6691 73.4653 81.9528 74.1936 81.0895 74.7005L45.2032 95.6902C44.3394 96.1955 43.3596 96.4615 42.3621 96.4615C41.3647 96.4615 40.3849 96.1955 39.5211 95.6902Z"
                              fill="white"/>
                        <path d="M33.9814 70.0738C32.8046 70.0738 31.851 69.1059 31.851 67.9137V30.3623C31.851 29.1717 32.299 28.385 33.3161 27.7889L48.7459 18.753C49.7639 18.1569 50.6607 18.1569 51.6786 18.753L58.9932 23.0368C60.0103 23.633 60.4583 24.4196 60.4583 25.6102V67.9134C60.4583 69.1056 59.5039 70.0727 58.3271 70.0727C57.1503 70.0727 56.1959 69.1056 56.1959 67.9134V26.3864L50.2117 22.8816L36.1136 31.1385V67.9123C36.1136 69.1045 35.1591 70.0715 33.9824 70.0715L33.9814 70.0738ZM33.9822 79.5779C33.5811 79.5779 33.2058 79.4678 32.8848 79.2722L25.2016 74.7725C24.1844 74.1764 23.7365 73.3897 23.7365 72.1992V25.6127C23.7365 24.4222 24.1845 23.6355 25.2016 23.0394L32.8848 18.5396C33.2058 18.3441 33.5811 18.2314 33.9822 18.2314C35.159 18.2314 36.1134 19.1985 36.1134 20.3907C36.1134 21.2036 35.6697 21.9115 35.0145 22.2799L27.9982 26.3884V71.421L35.0145 75.5295C35.6697 75.8979 36.1134 76.6058 36.1134 77.4187C36.1134 78.6109 35.159 79.5779 33.9822 79.5779ZM42.0982 79.5804C40.9214 79.5804 39.9678 78.6125 39.9678 77.4202V54.127C39.9678 52.9364 40.4158 52.1497 41.4329 51.5536L49.1379 47.0353C49.4738 46.8388 49.8399 46.7457 50.2017 46.7457C50.938 46.7457 51.6543 47.1327 52.0488 47.8253C52.2427 48.1657 52.3346 48.5365 52.3346 48.9032L52.3447 72.6678C52.3447 73.86 51.3902 74.827 50.2134 74.827C49.0367 74.827 48.0822 73.86 48.0822 72.6678V52.6473L44.2293 54.9039V77.421C44.2293 78.6132 43.2748 79.5802 42.0981 79.5802L42.0982 79.5804ZM42.0982 46.312C40.9214 46.312 39.9678 45.3441 39.9678 44.1518V35.1159C39.9678 33.9253 40.4166 33.1395 41.4337 32.5425L49.1387 28.0242C49.4747 27.8277 49.8407 27.7346 50.2026 27.7346C50.9389 27.7346 51.6552 28.1216 52.0496 28.8142C52.2436 29.1546 52.3355 29.5255 52.3355 29.8921L52.3455 39.3996C52.3455 40.5919 51.3902 41.5589 50.2134 41.5589C49.0367 41.5589 48.0822 40.5919 48.0822 39.3996V33.6365L44.2293 35.8931V44.1525C44.2293 45.3448 43.2748 46.3118 42.0981 46.3118L42.0982 46.312Z"
                              fill="#111111"/>
                    </svg>
                  </a>
                </div>
            </div>
            <div class="card card1">
                <div class="row justify-content-center my-auto">
                    <div class="col-md-8 col-10 my-5">
                        <div class="row justify-content-center px-3 mb-3"></div>
                        <h3 class="mb-5 text-center heading">We are ArithmeticPvP</h3>
                        <h6 class="msg-info">Please login to your account</h6>
                      <form v-on:submit.prevent="submitForm">
                        <div class="form-group"> <label class="form-control-label text-muted">Name</label> <input type="text" class="form-control input-text" id="name" v-model="name" placeholder="Name" required> </div>
                        <div class="form-group"> <label class="form-control-label text-muted">Surname</label> <input type="text" class="form-control input-text" id="surname" v-model="surname" placeholder="Surname" required> </div>
                        <div class="form-group"> <label class="form-control-label text-muted">Nickname</label><input type="text" class="form-control input-text" id="nickname" v-model="nickname" placeholder="Nickname" required> </div>
                        <div class="form-group"> <label class="form-control-label text-muted">Email</label> <input type="text" id="email" name="email" placeholder="Email" class="form-control input-text" v-model="email" required> </div>
                        <div class="form-group"> <label class="form-control-label text-muted">Password</label> <input type="password" id="floatingPassword1" name="psw" placeholder="Password" class="form-control input-text" v-model="password" required> </div>
                        <div class="form-group"> <label class="form-control-label text-muted">Confirm Password</label> <i class="fa fa-user icon"></i> <input type="password" id="floatingPassword2" name="psw" placeholder="Confirm Password" class="form-control input-text" v-model="password2" required> </div>
                        <div class="form-group"> <label class="form-check-label">Show password</label> <input type="checkbox" id="seePassword" @click="showPasswords"> </div>
                        <div class="row justify-content-center my-3 px-3"> <button class="btn-block btn-color" type="submit">Sign Up</button> </div>
                      </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

  </div>


  <!--  <b-overlay :show="showLoading" class="d-flex flex-column h-100">
      <Header></Header>

      <div class="d-flex flex-column wrapper" :aria-hidden="showLoading ? 'true' : null">
        <b-alert
            v-model="showBottom"
            class="position-fixed fixed-bottom m-0 rounded-0 w-50"
            style="z-index: 2000;"
            variant="danger"
            dismissible>
          <b>{{ this.report_message }}</b>
        </b-alert>

        <div class="container con d-flex flex-column justify-content-center">

          <div class="card text-center bg-transparent border-0">
            <div class="card-body">

              <svg class="mb-4" width="84" height="97" viewBox="0 0 84 97" fill="none"
                   xmlns="http://www.w3.org/2000/svg">
                <path
                    d="M39.5211 95.6902L3.61798 74.6835C2.75718 74.178 2.04247 73.4524 1.54536 72.5792C1.04825 71.706 0.786152 70.7159 0.785291 69.7078V27.7114C0.783212 26.7005 1.04391 25.7069 1.54117 24.8304C2.03843 23.954 2.75472 23.2257 3.61798 22.7187L39.5211 1.72904C40.3849 1.22377 41.3647 0.957764 42.3621 0.957764C43.3596 0.957764 44.3394 1.22377 45.2032 1.72904L81.0895 22.7357C81.9528 23.2427 82.6691 23.971 83.1663 24.8474C83.6636 25.7239 83.9243 26.7175 83.9222 27.7284V69.7078C83.9243 70.7187 83.6636 71.7124 83.1663 72.5888C82.6691 73.4653 81.9528 74.1936 81.0895 74.7005L45.2032 95.6902C44.3394 96.1955 43.3596 96.4615 42.3621 96.4615C41.3647 96.4615 40.3849 96.1955 39.5211 95.6902Z"
                    fill="white"/>
                <path
                    d="M33.9814 70.0738C32.8046 70.0738 31.851 69.1059 31.851 67.9137V30.3623C31.851 29.1717 32.299 28.385 33.3161 27.7889L48.7459 18.753C49.7639 18.1569 50.6607 18.1569 51.6786 18.753L58.9932 23.0368C60.0103 23.633 60.4583 24.4196 60.4583 25.6102V67.9134C60.4583 69.1056 59.5039 70.0727 58.3271 70.0727C57.1503 70.0727 56.1959 69.1056 56.1959 67.9134V26.3864L50.2117 22.8816L36.1136 31.1385V67.9123C36.1136 69.1045 35.1591 70.0715 33.9824 70.0715L33.9814 70.0738ZM33.9822 79.5779C33.5811 79.5779 33.2058 79.4678 32.8848 79.2722L25.2016 74.7725C24.1844 74.1764 23.7365 73.3897 23.7365 72.1992V25.6127C23.7365 24.4222 24.1845 23.6355 25.2016 23.0394L32.8848 18.5396C33.2058 18.3441 33.5811 18.2314 33.9822 18.2314C35.159 18.2314 36.1134 19.1985 36.1134 20.3907C36.1134 21.2036 35.6697 21.9115 35.0145 22.2799L27.9982 26.3884V71.421L35.0145 75.5295C35.6697 75.8979 36.1134 76.6058 36.1134 77.4187C36.1134 78.6109 35.159 79.5779 33.9822 79.5779ZM42.0982 79.5804C40.9214 79.5804 39.9678 78.6125 39.9678 77.4202V54.127C39.9678 52.9364 40.4158 52.1497 41.4329 51.5536L49.1379 47.0353C49.4738 46.8388 49.8399 46.7457 50.2017 46.7457C50.938 46.7457 51.6543 47.1327 52.0488 47.8253C52.2427 48.1657 52.3346 48.5365 52.3346 48.9032L52.3447 72.6678C52.3447 73.86 51.3902 74.827 50.2134 74.827C49.0367 74.827 48.0822 73.86 48.0822 72.6678V52.6473L44.2293 54.9039V77.421C44.2293 78.6132 43.2748 79.5802 42.0981 79.5802L42.0982 79.5804ZM42.0982 46.312C40.9214 46.312 39.9678 45.3441 39.9678 44.1518V35.1159C39.9678 33.9253 40.4166 33.1395 41.4337 32.5425L49.1387 28.0242C49.4747 27.8277 49.8407 27.7346 50.2026 27.7346C50.9389 27.7346 51.6552 28.1216 52.0496 28.8142C52.2436 29.1546 52.3355 29.5255 52.3355 29.8921L52.3455 39.3996C52.3455 40.5919 51.3902 41.5589 50.2134 41.5589C49.0367 41.5589 48.0822 40.5919 48.0822 39.3996V33.6365L44.2293 35.8931V44.1525C44.2293 45.3448 43.2748 46.3118 42.0981 46.3118L42.0982 46.312Z"
                    fill="#111111"/>
              </svg>

              <h1 class="mb-4 fw-normal">Please register</h1>

              <form class="row gx-1" @submit.prevent="submitForm">

                <div class="form-floating col-6 mb-2">
                  <input type="text" class="form-control" id="name" v-model="name" placeholder="name" required>
                  <label for="name">Name</label>
                </div>
                <div class="form-floating col-6 mb-2">
                  <input type="text" class="form-control" id="surname" v-model="surname" placeholder="surname" required>
                  <label for="surname">Surname</label>
                </div>

                <div class="form-floating col-12 mb-2">
                  <input type="text" class="form-control" id="nickname" v-model="nickname" placeholder="nickname"
                         required>
                  <label for="nickname">Nickname</label>
                </div>

                <div class="form-floating mb-2">
                  <input type="email" class="form-control" id="floatingInput" v-model="email" placeholder="email"
                         required>
                  <label for="floatingInput">Email address</label>
                </div>
                <div class="form-floating col-6 mb-3">
                  <input type="password" class="form-control" id="floatingPassword1" v-model="password"
                         placeholder="password1" required>
                  <label for="floatingPassword1">Password</label>
                </div>
                <div class="form-floating col-6 mb-3">
                  <input type="password" class="form-control" id="floatingPassword2" v-model="password2"
                         placeholder="password2" required>
                  <label for="floatingPassword2">Repeat password</label>
                </div>

                <div class="form-check mb-4 col-12 text-start mx-1">
                  <input class="form-check-input" type="checkbox" id="seePassword" @click="showPasswords">
                  <label class="form-check-label" for="seePassword">Show password</label>
                </div>


                <div>
                  <button class="w-100 btn btn-lg btn-dark" type="submit">Sign up</button>
                </div>

              </form>
            </div>
          </div>
        </div>
      </div>
    </b-overlay>-->

</template>

<script>
import axios from "axios";
import Header from "./Header";

export default {
  name: "SignUp",
  // eslint-disable-next-line vue/no-unused-components
  components: {Header},
  data() {
    return {
      name: "",
      surname: "",
      nickname: "",
      email: "",
      password: "",
      password2: "",
      see: false,
      showBottom: false,
      report_message: "",
    }
  },
  // Register on the system (send activation message to the email)
  methods: {
    // Register on the system (send activation message to the email)
    submitForm() {
      this.showBottom = false
      if (this.password === this.password2) {
        this.turnOnLoading()
        const formData = {
          username: this.nickname,
          first_name: this.name,
          last_name: this.surname,
          email: this.email,
          password: this.password,
        }
        axios.post("/api/v1/users/", formData)
            .then(response => {
              this.turnOffLoading()
              console.log(response)
              this.$router.push("/signIn")
            })
            .catch(error => {
              this.turnOffLoading()
              // alert(error);
              console.log(error)
              this.report_message = error.response.data
              this.showBottomAlert()
            })
      } else {
        this.report_message = "Passwords doesn't match"
        this.showBottomAlert()
      }

    },
    // Show the hidden passwords
    showPasswords() {
      const passwordField1 = document.querySelector('#floatingPassword1')
      const passwordField2 = document.querySelector('#floatingPassword2')
      if (this.see) {
        passwordField1.setAttribute('type', 'password')
        passwordField2.setAttribute('type', 'password')
      } else {
        passwordField1.setAttribute('type', 'text')
        passwordField2.setAttribute('type', 'text')
      }
      this.see = !this.see
    },
    // Show the bottom alert in case of some error
    showBottomAlert() {
      this.showBottom = true
    },
    turnOnLoading() {
      document.getElementById("overlay").style.display = "block";
    },
    turnOffLoading() {
      document.getElementById("overlay").style.display = "none";
    }
  },
  beforeCreate() {
    document.title = "Sign Up"
  }
}
</script>

<style scoped>

body {
    color: #000;
    overflow-x: hidden;
    height: 100%;
    /*background-image: linear-gradient(to right, #D500F9, #FFD54F);*/
    background-repeat: no-repeat
}

.input-text,
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
    border: 1px solid black !important;
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
        margin-top: 100px !important;
        margin-bottom: 100px !important
    }
}

@media screen and (max-width: 768px) {
    .container {
        padding: 10px !important
    }

    .card2 {
        padding: 50px
    }

    .right {
        margin-top: 50px !important;
        margin-bottom: 50px !important
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