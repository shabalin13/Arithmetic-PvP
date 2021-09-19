import Vue from 'vue'
import App from './App.vue'
import router from './router/router';
import axios from "axios";
// import { createApp } from "vue"
Vue.config.productionTip = false

axios.defaults.baseURL = "http://127.0.0.1:8000"

// createApp(App).use(router, axios).$mount("#app")
new Vue({
  render: h => h(App),
    router,

}).$mount('#app');
