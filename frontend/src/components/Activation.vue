<template>

    <div class="body-con wrapper">
       <b-overlay :show="showLoading" class="d-flex flex-column h-100">
         <div class="d-flex flex-column main-con" :aria-hidden="showLoading ? 'true' : null">
        <div class="m-5 p-5 text-center">
            <h1 class="my-5">Congrats, you have successfully activated your account via Email!</h1>
            <button class="btn btn-lg btn-dark center" type="submit" onclick="window.location.href='/'">Go to Main Page</button>
        </div>
          <b-alert
      v-model="showBottom"
      class="position-fixed fixed-bottom m-0 rounded-0 w-50"
      style="z-index: 2000;"
      variant="danger"
      dismissible>
      <b>{{ this.report_message }}</b>
    </b-alert>
         </div>
    </b-overlay>
    </div>
</template>

<script>
     import axios from "axios";

     export default {
        name: "Activation",
        data() {
          return{
            showBottom: false,
            report_message: "",
            showLoading: false
          }
        },
        created() {
          this.activate()
        },
        methods: {
          activate(){
            axios.get('activate/' + this.userId + "/" + this.token + "")
            .then(response => {
              console.log(response)
              this.showLoading = false
            })
            .catch(error => {
              this.showLoading = false
              this.report_message = error.response.data
              this.showBottom = true
              setTimeout(function (){
                this.$router.push("/")
              }, 3000)
            })
          }
        },
        props: ['userId', 'token']
     }
</script>

<style scoped>

</style>