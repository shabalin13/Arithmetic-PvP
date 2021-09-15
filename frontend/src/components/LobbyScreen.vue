<template>
  <div>
    <Header></Header>
  </div>
</template>

<script>
import Header from "./Header"

export default {
  name: "LobbyScreen",
  components: {
    Header
  },
  beforeCreate() {
   this.createRoom()
  },
  methods: {
    checkNewPeople(){
      console.log("Check new people");
      // after getting array of the people
      this.updateTable([]);

    },
    updateTable(people_array){
      console.log(people_array);
    },
    startGame(){
      // set room to no-waiting mode
      console.log("Game started");
    },
    createRoom(){
      // create room entry on the server
      console.log("Room created");
      // after getting the response
      setInterval(this.checkNewPeople, 1000);
    }
  },
}
</script>

<style scoped>

</style>