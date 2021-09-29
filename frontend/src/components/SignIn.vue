<template>
<!--  <div class="wrapper d-flex flex-column">
    <main class="form-signin">
        <form v-on:submit.prevent="submitForm">

            <svg class="mb-4" width="84" height="97" viewBox="0 0 84 97" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M39.5211 95.6902L3.61798 74.6835C2.75718 74.178 2.04247 73.4524 1.54536 72.5792C1.04825 71.706 0.786152 70.7159 0.785291 69.7078V27.7114C0.783212 26.7005 1.04391 25.7069 1.54117 24.8304C2.03843 23.954 2.75472 23.2257 3.61798 22.7187L39.5211 1.72904C40.3849 1.22377 41.3647 0.957764 42.3621 0.957764C43.3596 0.957764 44.3394 1.22377 45.2032 1.72904L81.0895 22.7357C81.9528 23.2427 82.6691 23.971 83.1663 24.8474C83.6636 25.7239 83.9243 26.7175 83.9222 27.7284V69.7078C83.9243 70.7187 83.6636 71.7124 83.1663 72.5888C82.6691 73.4653 81.9528 74.1936 81.0895 74.7005L45.2032 95.6902C44.3394 96.1955 43.3596 96.4615 42.3621 96.4615C41.3647 96.4615 40.3849 96.1955 39.5211 95.6902Z"
                      fill="white"/>
                <path d="M33.9814 70.0738C32.8046 70.0738 31.851 69.1059 31.851 67.9137V30.3623C31.851 29.1717 32.299 28.385 33.3161 27.7889L48.7459 18.753C49.7639 18.1569 50.6607 18.1569 51.6786 18.753L58.9932 23.0368C60.0103 23.633 60.4583 24.4196 60.4583 25.6102V67.9134C60.4583 69.1056 59.5039 70.0727 58.3271 70.0727C57.1503 70.0727 56.1959 69.1056 56.1959 67.9134V26.3864L50.2117 22.8816L36.1136 31.1385V67.9123C36.1136 69.1045 35.1591 70.0715 33.9824 70.0715L33.9814 70.0738ZM33.9822 79.5779C33.5811 79.5779 33.2058 79.4678 32.8848 79.2722L25.2016 74.7725C24.1844 74.1764 23.7365 73.3897 23.7365 72.1992V25.6127C23.7365 24.4222 24.1845 23.6355 25.2016 23.0394L32.8848 18.5396C33.2058 18.3441 33.5811 18.2314 33.9822 18.2314C35.159 18.2314 36.1134 19.1985 36.1134 20.3907C36.1134 21.2036 35.6697 21.9115 35.0145 22.2799L27.9982 26.3884V71.421L35.0145 75.5295C35.6697 75.8979 36.1134 76.6058 36.1134 77.4187C36.1134 78.6109 35.159 79.5779 33.9822 79.5779ZM42.0982 79.5804C40.9214 79.5804 39.9678 78.6125 39.9678 77.4202V54.127C39.9678 52.9364 40.4158 52.1497 41.4329 51.5536L49.1379 47.0353C49.4738 46.8388 49.8399 46.7457 50.2017 46.7457C50.938 46.7457 51.6543 47.1327 52.0488 47.8253C52.2427 48.1657 52.3346 48.5365 52.3346 48.9032L52.3447 72.6678C52.3447 73.86 51.3902 74.827 50.2134 74.827C49.0367 74.827 48.0822 73.86 48.0822 72.6678V52.6473L44.2293 54.9039V77.421C44.2293 78.6132 43.2748 79.5802 42.0981 79.5802L42.0982 79.5804ZM42.0982 46.312C40.9214 46.312 39.9678 45.3441 39.9678 44.1518V35.1159C39.9678 33.9253 40.4166 33.1395 41.4337 32.5425L49.1387 28.0242C49.4747 27.8277 49.8407 27.7346 50.2026 27.7346C50.9389 27.7346 51.6552 28.1216 52.0496 28.8142C52.2436 29.1546 52.3355 29.5255 52.3355 29.8921L52.3455 39.3996C52.3455 40.5919 51.3902 41.5589 50.2134 41.5589C49.0367 41.5589 48.0822 40.5919 48.0822 39.3996V33.6365L44.2293 35.8931V44.1525C44.2293 45.3448 43.2748 46.3118 42.0981 46.3118L42.0982 46.312Z"
                      fill="#111111"/>
            </svg>

            <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

            <div class="form-floating">
                <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com" v-model="email">
                <label for="floatingInput">Email address</label>
            </div>
            <div class="form-floating">
                <input type="password" class="form-control" id="floatingPassword" placeholder="Password" v-model="password">
                <label for="floatingPassword">Password</label>
            </div>
            <a href="#" class="mb-1 nav-link text-dark">
                <img src="../assets/static/images/google.svg" alt="Signin with Google">
                <span class="links" style="color: black">Sign in with Google</span>
            </a>

            <div class="checkbox mb-3">
                <label>
                    <input type="checkbox" value="remember-me"> Remember me
                </label>
            </div>
            <button class="w-100 btn btn-lg btn-dark" type="submit">Sign in</button>

        </form>
    </main>

