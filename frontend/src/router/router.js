import Vue from "vue";
import Router from "vue-router"
import MainScreen from "../components/MainScreen"
import LobbyScreen from "../components/LobbyScreen";
import SignIn from "../components/SignIn";
import SignUp from "../components/SignUp";
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
    },{
        name: "signIn",
        path: "/signIn",
        component: SignIn
    },{
        name: "signUp",
        path: "/signUp",
        component: SignUp
    }
    ],
    mode: 'history'
});
export default router;