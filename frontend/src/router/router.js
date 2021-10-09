import Vue from "vue";
import Router from "vue-router"
import MainScreen from "../components/MainScreen"
import LobbyScreen from "../components/LobbyScreen";
import SignIn from "../components/SignIn";
import SignUp from "../components/SignUp";
import WaitingRoom from "../components/WaitingRoom";
import NewGame from "../components/NewGame";
import Community from "../components/Community";
import Game from "@/components/Game";
import Activation from "../components/Activation";
import Statistics from "../components/Statistics";
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
    }, {
        name: "waitingRoom",
        path: "/waiting",
        component: WaitingRoom,
        props: {
            room_id: Number
        }
    }, {
        name: "newGame",
        path: "/newGame",
        component: NewGame
    }, {
        name: "community",
        path: "/community",
        component: Community
    }, {
        name: "game",
        path: "/game",
        component: Game
    }, {
        name: "statistics",
        path: "/statistics",
        component: Statistics
    }, {
        name: "activation",
        path: "/activate/:userId/:token",
        component: Activation,
        props: true
    }
    ],
    mode: 'history'
});
export default router;