<template>
  <div class="home">
    <div class="hero is-success is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">Welcome to GanarCRM</h1>
        <h2 class="subtitle">GanarCRM is built for simple client management</h2>
        <p class="is-size-2 has-text-centered">Manage</p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="columns is-multiline">
          <div class="column is-4">
            <div class="box has-text-centered">
              <p class="is-size-3 mt-4 mb-4">Your Team</p>

              <p>You can manage your team</p>
            </div>
          </div>
          <div class="column is-4">
            <div class="box has-text-centered">
              <h2 class="is-size-3 mt-4 mb-4">Your Clients</h2>

              <p>You can manage your clients</p>
            </div>
          </div>
          <div class="column is-4">
            <div class="box has-text-centered">
              <p class="is-size-3 mt-4 mb-4">Your Leads</p>

              <p>You can manage your leads</p>
            </div>
          </div>

          <div class="column is-12 has-text-centered">
            <template v-if="$store.state.user.isAuthenticated">
              <router-link
                :to="{ name: 'Team' }"
                class="button is-info is-size-4 mt-6 mb-6 is-rounded"
                >My Team</router-link
              >
            </template>
            <template v-else>
              <router-link
                :to="{ name: 'SignUp' }"
                class="button is-info is-size-4 mt-6 mb-6 is-rounded"
                >Click to get started</router-link
              >
            </template>
          </div>

          <hr />
        </div>
      </div>
    </section>
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: "Home",
}
</script>
