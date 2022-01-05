<template>
  <div class="column is-4 has-text-centered">
    <div class="box">
      <h2 class="subtitle">Big team</h2>
      <h4 class="is-size-4">$25</h4>

      <p>Max 50 clients</p>
      <p>Max 50 leads</p>
      <hr />
      <template v-if="$store.state.team.plan === 'Big team'">
        <button class="button is-info is-rounded is-medium" disabled>
          Subscribed
        </button>
        <button
          class="button is-medium is-rounded is-light is-danger"
          @click="$emit('cancelPlan')"
        >
          Cancel
        </button>
      </template>
      <template v-else>
        <button
          @click="$emit('subscribe', 'bigteam')"
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
  name: 'BigTeamPlan',
  emits: ['subscribe', 'cancelPlan'],
  methods: {
    // cancelPlan() {
    //   this.$emit("cancelPlan")
    // },
    // subscribe(plan) {
    //   this.$emit("subscribe", plan)
    // },
  },
}
</script>