</div>-->
  <div id="signInScreen" class="wrapper">
    <Header></Header>
    <div class="container con d-flex flex-column justify-content-center">
    <div class="card text-center bg-transparent border-0">
        <div class="card-body border-0">

            <svg class="mb-4" width="126" height="145" viewBox="0 0 84 97" fill="none"
                     xmlns="http://www.w3.org/2000/svg">
                    <path d="M39.5211 95.6902L3.61798 74.6835C2.75718 74.178 2.04247 73.4524 1.54536 72.5792C1.04825 71.706 0.786152 70.7159 0.785291 69.7078V27.7114C0.783212 26.7005 1.04391 25.7069 1.54117 24.8304C2.03843 23.954 2.75472 23.2257 3.61798 22.7187L39.5211 1.72904C40.3849 1.22377 41.3647 0.957764 42.3621 0.957764C43.3596 0.957764 44.3394 1.22377 45.2032 1.72904L81.0895 22.7357C81.9528 23.2427 82.6691 23.971 83.1663 24.8474C83.6636 25.7239 83.9243 26.7175 83.9222 27.7284V69.7078C83.9243 70.7187 83.6636 71.7124 83.1663 72.5888C82.6691 73.4653 81.9528 74.1936 81.0895 74.7005L45.2032 95.6902C44.3394 96.1955 43.3596 96.4615 42.3621 96.4615C41.3647 96.4615 40.3849 96.1955 39.5211 95.6902Z"
                          fill="white"/>
                    <path d="M33.9814 70.0738C32.8046 70.0738 31.851 69.1059 31.851 67.9137V30.3623C31.851 29.1717 32.299 28.385 33.3161 27.7889L48.7459 18.753C49.7639 18.1569 50.6607 18.1569 51.6786 18.753L58.9932 23.0368C60.0103 23.633 60.4583 24.4196 60.4583 25.6102V67.9134C60.4583 69.1056 59.5039 70.0727 58.3271 70.0727C57.1503 70.0727 56.1959 69.1056 56.1959 67.9134V26.3864L50.2117 22.8816L36.1136 31.1385V67.9123C36.1136 69.1045 35.1591 70.0715 33.9824 70.0715L33.9814 70.0738ZM33.9822 79.5779C33.5811 79.5779 33.2058 79.4678 32.8848 79.2722L25.2016 74.7725C24.1844 74.1764 23.7365 73.3897 23.7365 72.1992V25.6127C23.7365 24.4222 24.1845 23.6355 25.2016 23.0394L32.8848 18.5396C33.2058 18.3441 33.5811 18.2314 33.9822 18.2314C35.159 18.2314 36.1134 19.1985 36.1134 20.3907C36.1134 21.2036 35.6697 21.9115 35.0145 22.2799L27.9982 26.3884V71.421L35.0145 75.5295C35.6697 75.8979 36.1134 76.6058 36.1134 77.4187C36.1134 78.6109 35.159 79.5779 33.9822 79.5779ZM42.0982 79.5804C40.9214 79.5804 39.9678 78.6125 39.9678 77.4202V54.127C39.9678 52.9364 40.4158 52.1497 41.4329 51.5536L49.1379 47.0353C49.4738 46.8388 49.8399 46.7457 50.2017 46.7457C50.938 46.7457 51.6543 47.1327 52.0488 47.8253C52.2427 48.1657 52.3346 48.5365 52.3346 48.9032L52.3447 72.6678C52.3447 73.86 51.3902 74.827 50.2134 74.827C49.0367 74.827 48.0822 73.86 48.0822 72.6678V52.6473L44.2293 54.9039V77.421C44.2293 78.6132 43.2748 79.5802 42.0981 79.5802L42.0982 79.5804ZM42.0982 46.312C40.9214 46.312 39.9678 45.3441 39.9678 44.1518V35.1159C39.9678 33.9253 40.4166 33.1395 41.4337 32.5425L49.1387 28.0242C49.4747 27.8277 49.8407 27.7346 50.2026 27.7346C50.9389 27.7346 51.6552 28.1216 52.0496 28.8142C52.2436 29.1546 52.3355 29.5255 52.3355 29.8921L52.3455 39.3996C52.3455 40.5919 51.3902 41.5589 50.2134 41.5589C49.0367 41.5589 48.0822 40.5919 48.0822 39.3996V33.6365L44.2293 35.8931V44.1525C44.2293 45.3448 43.2748 46.3118 42.0981 46.3118L42.0982 46.312Z"
                          fill="#111111"/>
                </svg>

                <h1 class="mb-5 fw-normal">Please log in</h1>

            <form v-on:submit.prevent="submitForm">
                <div class="form-floating mb-2">
                    <input type="email" class="form-control" id="floatingInput" v-model="email" placeholder="name@example.com" required>
                    <label for="floatingInput">Email address</label>
                </div>
                <div class="form-floating mb-4">
                    <input type="password" class="form-control" id="floatingPassword" v-model="password" placeholder="Password" required>
                    <label for="floatingPassword">Password</label>
                </div>

                <button class="w-75 btn btn-lg btn-dark" type="submit">Login</button>

            </form>
        </div>
        <div class="card-footer bg-transparent border-0">
            <a href="">Forgot password</a>
        </div>
    </div>
</div>
  </div>
</template>

<script>
import axios from "axios";
import store from "../vuex/store";
import router from "../router/router";
import Header from "./Header";

export default {
  name: "SignIn",
  components: {Header},
  data() {
    return{
      email: "",
      password: ""
    }
  }, methods: {
    submitForm() {
      axios.defaults.headers.common["Authorization"] = ""
      localStorage.removeItem("access_token")

      const formData = {
        username: this.email,
        password: this.password
      }

      axios.post("/api/v1/jwt/create/", formData)
      .then(response => {
        console.log(response)

        const access = response.data.access
        const refresh = response.data.refresh

        store.commit('setAccess', access)
        store.commit('setRefresh', refresh)

        axios.defaults.headers.common["Authorization"] = "JWT " + access

        localStorage.setItem("access_token", access)
        localStorage.setItem("refresh_token", refresh)

        router.push("/")
      }).catch(error => {
        console.log(error)
      })
    }
  }, beforeCreate() {
    document.title = "Sign In"
  }
}
</script>

<style scoped>


</style>