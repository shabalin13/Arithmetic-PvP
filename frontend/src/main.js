import Vue from 'vue'
import App from './App.vue'
import router from './router/router';
import axios from "axios";
import store from "./vuex/store";
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

Vue.config.productionTip = false

axios.defaults.baseURL = "http://127.0.0.1:8000"
// axios.defaults.baseURL = "http://192.168.8.105:8000"

Vue.use(BootstrapVue)

Vue.use(IconsPlugin)

new Vue({
   router,
   store,
  render: h => h(App),

}).$mount('#app');
