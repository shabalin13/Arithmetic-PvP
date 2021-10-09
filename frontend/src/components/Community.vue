<template>
  <div class="body-con" id="communityScreen">
    <Header></Header>

    <div class="main-con">
      <div class="fw-light pt-4 pb-2 px-3">
        <div class="card text-black bg-light">
          <div class="card-body">
            <h5 class="card-title">About the game</h5>
            <p class="card-text">
              Arithmetic PvP is a verbal counting online game. Players compete in calculating various
              expressions,
              starting from primitive ones, such as 2+2, ending with extremely hard containing
              several-digit
              numbers. There is also a single-player mode, where you can run the endless mode and
              constantly
              improve your skill, or play campaign which has levels of increasing complexity.
            </p>
            <h6>Play our game if you want to:</h6>
            <ul>
              <li>Improve your arithmetic skills</li>
              <li>Find new friends with same interests</li>
              <li>Compete!</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="fw-light pt-4 pb-2 px-3">
        <div class="card text-black bg-light">
          <div class="card-body">
            <h5 class="card-title">Leaderboard</h5>
            <p class="card-text">
            </p>
            <h6>Our best players</h6>
            <ul>
              <li>troHaN - 100000000000000 points</li>
              <li>KamilAin - 9999999999999 points</li>
            </ul>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import Header from "./Header";

export default {
  name: "Community",
  components: {Header}
}
</script>

<style scoped>

</style>