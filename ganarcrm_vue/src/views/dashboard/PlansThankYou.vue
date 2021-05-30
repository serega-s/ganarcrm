<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Thank you</h1>

        <router-link :to="{ name: 'Team' }" class="button is-primary">
          Back to Team
        </router-link>
      </div>

      <div class="column is-4">
        <p>Thank you for subscribing to a plan!</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PlansThankYou",
}
</script>
