<template>
  <div class="column is-4 has-text-centered">
    <div class="box">
      <h2 class="subtitle">Free</h2>
      <h4 class="is-size-4">$0</h4>

      <p>Max 5 clients</p>
      <p>Max 5 leads</p>
      <hr />
      <template v-if="$store.state.team.plan === 'Free'">
        <button class="button is-info is-rounded is-medium" disabled>
          Subscribed
        </button>
      </template>
      <template v-else>
        <button
          @click="cancelPlan"
          class="button is-success is-rounded is-medium is-outlined"
        >
          Subscribe
        </button>
      </template>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Plan',
  methods: {
    cancelPlan() {
      this.$emit('cancelPlan')
    }
  }
}
</script>

<style></style>
