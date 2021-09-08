import Vue from "vue";
import Router from "vue-router"
import MainScreen from "../components/MainScreen"
import LobbyScreen from "../components/LobbyScreen";
Vue.use(Router)


let router = new Router({
    routes: [{
        name: "home",
        path: "/",
        component: MainScreen,
    },{
        name: "lobby",
        path: "/lobby",
        component: LobbyScreen
    }
    ],
    mode: 'history'
});
export default router;