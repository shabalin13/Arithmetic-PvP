<template>
<!--   Modal: modalPoll-->
<!--<div class="modal fade right" id="modalPoll-1" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
  aria-hidden="true" data-backdrop="false">
  <div class="modal-dialog modal-full-height modal-right modal-notify modal-info" role="document">
    <div class="modal-content">
      &lt;!&ndash;Header&ndash;&gt;
      <div class="modal-header">
        <p class="heading lead">Feedback request
        </p>

        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true" class="white-text">×</span>
        </button>
      </div>

      &lt;!&ndash;Body&ndash;&gt;
      <div class="modal-body">
        <div class="text-center">
          <i class="far fa-file-alt fa-4x mb-3 animated rotateIn"></i>
          <p>
            <strong>Your opinion matters</strong>
          </p>
          <p>Have some ideas how to improve our product?
            <strong>Give us your feedback.</strong>
          </p>
        </div>

        <hr>

        &lt;!&ndash; Radio &ndash;&gt;
        <p class="text-center">
          <strong>Your rating</strong>
        </p>
        <div class="form-check mb-4">
          <input class="form-check-input" name="group1" type="radio" id="radio-179" value="option1" checked>
          <label class="form-check-label" for="radio-179">Very good</label>
        </div>

        <div class="form-check mb-4">
          <input class="form-check-input" name="group1" type="radio" id="radio-279" value="option2">
          <label class="form-check-label" for="radio-279">Good</label>
        </div>

        <div class="form-check mb-4">
          <input class="form-check-input" name="group1" type="radio" id="radio-379" value="option3">
          <label class="form-check-label" for="radio-379">Mediocre</label>
        </div>
        <div class="form-check mb-4">
          <input class="form-check-input" name="group1" type="radio" id="radio-479" value="option4">
          <label class="form-check-label" for="radio-479">Bad</label>
        </div>
        <div class="form-check mb-4">
          <input class="form-check-input" name="group1" type="radio" id="radio-579" value="option5">
          <label class="form-check-label" for="radio-579">Very bad</label>
        </div>
        &lt;!&ndash; Radio &ndash;&gt;

        <p class="text-center">
          <strong>What could we improve?</strong>
        </p>
        &lt;!&ndash;Basic textarea&ndash;&gt;
        <div class="md-form">
          <textarea type="text" id="form79textarea" class="md-textarea form-control" rows="3"></textarea>
          <label for="form79textarea">Your message</label>
        </div>

      </div>

      &lt;!&ndash;Footer&ndash;&gt;
      <div class="modal-footer justify-content-center">
        <a type="button" class="btn btn-primary waves-effect waves-light">Send
          <i class="fa fa-paper-plane ml-1"></i>
        </a>
        <a type="button" class="btn btn-outline-primary waves-effect" data-dismiss="modal">Cancel</a>
      </div>
    </div>
  </div>
</div>-->
<!-- Modal: modalPoll-->

  <div class="modal-mask">
        <div class="modal-wrapper">
          <div class="modal-dialog" role="document">
            <div class="modal-content">
              <div class="modal-header">
                <div class="modal-header">
                  <h5 class="modal-title">Customize your level</h5>
                </div>
              </div>
                <div class="modal-body">



        <!-- Radio -->
                <p class="text-center">
                  <strong>Difficulty</strong>
                </p>
<!--                <div class="form-check mb-4">
                  <input class="form-check-input" name="group1" type="radio" id="radio-1" value="easy" checked v-model="difficulty">
                  <label class="form-check-label" for="radio-1">Easy</label>
                </div>

                <div class="form-check mb-4">
                  <input class="form-check-input" name="group1" type="radio" id="radio-2" value="norm" v-model="difficulty">
                  <label class="form-check-label" for="radio-2">Medium</label>
                </div>

                <div class="form-check mb-4">
                  <input class="form-check-input" name="group1" type="radio" id="radio-3" value="hard" v-model="difficulty">
                  <label class="form-check-label" for="radio-3">Hard</label>
                </div>
                <div class="form-check mb-4">
                  <input class="form-check-input" name="group1" type="radio" id="radio-4" value="pain" v-model="difficulty">
                  <label class="form-check-label" for="radio-4">Hard with pain</label>
                </div>-->
                  <div class="text-center">
                    <b-dropdown id="dropdown-1" v-bind:text="difficultyFullName" class="m-md-2 w-25">
                      <b-dropdown-item @click="difficulty='easy'; difficultyFullName='Easy'">Easy</b-dropdown-item>
                      <b-dropdown-item @click="difficulty='norm'; difficultyFullName='Medium'">Medium</b-dropdown-item>
                      <b-dropdown-item @click="difficulty='hard'; difficultyFullName='Hard'">Hard</b-dropdown-item>
                      <b-dropdown-item @click="difficulty='pain'; difficultyFullName='Hard with pain'">Hard with pain</b-dropdown-item>
                    </b-dropdown>
                  </div>

        <!-- Radio -->

                  <!-- Radio -->
                <p class="text-center">
                  <strong>Seconds Per Question</strong>
                </p>
<!--                <div class="form-check mb-4">
                  <input class="form-check-input" name="group2" type="radio" id="radio-5" value="6" checked v-model="timePerQuestion">
                  <label class="form-check-label" for="radio-5">6s</label>
                </div>

                <div class="form-check mb-4">
                  <input class="form-check-input" name="group2" type="radio" id="radio-6" value="8" v-model="timePerQuestion">
                  <label class="form-check-label" for="radio-6">8s</label>
                </div>

                <div class="form-check mb-4">
                  <input class="form-check-input" name="group2" type="radio" id="radio-7" value="10" v-model="timePerQuestion">
                  <label class="form-check-label" for="radio-7">10s</label>
                </div>
                <div class="form-check mb-4">
                  <input class="form-check-input" name="group2" type="radio" id="radio-8" value="12" v-model="timePerQuestion">
                  <label class="form-check-label" for="radio-8">12s</label>
                </div>-->

                  <div class="text-center">
                    <b-dropdown id="dropdown-2" v-bind:text="timePerQuestion + 's'" class="m-md-2 w-25">
                      <b-dropdown-item @click="timePerQuestion='6'">6</b-dropdown-item>
                      <b-dropdown-item @click="timePerQuestion='8'">8</b-dropdown-item>
                      <b-dropdown-item @click="timePerQuestion='10'">10</b-dropdown-item>
                      <b-dropdown-item @click="timePerQuestion='12'">12</b-dropdown-item>
                    </b-dropdown>
                  </div>

        <!-- Radio -->

              </div>
              <div class="modal-footer">
<!--                <button type="button" class="btn btn-secondary" @click="showModal = false">Close</button>-->
                <button type="button" class="btn btn-primary" @click="submitModal">Start</button>
              </div>
            </div>
          </div>
        </div>
      </div>
</template>

<script>
export default {
  name: "EndlessCustomizationModel",
  data(){
    return{
      difficulty: "easy",
      timePerQuestion: "6",
      difficultyFullName: "Easy"
    }
  },
  methods: {
    submitModal(){
      this.$emit("runEndlessMode", {diff: this.difficulty, time: this.timePerQuestion})
    }
  }
}
</script>

<style scoped>

.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  transition: opacity .3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

/*.modal-body{
  overflow-y:scroll;
  overflow-x:hidden;
}*/

</style>