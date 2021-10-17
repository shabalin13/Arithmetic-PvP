<template>

  <div class="body-con">
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
    <div class="card card0 flex-fill">
        <div class="d-flex flex-lg-row flex-column flex-fill">

            <authorization-left-side></authorization-left-side>

            <div class="card card1">
                <div class="row justify-content-center my-auto">
                    <div class="col-md-8 col-10 my-5">
                        <div class="row justify-content-center px-3 mb-3"></div>
                          <div class="align-items-center row mb-5">
                              <svg id="logo_hidden" class="text-center" width="84" height="96" viewBox="0 0 84 96" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M38.7358 94.7325L2.8327 73.7258C1.9719 73.2203 1.2572 72.4946 0.760083 71.6214C0.262969 70.7482 0.000873571 69.7581 1.2333e-05 68.7501V26.7537C-0.00206627 25.7428 0.258635 24.7491 0.755895 23.8727C1.25315 22.9962 1.96944 22.2679 2.8327 21.761L38.7358 0.771276C39.5996 0.266004 40.5794 0 41.5768 0C42.5743 0 43.5541 0.266004 44.4179 0.771276L80.3042 21.778C81.1675 22.2849 81.8838 23.0132 82.381 23.8897C82.8783 24.7661 83.139 25.7597 83.1369 26.7707V68.7501C83.139 69.761 82.8783 70.7546 82.381 71.6311C81.8838 72.5075 81.1675 73.2358 80.3042 73.7428L44.4179 94.7325C43.5541 95.2377 42.5743 95.5037 41.5768 95.5037C40.5794 95.5037 39.5996 95.2377 38.7358 94.7325Z" fill="#111111"/>
                                <path d="M33.9814 69.0738C32.8046 69.0738 31.851 68.106 31.851 66.9137V29.3623C31.851 28.1718 32.299 27.3851 33.3161 26.789L48.7459 17.7531C49.7639 17.157 50.6607 17.157 51.6786 17.7531L58.9932 22.0369C60.0103 22.633 60.4583 23.4197 60.4583 24.6102V66.9134C60.4583 68.1057 59.5039 69.0727 58.3271 69.0727C57.1503 69.0727 56.1959 68.1057 56.1959 66.9134V25.3864L50.2117 21.8817L36.1136 30.1385V66.9123C36.1136 68.1046 35.1591 69.0716 33.9824 69.0716L33.9814 69.0738ZM33.9822 78.578C33.5811 78.578 33.2058 78.4679 32.8848 78.2723L25.2016 73.7726C24.1844 73.1764 23.7365 72.3898 23.7365 71.1992V24.6128C23.7365 23.4222 24.1845 22.6356 25.2016 22.0394L32.8848 17.5397C33.2058 17.3441 33.5811 17.2315 33.9822 17.2315C35.159 17.2315 36.1134 18.1985 36.1134 19.3908C36.1134 20.2036 35.6697 20.9116 35.0145 21.2799L27.9982 25.3884V70.4211L35.0145 74.5296C35.6697 74.8979 36.1134 75.6058 36.1134 76.4187C36.1134 77.611 35.159 78.578 33.9822 78.578ZM42.0981 78.5805C40.9214 78.5805 39.9678 77.6125 39.9678 76.4202V53.127C39.9678 51.9365 40.4158 51.1498 41.4329 50.5537L49.1379 46.0353C49.4738 45.8388 49.8399 45.7457 50.2017 45.7457C50.938 45.7457 51.6543 46.1327 52.0488 46.8254C52.2427 47.1657 52.3346 47.5366 52.3346 47.9032L52.3447 71.6678C52.3447 72.8601 51.3902 73.8271 50.2134 73.8271C49.0367 73.8271 48.0822 72.8601 48.0822 71.6678V51.6474L44.2293 53.904V76.421C44.2293 77.6133 43.2748 78.5803 42.0981 78.5803L42.0981 78.5805ZM42.0981 45.3121C40.9214 45.3121 39.9678 44.3441 39.9678 43.1518V34.1159C39.9678 32.9254 40.4166 32.1396 41.4337 31.5426L49.1387 27.0242C49.4747 26.8278 49.8407 26.7347 50.2026 26.7347C50.9389 26.7347 51.6551 27.1217 52.0496 27.8143C52.2436 28.1547 52.3355 28.5255 52.3355 28.8921L52.3455 38.3997C52.3455 39.5919 51.3902 40.5589 50.2134 40.5589C49.0367 40.5589 48.0822 39.5919 48.0822 38.3997V32.6366L44.2293 34.8932V43.1526C44.2293 44.3448 43.2748 45.3119 42.0981 45.3119L42.0981 45.3121Z" fill="white"/>
                              </svg>
                          </div>
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

</template>

<script>
import axios from "axios";
import Header from "./Header";
import AuthorizationLeftSide from "./UI/AuthorizationLeftSide";

export default {
  name: "SignUp",
  // eslint-disable-next-line vue/no-unused-components
  components: {AuthorizationLeftSide, Header},
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
              if (error.response.status === 400)
                if (error.response.data.non_field_errors !== undefined){
                  this.report_message = error.response.data.non_field_errors
                }else if (error.response.data.username !== undefined){
                  this.report_message = error.response.data.username
                }else{
                 this.report_message = error.response.data
                }
              else
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
    background-color: #dedede;
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

#logo_hidden{
  display: none;
}


@media screen and (max-width: 992px) {
    .card1 {
        width: 100%;
        padding: 40px 30px 10px 30px
    }

    .card2 {
        /*width: 100%*/
      display: none;
    }

    .right {
        margin-top: 100px !important;
        margin-bottom: 100px !important
    }

    #logo_hidden{
      display: block;
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