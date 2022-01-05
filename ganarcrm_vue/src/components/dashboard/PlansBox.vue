<template>
  <div class="columns">
    
  </div>
</template>

<script>
export default {
  methods: {
    cancelPlan() {
      this.$emit("cancelPlan")
    },
    subscribe(plan) {
      this.$emit("subscribe", plan)
    },
  }
}
</script>

<style></style>
