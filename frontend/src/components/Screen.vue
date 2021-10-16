<template>
  <div class="equation_canvas px-4 d-flex flex-fill" style="max-height: 50%">
        <div class="card bg-light flex-fill text-dark border-0 m-0 p-0" id="eq">
          <div class="card-body d-flex align-items-center justify-content-center">
            <span class="m-0 p-0 fs-1">{{ parentCurrentTask }} {{ parentInputNumber }} </span>

            <b-spinner label="Spinning" v-if="inputChecking === 0"></b-spinner>
            <b-spinner type="grow" label="Spinning" v-else-if="inputChecking === 1" variant="danger"></b-spinner>
            <b-spinner type="grow" label="Spinning" v-else-if="inputChecking === 2" variant="success"></b-spinner>
          </div>
        </div>
      </div>
</template>

<script>
export default {
  name: "Screen",
  props: {
    inputChecking: Number,
    parentCurrentTask: String,
    parentInputNumber: String
  },
}
</script>

<style scoped>

</style>