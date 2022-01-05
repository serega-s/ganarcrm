<template>
  <div class="column is-4 has-text-centered">
    <div class="box">
      <h2 class="subtitle">Small team</h2>
      <h4 class="is-size-4">$10</h4>

      <p>Max 15 clients</p>
      <p>Max 15 leads</p>
      <hr />
      <template v-if="$store.state.team.plan === 'Small team'">
        <button class="button is-info is-rounded is-medium" disabled>
          Subscribed
        </button>
        <button
          class="button is-medium is-rounded is-light is-danger"
          @click="cancelPlan"
        >
          Cancel
        </button>
      </template>
      <template v-else>
        <button
          @click="subscribe('smallteam')"
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
  // name: "SmallTeamPlan",
  methods: {
    cancelPlan() {
      this.$emit("cancelPlan")
    },
    subscribe(plan) {
      this.$emit("subscribe", plan)
    },
  },
}
</script>
