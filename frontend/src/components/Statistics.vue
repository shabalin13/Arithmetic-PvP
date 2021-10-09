<template>

  <div class="body-con">
    <Header></Header>

    <div class="main-con wrapper">

      <div class="pt-3 px-2 d-flex flex-column flex-fill">

        <div class="1-place py-3">

          <div class="card bg-transparent border-0 d-flex align-items-center text-break text-center">
            <h1 class="fw-light fst-italic border-bottom border-2 border-dark">1st place <i class="bi bi-award"></i></h1>
            <h2 class="">DIMbI4</h2>
          </div>

        </div>

        <div class="d-flex flex-row justify-content-around py-3">

          <div class="card bg-transparent px-2 border-0 d-flex align-items-center text-break text-center">
            <h2 class="fw-light fst-italic border-bottom border-2 border-dark">2nd place</h2>
            <h3 class="">troHaN</h3>
          </div>

          <div class="card bg-transparent border-0 d-flex align-items-center text-break text-center">
            <h2 class="fw-light fst-italic border-bottom border-2 border-dark">3rd place</h2>
            <h3 class="">KamilAin</h3>
          </div>

        </div>

      </div>

      <div class="p-2 flex-fill">
        <div class="overflow-auto text-center">
          <table class="table table-hover table-light">
            <thead class="table-success sticky-top">
            <tr>
              <th class="border-0" scope="col">#</th>
              <th class="border-0" scope="col">Nickname</th>
              <th class="border-0" scope="col">Avg speed(eq/s)</th>
              <th class="border-0" scope="col">Total accuracy</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <th scope="row">1</th>
                <td>DIMbI4</td>
                <td>1</td>
                <td>86%</td>
            </tr>
            <tr>
                <th scope="row">2</th>
                <td>troHaN</td>
                <td>2</td>
                <td>87%</td>
            </tr>
            <tr>
                <th scope="row">3</th>
                <td>KamilAin</td>
                <td>1</td>
                <td>67%</td>
            </tr>
            <tr>
                <th scope="row">4</th>
                <td>gfx73</td>
                <td>2.4</td>
                <td>56%</td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>

    </div>

  </div>

</template>

<script>
import Header from "./Header";

export default {
  name: "Statistics",
  components: {Header}
}
</script>

<style scoped>

</style>