<template>
  <div class="wrapper d-flex flex-column justify-content-between">
    <Header></Header>

    <div class="progress_bars px-4 my-3">

      <div class="row d-flex flex-row align-items-center justify-content-center">
        <div class="col-3">
          <div class="me-2"><span class="fw-light">DIMbI4</span></div>
        </div>
        <div class="col-9">
          <div class="progress flex-fill">
            <div class="progress-bar progress-bar-striped" role="progressbar" style="width: 10%" aria-valuenow="10"
                 aria-valuemin="0" aria-valuemax="100"></div>
          </div>
        </div>
      </div>

      <div class="row d-flex flex-row align-items-center justify-content-center">
        <div class="col-3">
          <div class="text-truncate"><span class="fw-light">troHaN</span></div>
        </div>
        <div class="col-9">
          <div class="progress flex-fill">
            <div class="progress-bar progress-bar-striped bg-success" role="progressbar" style="width: 25%"
                 aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
          </div>
        </div>
      </div>

      <div class="row d-flex flex-row align-items-center justify-content-center">
        <div class="col-3">
          <div class="text-truncate"><span class="fw-light">KamilAin</span></div>
        </div>
        <div class="col-9">
          <div class="progress flex-fill">
            <div class="progress-bar progress-bar-striped bg-info" role="progressbar" style="width: 50%"
                 aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
          </div>
        </div>
      </div>

      <div class="row d-flex flex-row align-items-center justify-content-center">
        <div class="col-3">
          <div class="text-truncate"><span class="fw-light ">qwertyasdfawbvaerberb</span></div>
        </div>
        <div class="col-9">
          <div class="progress flex-fill">
            <div class="progress-bar progress-bar-striped bg-danger" role="progressbar" style="width: 100%"
                 aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
          </div>
        </div>
      </div>




      <!--<div class="d-flex flex-row align-items-center">
        <div class="me-2"><span class="fw-light">DIMbI4</span></div>
        <div class="progress flex-fill">
          <div class="progress-bar progress-bar-striped" role="progressbar" style="width: 10%" aria-valuenow="10"
               aria-valuemin="0" aria-valuemax="100"></div>
        </div>
      </div>

      <div class="d-flex flex-row align-items-center">
        <div class="me-2"><span class="fw-light">troHaN</span></div>
        <div class="progress flex-fill">
          <div class="progress-bar progress-bar-striped bg-success" role="progressbar" style="width: 25%"
               aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
      </div>

      <div class="d-flex flex-row align-items-center">
        <div class="me-2"><span class="fw-light">aerilvbaerwivbewqrivbceivbcqe</span></div>
        <div class="progress flex-fill">
          <div class="progress-bar progress-bar-striped bg-info" role="progressbar" style="width: 50%"
               aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
      </div>

      <div class="d-flex flex-row align-items-center">
        <div class="me-2"><span class="fw-light">troHaN</span></div>
        <div class="progress flex-fill">
          <div class="progress-bar progress-bar-striped bg-danger" role="progressbar" style="width: 100%"
               aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
      </div>-->


    </div>

    <div class="equation_canvas px-4 mb-3 d-flex flex-grow-1">
      <div class="card bg-light text-dark flex-grow-1" id="eq">

      </div>
    </div>

    <div class="keyboard d-flex flex-column px-4 mb-3">
      <div class="row my-1">
        <div class="d-grid col-4 mx-auto">
          <button type="button" class="btn btn-outline-dark"><span>7</span></button>
        </div>
        <div class=" d-grid col-4 mx-auto">
          <button type="button" class="btn btn-outline-dark"><span>8</span></button>
        </div>
        <div class=" d-grid col-4 mx-auto">
          <button type="button" class="btn btn-outline-dark"><span>9</span></button>
        </div>
      </div>

      <div class="row my-1">
        <div class="d-grid col-4 mx-auto">
          <button type="button" class="btn btn-outline-dark"><span>4</span></button>
        </div>
        <div class="d-grid col-4 mx-auto">
          <button type="button" class="btn btn-outline-dark"><span>5</span></button>
        </div>
        <div class="d-grid col-4 mx-auto">
          <button type="button" class="btn btn-outline-dark"><span>6</span></button>
        </div>
      </div>

      <div class="row my-1">
        <div class="d-grid col-4 mx-auto">
          <button type="button" class="btn btn-outline-dark"><span>1</span></button>
        </div>
        <div class="d-grid col-4 mx-auto">
          <button type="button" class="btn btn-outline-dark"><span>2</span></button>
        </div>
        <div class="d-grid col-4 mx-auto">
          <button type="button" class="btn btn-outline-dark"><span>3</span></button>
        </div>
      </div>

      <div class="row my-1">
        <div class="d-grid col-4 mx-auto">
          <button type="button" class="btn btn-outline-dark"><span>-</span></button>
        </div>
        <div class="d-grid col-4 mx-auto">
          <button type="button" class="btn btn-outline-dark"><span>0</span></button>
        </div>
        <div class="d-grid col-4 mx-auto">
          <button type="button" class="btn btn-outline-dark"><span>Del</span></button>
        </div>
      </div>

    </div>

  </div>
</template>

<script>
import Header from "@/components/Header";

export default {
  name: "Game",
  components: {Header}
}
</script>

<style scoped>

</style>