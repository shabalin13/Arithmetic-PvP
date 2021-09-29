import Vue from 'vue'
import App from './App.vue'
import router from './router/router';
import axios from "axios";
import store from "./vuex/store";
Vue.config.productionTip = false

axios.defaults.baseURL = "http://127.0.0.1:8000"

new Vue({
   router,
   store,
  render: h => h(App),

}).$mount('#app');
