//import api from "./axios-base"
//import axios from "axios";
import Vue from "vue";
import Vuex from "vuex"

Vue.use(Vuex)

let store = new Vuex.Store({
    state: {
        'access_token': '',
        'refresh_token': ''
    }, mutations: {
        initializeStore(state){
            if (localStorage.getItem("access_token")){
                state.access_token = localStorage.getItem("access_token")
                state.refresh_token = localStorage.getItem("refresh_token")
            }else{
                state.access_token = ''
                state.refresh_token = ''
            }
        },
        setAccess(state, access){
            state.access_token = access
        },
        setRefresh(state, refresh){
            state.refresh_token = refresh
        }
    }, actions: {

    }, modules: {

    }

})

export default store


